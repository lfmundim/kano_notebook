import pandas as pd

def generate_feature_percentages(df):
    """
    Generates a table of percentages for each Kano category per feature.
    :param df: DataFrame with Kano categories
    :return: DataFrame with percentages of each Kano category per feature
    """
    feature_percentages = df.groupby('Feature')['Kano Category'].value_counts(normalize=True).unstack(fill_value=0) * 100
    return feature_percentages

def generate_feature_counts(df):
    """
    Generates a table of absolute counts for each Kano category per feature.
    :param df: DataFrame with Kano categories
    :return: DataFrame with counts of each Kano category per feature
    """
    feature_counts = df.groupby('Feature')['Kano Category'].value_counts().unstack(fill_value=0)
    return feature_counts

def generate_highest_category_table(feature_percentages):
    """
    Generates a table with the feature, the highest percentile, and the corresponding category.
    :param feature_percentages: DataFrame with percentages of each Kano category per feature
    :return: DataFrame with feature, highest percentage, and category
    """
    highest_category_table = []

    for feature, row in feature_percentages.iterrows():
        max_percentage = row.max()
        max_category = row.idxmax()

        highest_category_table.append({
            "Feature": feature,
            "Highest Percentile": max_percentage,
            "Category": max_category
        })

    return pd.DataFrame(highest_category_table)