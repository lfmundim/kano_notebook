import pandas as pd
from configuration import pair_to_category, functional_score_map, dysfunctional_score_map, indifferent_category, response_mapping
# from configuration import *

def apply_kano_categorization(df):
    """
    Applies Kano analysis on the given DataFrame.
    :param df: DataFrame containing paired Functional and Dysfunctional responses
    :return: DataFrame with Kano categories and another with scores
    """
    categories = []
    scores = []
    print(pair_to_category)

    for i in range(1, len(df.columns), 2):
        functional_column = df.columns[i]
        dysfunctional_column = df.columns[i + 1]

        # Map scores for functional and dysfunctional responses
        df[functional_column + '_Score'] = df[functional_column].map(functional_score_map)
        df[dysfunctional_column + '_Score'] = df[dysfunctional_column].map(dysfunctional_score_map)

        # Calculate averages
        functional_avg = df[functional_column + '_Score'].mean()
        dysfunctional_avg = df[dysfunctional_column + '_Score'].mean()

        scores.append({
            "Feature": functional_column,
            "Av. Functional Score": round(functional_avg, 2),
            "Av. Dysfunctional Score": round(dysfunctional_avg, 2)
        })

        for _, row in df.iterrows():
            response_func = response_mapping.get(row[functional_column])
            response_dys = response_mapping.get(row[dysfunctional_column])

            category = pair_to_category.get((response_func.strip(), response_dys.strip()), indifferent_category)

            categories.append({"Feature": functional_column, "User ID": row.iloc[0], "Kano Category": category})

    return pd.DataFrame(categories), pd.DataFrame(scores)