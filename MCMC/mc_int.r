# Define the integrand function
f <- function(x) exp(-x^2)

# Define the probability density function for importance sampling
g <- function(x) 2*dnorm(x, mean=2, sd=1)

# Define the integration domain
a <- -Inf
b <- Inf

# Define the number of random points to generate
N <- 10000

# Generate random points from the PDF g
x <- rnorm(N, mean=2, sd=1)

# Evaluate the integrand function at each point
fx <- f(x)

# Calculate the weights for each point using importance sampling
w <- fx / g(x)

# Estimate the integral using importance sampling
I <- mean(w) * integrate(g, a, b)$value

# Estimate the variance of the estimation
var_I <- var(w) / N

# Print the estimated integral and its variance
cat("Estimated integral:", I, "\n")
cat("Variance of the estimation:", var_I)
