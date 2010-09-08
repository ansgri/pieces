# Rosenblatt's perceptron

data(iris)

dd <- iris[iris$Species != "versicolor", -(3:4)]
#dd <- dd[-42, ] # this point breaks linear separation (at least w/o intercept)
dm <- data.matrix(dd[, 1:2])
dm <- cbind(dm, 1) # to add intercept to the separating plane
dc <- rep(1, nrow(dm))
dc[dd$Species == "virginica"] <- -1

trainPerceptron <- function(dm, dc) {
  result <- list()
  oldW <- c()
  w <- rep(0, ncol(dm))
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
    plot(dm[,1:2], main=paste("step", s), pch=ifelse(dc > 0, 1, 2), sub=paste(w, collapse=' '))
    abline(-w[3] / w[2], -w[1] / w[2])
  }
}


# pc <- trainPerceptron(dm, dc)
# plotPerceptronSteps(pc, dm, dc, length(pc))
# png("perceptron-biased.png", width=600, height=600)
# par(mfrow=c(2,2))
# plotPerceptronSteps(pc, dm, dc, c(20, 50, 250, length(pc)))
# dev.off()
