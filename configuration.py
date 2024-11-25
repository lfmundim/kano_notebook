LIKE = 'Like'
EXPECT = 'Expect'
NEUTRAL = 'Neutral'
TOLERATE = 'Tolerate'
DISLIKE = 'Dislike'

# Define score mappings
functional_score_map = {
    'Like': 4,
    'Expect': 2,
    'Neutral': 0,
    'Tolerate': -1,
    'Dislike': -2
}

dysfunctional_score_map = {
    'Like': -2,
    'Expect': -1,
    'Neutral': 0,
    'Tolerate': 2,
    'Dislike': 4
}

like_response = 'Gostaria que fosse assim'
expect_response = 'Estou à espera que seja assim'
neutral_response = 'Seria indiferente'
tolerate_response = 'Toleraria que fosse assim'
dislike_response = 'Não gostaria que fosse assim'

attractive_category = 'Atrativo'
performance_category = 'Desempenho'
must_be_category = 'Básico'
reverse_category = 'Reverso'
questionable_category = 'Questionável'
indifferent_category = 'Indiferente'

# Consider left to be functional response and right dysfunctional
# Define the pairs and their categories
pair_to_category = {
    (LIKE, TOLERATE): attractive_category,
    (LIKE, NEUTRAL): attractive_category,
    (LIKE, EXPECT): attractive_category,
    (LIKE, DISLIKE): performance_category,
    (EXPECT, DISLIKE): must_be_category,
    (NEUTRAL, DISLIKE): must_be_category,
    (TOLERATE, DISLIKE): must_be_category,
    (DISLIKE, LIKE): reverse_category,
    (DISLIKE, TOLERATE): reverse_category,
    (DISLIKE, NEUTRAL): reverse_category,
    (DISLIKE, EXPECT): reverse_category,
    (LIKE, LIKE): questionable_category,
    (DISLIKE, DISLIKE): questionable_category
}

# Any pair not found on those will be considered Indifferent


# Mapping responses from user defined to constants
response_mapping = {
    like_response: LIKE,
    expect_response: EXPECT,
    neutral_response: NEUTRAL,
    tolerate_response: TOLERATE,
    dislike_response: DISLIKE
}

# Define mappings for scores
functional_score_map = {
    like_response: 4,
    expect_response: 2,
    neutral_response: 0,
    tolerate_response: -1,
    dislike_response: -2
}

dysfunctional_score_map = {
    like_response: -2,
    expect_response: -1,
    neutral_response: 0,
    tolerate_response: 2,
    dislike_response: 4
}