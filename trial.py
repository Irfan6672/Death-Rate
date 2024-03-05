# Age-specific death rates of COPD for the United States and Uganda in 2019
copd_death_rates = {
    "United States": {
        "0-4": 0.04, "5-9": 0.02, "10-14": 0.02, "15-19": 0.02,
        "20-24": 0.06, "25-29": 0.11, "30-34": 0.29, "35-39": 0.56,
        "40-44": 1.42, "45-49": 4, "50-54": 14.13, "55-59": 37.22,
        "60-64": 66.48, "65-69": 108.66, "70-74": 213.1, "75-79": 333.06,
        "80-84": 491.1, "85+": 894.45
    },
    "Uganda": {
        "0-4": 0.4, "5-9": 0.17, "10-14": 0.07, "15-19": 0.23,
        "20-24": 0.38, "25-29": 0.4, "30-34": 0.75, "35-39": 1.11,
        "40-44": 2.04, "45-49": 5.51, "50-54": 13.26, "55-59": 33.25,
        "60-64": 69.62, "65-69": 120.78, "70-74": 229.88, "75-79": 341.06,
        "80-84": 529.31, "85+": 710.4
    }
}

# Total population of the United States and Uganda in 2019
us_population = 334.3e6
uganda_population = 42.9e6

# WHO standard population (age groups 0-4, 5-9, ..., 80-84, 85+)
who_standard_population = [98416, 97772, 97649, 98222, 101660, 110599, 122577, 109451, 82767, 64307, 46266, 31202, 20490, 13162, 8273, 4862, 2560, 1092, 260]

def calculate_crude_death_rate(death_rates, population):
    total_deaths = sum(death_rates.values())
    crude_death_rate = (total_deaths / population) * 100000
    return round(crude_death_rate, 1)

def calculate_age_standardized_death_rate(death_rates):
    asr = 0
    for age_group, death_rate in death_rates.items():
        asr += death_rate * who_standard_population[int(age_group.split('-')[0]) // 5]
    asr /= sum(who_standard_population)
    asr *= 100000
    return round(asr, 1)

# Calculate and print crude death rates for both countries
us_crude_death_rate = calculate_crude_death_rate(copd_death_rates["United States"], us_population)
uganda_crude_death_rate = calculate_crude_death_rate(copd_death_rates["Uganda"], uganda_population)

print("Crude Death Rate (per 100,000 people) for COPD in 2019:")
print("United States:", us_crude_death_rate)
print("Uganda:", uganda_crude_death_rate)

# # Calculate and print age-standardized death rates for both countries
# us_age_standardized_death_rate = calculate_age_standardized_death_rate(copd_death_rates["United States"])
# uganda_age_standardized_death_rate = calculate_age_standardized_death_rate(copd_death_rates["Uganda"])

# print("\nAge-Standardized Death Rate (per 100,000 people) for COPD in 2019 (WHO Standard Population):")
# print("United States:", us_age_standardized_death_rate)
# print("Uganda:", uganda_age_standardized_death_rate)
