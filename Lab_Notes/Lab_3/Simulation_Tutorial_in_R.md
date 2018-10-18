Simulation\_Tutorial
================
Nora Nickels
10/17/2018

Simulating Data: R Tutorial
---------------------------

Perspectives of Computational Analysis - Fall 2017
--------------------------------------------------

``` r
# Load necessary libraries and set seed.
library(tidyverse)
set.seed(1234)
```

#### To simulate data, the first step is creating a function that defines your data generating process.

``` r
# Create a function to calculate increasing annual income.

# In your homework assignment:
# you will set: 
# base_inc (average starting income)
# rho (positive dependence of today's income on last period's income)
# g (long-run annual growth rate of income)
# sigma (standard deviation)

# For the sake of this tutorial, we'll set only a few simple parameters:
# I define my starting income, my sd, a random parameter "n" (for nora), my start year (my graduation year), and n_years

income_nora <- function(base_inc, sigma, n, n_years, start_year = 2019){
  
  # define normally distributed errors: we set the mean and the sd of these errors
  # the error term should be a distributed lognormal
  # rnorm() is a density distribution function for the normal distribution with mean equal to mean and sd = sd
  errors_nora <- rnorm(n_years, mean = 0, sd = sigma)
  
  # define our vector, which will define the log income over n years
  income_log_nora <- vector("numeric", n_years)
  
  # use for loop to define the process
  # year is the unit that will change over time; AKA, our data frame will have one simulated income per year
  for(year in seq_len(n_years)){
    if(year == 1){
      income_log_nora[[year]] <- log(base_inc) + errors_nora[[year]]
    } else {
      income_log_nora[[year]] <- log(base_inc) + n + errors_nora[[year]]
    }
  }
  
  # Output of a data frame, with variables of income and year.
  # This translates the log value back into income
  # and also translates the corresponding year that goes along with that simulated income
  data_frame(inc = exp(income_log_nora),
             year = 2019 + seq_len(n_years) - 1)
}
```

#### To simulate data, the next step is plugging those into the income process you defined to simulate your lifetime income.

``` r
# Example simulation

# Define the simulation; 100 simulations, each of 60 years length.
# I will work for 60 years after I graduate in this simulation. Because I will live a long and healthy life!

n_sims <- 100
n_years <- 60

# Now use rerun function to simulate the data iterations, then create a data frame 

simulated_income_nora <- n_sims %>%
  # in rerun(), I define my parameters
  # rerun generates data
  rerun(income_nora(base_inc = 40000, sigma = .1, n = 4,
                      n_years = n_years, start_year = 2019)) %>%
  # use bind_rows() to create a data frame
  bind_rows(.id = "id") %>%
  # id will define which simulation we are looking at
  select(id, year, inc)

# View the data frame we've created.
View(simulated_income_nora)

head(simulated_income_nora)
```

    ## # A tibble: 6 x 3
    ##   id     year      inc
    ##   <chr> <dbl>    <dbl>
    ## 1 1      2019   35452.
    ## 2 1      2020 2245363.
    ## 3 1      2021 2434079.
    ## 4 1      2022 1727291.
    ## 5 1      2023 2279684.
    ## 6 1      2024 2297289.

``` r
# what you'll end up with is 100 simulations, each with 60 years of work and an income for each of those years. 
# you've done it!
```

``` r
# Plot the first income path. Id is the variable that defines which simulated income path.
simulated_income_nora %>%
  filter(id == 1) %>%
  ggplot(aes(year, inc)) +
  geom_line() +
  labs(title = "Simulated income increase over time (one simulation)",
       x = "Year", 
       y = "Annual Income") +
  scale_y_continuous(labels = scales::dollar)
```

![](Simulation_Tutorial_files/figure-markdown_github/plot-1.png)
