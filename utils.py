from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd


def pass_rates(data, threshold):
    # Assuming you have these already calculated in your notebook
    aka_name_counts = data['AKA Name'].value_counts()
    dba_name_counts = data['DBA Name'].value_counts()

    # Define outliers for AKA Name and DBA Name
    outliers_aka_name = aka_name_counts[aka_name_counts <= threshold]
    outliers_dba_name = dba_name_counts[dba_name_counts <= threshold]

    # Create masks for the outliers
    mask_aka_outliers = data['AKA Name'].isin(outliers_aka_name.index)
    mask_dba_outliers = data['DBA Name'].isin(outliers_dba_name.index)

    # Calculate pass rates
    pass_rate_common_aka = data.loc[~mask_aka_outliers, 'Results'].mean()
    pass_rate_rare_aka = data.loc[mask_aka_outliers, 'Results'].mean()

    pass_rate_common_dba = data.loc[~mask_dba_outliers, 'Results'].mean()
    pass_rate_rare_dba = data.loc[mask_dba_outliers, 'Results'].mean()

    return {
        'AKA Name': {
            'Common': pass_rate_common_aka,
            'Rare': pass_rate_rare_aka
        },
        'DBA Name': {
            'Common': pass_rate_common_dba,
            'Rare': pass_rate_rare_dba
        }
    }

