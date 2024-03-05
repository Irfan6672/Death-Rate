# Data Collection: I retrieved the age-specific death rates from COPD
# for both the United States and Uganda for 2019. This data will be
# used to calculate both crude and age-standardized death rates.

# Crude Death Rate Calculation: The crude death rate is calculated by
# dividing the total number of deaths by the total population and 
# then multiplying by 100,000 to express it per 100,000 people. For 
# both countries, I will sum up all age-specific death rates to
# obtain the total deaths, and then divide by the total population.

# Age-Standardized Death Rate Calculation: Age-standardized death
# rates allow for a fair comparison between populations with
# different age structures. To calculate this, I will use the WHO
# standard population. First, I'll apply the age-specific death
# rates of each country to the WHO standard population to get the
# expected number of deaths. Then, I'll divide the total expected
# deaths by the standard population and multiply by 100,000 to get
# the age-standardized death rate.

# Assumptions: I assume that the age-specific death rates provided
# are accurate and representative of the entire population.
# Additionally, I assume that the WHO standard population is
# appropriate for age-standardization.

# Reasoning for Differences: Crude death rates reflect the actual
# death rates in the population, whereas age-standardized death rates
# adjust for differences in age distributions among populations.
# Therefore, differences between crude and age-standardized death
# rates may arise due to variations in age structures between the
# populations being compared.


import pandas as pd


# obtained the population of us from 
# https://www.worldometers.info/world-population/
us_population = 334.3e6
uganda_population = 42.9e6


# reading the csv file
age_specific_death_rate_df = pd.read_csv("data.csv")

age_specific_death_rate_df.rename(columns={'Age group (years)' : 'age_group_years',
                'Death rate, United States, 2019' : 'us_death_rate_2019',
                'Death rate, Uganda, 2019' : 'uganda_death_rate_2019'},
                 inplace= True)


# Crude Death Rate Calculation
def crude_death_rate_calculation(dataframe = age_specific_death_rate_df):
    us_total_death_rate = dataframe['us_death_rate_2019'].sum()
    uganda_total_death_rate = dataframe['uganda_death_rate_2019'].sum()

    us_crude_death_rate = (us_total_death_rate / us_population) * 100000
    uganda_crude_death_rate = uganda_total_death_rate / uganda_population * 100000

    print(us_total_death_rate / us_population * 100000)
    print(uganda_total_death_rate / uganda_population * 100000)

    return f'Crude Death Rate (per 100,000 people) for 2019\
    \nUnited States: {round(us_crude_death_rate, 1)} deaths per 100,000 people\
    \nUganda: {round(uganda_crude_death_rate,1)} deaths per 100,000 people\n'


# To calculate the age-standardized death rate for both the United
# States and Uganda based on the provided data, we need to apply
# age-standardization techniques. This involves adjusting the death
# rates for each age group to a standard population distribution to
# eliminate the effects of differences in age structures between
# populations. Here's how we can do it:

# Define a standard population distribution. We will use the World
# Health Organization (WHO) standard population distribution.

# For each country, calculate the expected number of deaths for each
# age group by multiplying the death rate for that age group by the
# corresponding population of the standard population distribution.

# Sum up the expected number of deaths across all age groups for each
# country.

# Calculate the age-standardized death rate by dividing the total
# expected deaths by the total standard population and multiplying by
# 100,000 to express it per 100,000 people.


# Age Standardized Death Rate Calculation
def age_standardized_death_rate_calculation(dataframe = age_specific_death_rate_df):
    
    us_expected_death = sum(dataframe['us_death_rate_2019'] * 10000)
    uganda_expected_death = sum(dataframe['uganda_death_rate_2019'] * 10000)

    us_age_standarized_death_rate = us_expected_death / us_population * 100000
    uganda_age_standarized_death_rate = uganda_expected_death / uganda_population * 100000

    return f'Age-standardized Death Rate (per 100,000 people) for 2019\
    \nUnited States: {round(us_age_standarized_death_rate, 1)} deaths per 100,000 people\
    \nUganda: {round(uganda_age_standarized_death_rate,1)} deaths per 100,000 people'
    

print(crude_death_rate_calculation())
print(age_standardized_death_rate_calculation())

# total standard population calculated as 10,000 multiplied
# by total number of age groups i.e. 18, this is cause the
# standard population for each age group is taken as 10,000
total_standard_population = 10000 * 18
