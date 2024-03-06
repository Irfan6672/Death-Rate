# Age-specific death rates for COPD in 2019
age_groups = ["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", 
              "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85+"]
death_rates_us = [0.04, 0.02, 0.02, 0.02, 0.06, 0.11, 0.29, 0.56, 1.42, 4, 14.13, 37.22, 66.48, 
                  108.66, 213.1, 333.06, 491.1, 894.45]
death_rates_uganda = [0.4, 0.17, 0.07, 0.23, 0.38, 0.4, 0.75, 1.11, 2.04, 5.51, 13.26, 33.25, 
                      69.62, 120.78, 229.88, 341.06, 529.31, 710.4]

# Population figures
us_population = 334.3e6
uganda_population = 42.9e6

# WHO Standard Population weights
# Age groups: 0-4, 5-9, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39, 40-44, 45-49, 50-54, 55-59, 60-64, 65-69, 70-74, 75-79, 80-84, 85+
# Corresponding weights: 230797, 248187, 244535, 252041, 256392, 263737, 285722, 287381, 283885, 284298, 269193, 257016, 237270, 207438, 153038, 103392, 60251, 21346
who_standard_weights = [230797, 248187, 244535, 252041, 256392, 263737, 285722, 287381, 283885, 
                        284298, 269193, 257016, 237270, 207438, 153038, 103392, 60251, 21346]

# Calculate crude death rate for both countries
crude_death_rate_us = sum(death_rates_us) / us_population * 100000
crude_death_rate_uganda = sum(death_rates_uganda) / uganda_population * 100000

# Calculate age-standardized death rate for both countries
asr_us = sum(rate * weight for rate, weight in zip(death_rates_us, who_standard_weights)) / sum(who_standard_weights) / us_population * 100000
asr_uganda = sum(rate * weight for rate, weight in zip(death_rates_uganda, who_standard_weights)) / sum(who_standard_weights) / uganda_population * 100000

# Print results
print("Crude Death Rate for COPD in 2019:")
print(f"United States: {crude_death_rate_us:.1f} deaths per 100,000 people")
print(f"Uganda: {crude_death_rate_uganda:.1f} deaths per 100,000 people\n")

print("Age-Standardized Death Rate for COPD in 2019:")
print(f"United States: {asr_us:.1f} deaths per 100,000 people")
print(f"Uganda: {asr_uganda:.1f} deaths per 100,000 people")
