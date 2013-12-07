#!/usr/bin/env python2

import cv2
import numpy as np


def masked_boxfilter(img, mask, repl, fill_threshold=6):
    res = np.zeros(img.shape, 'float32')
    acc = np.zeros(img.shape, 'uint8')
    imask = ~mask
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            shifted = np.roll(np.roll(img, dy, axis=0), dx, axis=1)
            res[imask] += shifted[imask]
            acc[imask] += 1
    res[imask] /= acc[imask]
    res = np.array(res + 0.5, img.dtype)
    res[acc < fill_threshold] = repl[acc < fill_threshold]
    # print res.dtype
    return res


def iteration(img, src, edges):
    # img = cv2.boxFilter(img, -1, (3, 3))
    mask = edges != 0
    return masked_boxfilter(img, mask, src)


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('source_image')
    args = p.parse_args()

    src = cv2.imread(args.source_image)
    cv2.imshow('src', src)

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(cv2.GaussianBlur(gray, (0, 0), 7), 
                      100, 200, apertureSize=7)

    vis = src.copy()
    # edges = cv2.dilate(edges, np.ones((3, 3)))
    vis[edges != 0] = (0, 0, 0)
    cv2.imshow('vis', vis)

    img = src.copy()
    # prev_img = src.copy()
    while True:
        cv2.imshow('result', img)
        ch = 0xFF & cv2.waitKey(10)
        if ch == 27:
            break
        img = iteration(img, src, edges)

        # cv2.imshow('diff', np.uint8(np.abs(np.float32(img) - np.float32(prev_img))))
        # prev_img = img.copy()

    cv2.destroyAllWindows()
