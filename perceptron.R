# Rosenblatt's perceptron

data(iris)

dd <- iris[iris$Species != "versicolor", -(3:4)]
dm <- data.matrix(dd[, 1:2])
dc <- rep(1, nrow(dm))
dc[dd$Species == "virginica"] <- -1

trainPerceptron <- function(dm, dc) {
  oldW <- c()
  w <- c(0, 0)
  while (!identical(w, oldW)) {
    oldW <- w
    for (i in 1:nrow(dm)) {
      pred <- sign(dm[i,] %*% w)
      w = w + (dc[i] - pred) * dm[i, ]
    }
    cat(w, "\n")
  }
  w
}
