# Rosenblatt's perceptron

data(iris)

dd <- iris[iris$Species != "versicolor", -(3:4)]
dd <- dd[-42, ] # this point breaks linear separation (at least w/o intercept)
dm <- data.matrix(dd[, 1:2])
dc <- rep(1, nrow(dm))
dc[dd$Species == "virginica"] <- -1

trainPerceptron <- function(dm, dc) {
  result <- list()
  oldW <- c()
  w <- c(0, 0)
  while (!identical(w, oldW)) {
    oldW <- w
    for (i in 1:nrow(dm)) {
      pred <- sign(dm[i,] %*% w)
      w = w + (dc[i] - pred) * dm[i, ]
    }
    # cat(w, "\n")
    result <- c(result, list(w))
  }
  result
}

plotPerceptronSteps <- function(pcResult, dm, dc, steps) {
  for (s in steps) {
    w <- pcResult[[s]]
    plot(dm, main=paste("step", s), pch=ifelse(dc > 0, 1, 2))
    abline(0, -w[1] / w[2])
  }
}


# pc <- trainPerceptron(dm, dc)
# plotPerceptronSteps(pc, dm, dc, length(pc))
# plotPerceptronSteps(pc, dm, dc, c(20, 25, 27, length(pc)))
