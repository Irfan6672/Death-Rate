# DATA COLLECTION:  
# Age-specific death rates for COPD in 2019 were retrieved for the
# United States and Uganda from the provided website. WHO standard
# population data and total populations for both countries in 2019
# were obtained from reliable sources.

# CRUDE DEATH RATE CALCULATION:
# Total deaths were computed by summing age-specific death rates per
# 100,000 across all age groups. These totals were divided by the
# respective total populations and multiplied by 100,000 to yield
# crude death rates.

# AGE-STANDARDIZED DEATH RATE CALCULATION:
# Utilizing the WHO standard population, age-specific death rates for
# each country were applied to derive expected deaths per age group.
# These were summed to obtain total expected deaths. The total was
# then divided by the standard population and multiplied by 100,000
# to generate age-standardized death rates.

# ASSUMPTIONS:
# Assumptions include the accuracy and representativeness of
# age-specific death rates and the suitability of the WHO standard
# population for age-standardization.

# REASONING FOR DIFFERENCES:
# Crude death rate reflect actual death rates, while age-standardized
# rates adjust for differences in age structures between populations.
# Disparities between the two metrics arise due to variations in age
# distributions among populations.


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
age_specific_death_rate_df.rename(
    columns={'Age group (years)' : 'age_group_years',
            'Death rate, United States, 2019' : 'us_death_rate_2019',
            'Death rate, Uganda, 2019' : 'uganda_death_rate_2019'},
            inplace= True)

# creating separate dataframes for us and uganda
us_age_specific_death_rate_df = pd.DataFrame(
    {'age_group' : age_specific_death_rate_df['age_group_years'],
    'death_rate' : age_specific_death_rate_df['us_death_rate_2019']})
uganda_age_specific_death_rate_df = pd.DataFrame(
    {'age_group' : age_specific_death_rate_df['age_group_years'],
    'death_rate' : age_specific_death_rate_df['uganda_death_rate_2019']})


# creating crude death rate calculation function
def crude_death_rate_calculation(dataframe, population):

    total_death_rate = dataframe['death_rate'].sum()
    crude_death_rate = round(total_death_rate / population * 100000, 1)
    return crude_death_rate


# creating age standardized death rate calculation function
def age_standardized_death_rate_calculation(dataframe):

    merged_df = pd.merge(who_standard_population_df, dataframe, on='age_group')
    merged_df['WHO_world_standard_proportion'] = merged_df['Percentage'] / 100
    merged_df['ASDR'] = merged_df['death_rate'] * merged_df['WHO_world_standard_proportion']
    age_standarized_death_rate = merged_df['ASDR'].sum()
    return round(age_standarized_death_rate, 1)


# Crude Death Rate Calculation
us_crude_death_rate = crude_death_rate_calculation(
    us_age_specific_death_rate_df, us_population)
uganda_crude_death_rate = crude_death_rate_calculation(
    uganda_age_specific_death_rate_df, uganda_population)


# Age Standardized Death Rate Calculation
us_age_standardized_death_rate = age_standardized_death_rate_calculation(
    us_age_specific_death_rate_df)
uganda_age_standardized_death_rate = age_standardized_death_rate_calculation(
    uganda_age_specific_death_rate_df)


# RESULT
print(f'CRUDE DEATH RATE:\
\nUnited States: {us_crude_death_rate} deaths per 100,000 people\
\nUganda: {uganda_crude_death_rate} deaths per 100,000 people' )

print(f'\nAGE-STANDARDIZED DEATH RATE:\
\nUnited States: {us_age_standardized_death_rate} deaths per 100,000 people\
\nUganda: {uganda_age_standardized_death_rate} deaths per 100,000 people')
