# Define the WHO standard population distribution (per 100,000 people)
who_standard_population = {
    '0-4': 10000,
    '5-9': 10000,
    '10-14': 10000,
    '15-19': 10000,
    '20-24': 10000,
    '25-29': 10000,
    '30-34': 10000,
    '35-39': 10000,
    '40-44': 10000,
    '45-49': 10000,
    '50-54': 10000,
    '55-59': 10000,
    '60-64': 10000,
    '65-69': 10000,
    '70-74': 10000,
    '75-79': 10000,
    '80-84': 10000,
    '85+': 10000
}

# Provided death rate data for the United States and Uganda
death_rates_us = {
    '0-4': 0.04,
    '5-9': 0.02,
    '10-14': 0.02,
    '15-19': 0.02,
    '20-24': 0.06,
    '25-29': 0.11,
    '30-34': 0.29,
    '35-39': 0.56,
    '40-44': 1.42,
    '45-49': 4,
    '50-54': 14.13,
    '55-59': 37.22,
    '60-64': 66.48,
    '65-69': 108.66,
    '70-74': 213.1,
    '75-79': 333.06,
    '80-84': 491.1,
    '85+': 894.45
}

death_rates_uganda = {
    '0-4': 0.4,
    '5-9': 0.17,
    '10-14': 0.07,
    '15-19': 0.23,
    '20-24': 0.38,
    '25-29': 0.4,
    '30-34': 0.75,
    '35-39': 1.11,
    '40-44': 2.04,
    '45-49': 5.51,
    '50-54': 13.26,
    '55-59': 33.25,
    '60-64': 69.62,
    '65-69': 120.78,
    '70-74': 229.88,
    '75-79': 341.06,
    '80-84': 529.31,
    '85+': 710.4
}

# Calculate the expected number of deaths for each country
expected_deaths_us = sum(death_rates_us[age_group] * who_standard_population[age_group] for age_group in death_rates_us)
expected_deaths_uganda = sum(death_rates_uganda[age_group] * who_standard_population[age_group] for age_group in death_rates_uganda)

# Calculate the total standard population
total_standard_population = sum(who_standard_population.values())

# Calculate the age-standardized death rate for each country
age_standardized_death_rate_us = (expected_deaths_us / total_standard_population) * 100000
age_standardized_death_rate_uganda = (expected_deaths_uganda / total_standard_population) * 100000

# Output results
print(expected_deaths_us)
print(total_standard_population)
print("Age-Standardized Death Rate (per 100,000 people) for 2019:")
print("United States:", round(age_standardized_death_rate_us, 1))
print("Uganda:", round(age_standardized_death_rate_uganda, 1))
