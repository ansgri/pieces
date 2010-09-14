coeffs = [1 1 4 -5 -3 5 1]
N_DATA_POINTS = 30
x = sort(rand([N_DATA_POINTS 1]) * 2)
y = polyval(coeffs, x)
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

pows = 1:15;
rmss = arrayfun(@(p)rmsForPower(x, y, p), pows);
plot(pows, rmss);
