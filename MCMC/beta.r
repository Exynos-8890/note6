# Define the beta distribution density function
dbeta <- function(x, shape1 = 0.5, shape2 = 0.5) {
  x^(shape1-1) * (1-x)^(shape2-1) / beta(shape1, shape2)
}

# Set the maximum value of the target density
M <- 10

# Set the number of samples to generate
n_samples <- 100000

# Initialize an empty vector to store the samples
samples <- numeric(n_samples)

# Generate samples using accept-reject algorithm
i <- 1
while (i <= n_samples) {
  # Generate a proposal from the uniform distribution
  x_proposal <- runif(1)
  
  # Generate a value from the uniform distribution to compare against the target density
  u <- runif(1)
  
  # Compute the ratio of the target density to the proposal density
  acceptance_ratio <- dbeta(x_proposal) / dbeta(0.5, 0.5)
  
  # Accept the proposal with probability min(acceptance_ratio, M) if u < acceptance_ratio / M
  if (u < acceptance_ratio / M) {
    samples[i] <- x_proposal
    i <- i + 1
  }
}

# Plot the generated samples
hist(samples, breaks = 50, freq = FALSE, main = "Beta Distribution")
curve(dbeta(x), add = TRUE, col = "red", lwd = 2)
