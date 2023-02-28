f <- c(0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1)
N <- 100000
d <- rep(0, N)
x <- 5
for (i in 1:N) {
  U <- runif(1)
  if (x == 2) {
    if (U < 0.5) {
      y <- 3
    } else {
      y <- 2
    }
  } else if (x == 12) {
    if (U < 0.5) {
      y <- 11
    } else {
      y <- 12
    }
  } else {
    if (U < 0.5) {
      y <- x - 1
    } else {
      y <- x + 1
    }
  }
  h <- min(1, f[y] / f[x])
  U <- runif(1)
  if (U < h) {
    x <- y
  }
  d[i] <- x
}
a <- 1:12
hist(d, breaks = a)
