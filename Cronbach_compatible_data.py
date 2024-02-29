!pip install pingouin

import numpy as np
import pandas as pd

# Function to generate survey data
def generate_survey_data(num_respondents, num_areas):
    # Randomly select a dominant response for each respondent
    dominant_responses = np.random.randint(0, 4, size=num_respondents)
    
    # Initialize survey data with dominant responses
    survey_data = np.zeros((num_respondents, num_areas), dtype=int)
    for i, response in enumerate(dominant_responses):
        survey_data[i] = response
    
    # Randomly choose a small subset of questions to deviate from dominant response
    for i in range(num_respondents):
        deviate_indices = np.random.choice(num_areas, size=int(0.6*num_areas), replace=False) #change(0.5*num_areas)
        for j in deviate_indices:
            survey_data[i, j] = np.random.randint(0, 4)  # Randomly select any response
    
    # Define Likert scale mapping
    likert_scale = {
        0: 'Constant',
        1: 'Frequent',
        2: 'Occasional',
        3: 'Never'
    }
    
    # Create DataFrame
    columns = [f'Area_{i+1}' for i in range(num_areas)]
    survey_df = pd.DataFrame(survey_data, columns=columns)
    
    return survey_df


import pingouin as pg

# Parameters
num_respondents = 380
num_areas = 9
target_alpha = 0.7  # Target Cronbach's alpha score

# Generate survey data and calculate Cronbach's alpha
alpha = 0
while alpha < target_alpha:
    survey_df = generate_survey_data(num_respondents, num_areas)
    alpha = pg.cronbach_alpha(data=survey_df)[0]


# Display Cronbach's alpha score
print("\nCronbach's alpha:", alpha)

survey_df.to_csv('NMQ_survey.csv')