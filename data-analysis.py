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




# from WHO refernce WHO Standard Population — Table 1 in 'Ahmad OB,
# Boschi-Pinto C, Lopez AD, Murray CJ, Lozano R, Inoue M (2001).
# Age standardization of rates: a new WHO standard.'
# Table of Standard WHO population



# obtained the population of us from 
# https://www.worldometers.info/world-population/


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

#IMPORTS
import pandas as pd


us_population = 334.3e6
uganda_population = 42.9e6


# reading the who standard population table .csv file
who_standard_population_df = pd.read_csv('who_standard_population.csv')
who_standard_population_df.rename(columns={'Age Group' : 'age_group',
                                        'Percentage (%)' : 'Percentage',
                                        'Population (assuming total population of 100000)' : 
                                        'Population'},
                                        inplace=True)
total_who_standard_population = sum(who_standard_population_df['Population'])


# reading the age specified death rate .csv file
age_specific_death_rate_df = pd.read_csv("data.csv")
age_specific_death_rate_df.rename(columns={'Age group (years)' : 'age_group_years',
                'Death rate, United States, 2019' : 'us_death_rate_2019',
                'Death rate, Uganda, 2019' : 'uganda_death_rate_2019'},
                 inplace= True)
us_age_specific_death_rate_df = pd.DataFrame({'age_group' : age_specific_death_rate_df['age_group_years'],
                                              'death_rate' : age_specific_death_rate_df['us_death_rate_2019']})
uganda_age_specific_death_rate_df = pd.DataFrame({'age_group' : age_specific_death_rate_df['age_group_years'],
                                              'death_rate' : age_specific_death_rate_df['uganda_death_rate_2019']})


# creating crude death rate calculation function
def crude_death_rate_calculation(dataframe, population):

    total_death_rate = dataframe['death_rate'].sum()
    crude_death_rate = round(total_death_rate / population * 100000, 1)
    return round(crude_death_rate, 1)


# creating age standardized death rate calculation function
def age_standardized_death_rate_calculation(dataframe, population):

    merged_df = pd.merge(who_standard_population_df, dataframe, on='age_group')
    merged_df['expected_death_rate'] = merged_df['Population'] * merged_df['death_rate']
    merged_df['WHO_world_standard_proportion'] = merged_df['Percentage'] / 100
    merged_df['ASDR'] = merged_df['death_rate'] * merged_df['WHO_world_standard_proportion']
    age_standarized_death_rate = merged_df['ASDR'].sum()
    return round(age_standarized_death_rate, 1)


# Crude Death Rate Calculation
us_crude_death_rate = crude_death_rate_calculation(us_age_specific_death_rate_df, us_population)
uganda_crude_death_rate = crude_death_rate_calculation(uganda_age_specific_death_rate_df, uganda_population)


# Age Standardized Death Rate Calculation
us_age_standardized_death_rate = age_standardized_death_rate_calculation(
    us_age_specific_death_rate_df, total_who_standard_population)
uganda_age_standardized_death_rate = age_standardized_death_rate_calculation(
    uganda_age_specific_death_rate_df, total_who_standard_population)


print(f'Crude Death Rate per 100,000 people\
\n\tUnited States: {us_crude_death_rate} deaths per 100,000 people\
\n\tUganda: {uganda_crude_death_rate} deaths per 100,000 people' )

print(f'\n\nAge-Standardized Death Rate per 100,000 people\
\n\tUnited States: {us_age_standardized_death_rate} deaths per 100,000 people\
\n\tUganda: {uganda_age_standardized_death_rate} deaths per 100,000 people')
