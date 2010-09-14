COEFFS = [1 1 4 -5 -3 5 1]
DATA_POINTS = 30
POWERS = 1:15
EXCLUSIONS = 10

x = sort(rand([DATA_POINTS 1]) * 2)
y = polyval(COEFFS, x)
y += randn([length(y) 1])
plot(x, y)

function m = powerMat(x, powers) 
  m = (x * ones([1 length(powers)])) .^ (ones([length(x) 1]) * powers);
end

function r = rmsForPower(x, y, pow)
  mm = powerMat(x, pow:-1:0);
  yFit = polyval(mm \ y, x);
  r = mean((yFit - y) .^ 2);
end

pows = POWERS;
rmss = arrayfun(@(p)rmsForPower(x, y, p), pows);

randPerm = randperm(length(x))
exIndices = sort(randPerm(1:EXCLUSIONS))
restIndices = sort(randPerm((EXCLUSIONS + 1):length(randPerm)))

function r = rmsForPowerEx(x, y, pow, exIndices, restIndices)
  xRest = x(restIndices)
  yRest = y(restIndices)

  mm = powerMat(xRest, pow:-1:0);
  yFit = polyval(mm \ yRest, x(exIndices));
  r = mean((yFit - y(exIndices)) .^ 2);
end

exNum = 10
rmssEx = arrayfun(@(p)rmsForPowerEx(x, y, p, exIndices, restIndices), pows);

% the resulting plot
semilogy(pows, [rmssEx; rmss]);
