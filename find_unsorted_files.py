#!/usr/bin/env python2

import os
import os.path as osp
import hashlib


def sha1_file(path):
    BLOCKSIZE = 2 ** 16
    h = hashlib.sha1()
    with open(path, 'rb') as f:
        while True:
            buf = f.read(BLOCKSIZE)
            if not buf:
                break
            h.update(buf)
    return h.digest()


def generate_file_paths(dir):
    for dirpath, _, filenames in os.walk(dir):
        for fn in filenames:
            yield osp.abspath(osp.join(dirpath, fn))


def build_dir_index(dir):
    result = {}
    for fullpath in generate_file_paths(dir):
        h = None
        try:
            h = sha1_file(fullpath)
        except IOError, e:
            print 'Error processing file {}: {}'.format(fullpath, e)
        result[fullpath] = h
    return result


def find_unsorted_files(unsorted_dir, sorted_dir):
    sorted_files_hashset = build_dir_index(sorted_dir).values()
    for fullpath in sorted(generate_file_paths(unsorted_dir)):
        status_char = '?'
        try:
            if sha1_file(fullpath) in sorted_files_hashset:
                status_char = ' '
            else:
                status_char = '*'
        except IOError, e:
            status_char = 'E'
        yield (status_char, fullpath)


def _print_files_info(lines, verbose=False, pretty=False, bare=False):
    prevpath = ''
    for status_char, fullpath in lines:
        if status_char == ' ' and not verbose:
            continue
        if bare and status_char != ' ':
            print fullpath
        elif pretty:
            prefix_len = len(osp.commonprefix((prevpath, fullpath)))
            if prefix_len > 0:
                prefix_len -= 1
            print '{}{} {}'.format(' ' * prefix_len, status_char, fullpath[prefix_len:])
        else:
            print '{} {}'.format(status_char, fullpath)
        prevpath = fullpath


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('unsorted_dir')
    p.add_argument('sorted_dir')
    p.add_argument('-v', '--verbose', action='store_true')
    p.add_argument('-p', '--pretty', action='store_true')
    p.add_argument('-b', '--bare', action='store_true')
    args = p.parse_args()
    
    ff = find_unsorted_files(args.unsorted_dir, args.sorted_dir)
    _print_files_info(ff, args.verbose, args.pretty, args.bare)
