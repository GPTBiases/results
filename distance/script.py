import pandas as pd
from scipy.stats import ttest_ind

import statsmodels.api as sm
from statsmodels.formula.api import ols


def analyze(experiment):
    # TODO: we are looking for monotonicity

    # Read in the Excel file
    df = pd.read_excel('results.xlsx')

    # Define variables to filter and variables to average over
    filter_vars = {'experiment': [experiment]}

    # Filter the data
    for var, values in filter_vars.items():
        df = df.loc[df[var].isin(values)]

    # Define the formula for the ANOVA
    formula = 'confidence ~ C(distance)'

    # Fit the ANOVA model
    model = ols(formula, data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)

    print(anova_table)


def main():
    experiments = ['animals_3w', 'animals_5w', 'spaced_animals_3w', 'spaced_animals_5w', 'animals_pavio', 'char_all_xy',
                   'letters', 'months', 'textual_all_xy', 'textual_hundred_xy', 'textual_ty_xy']

    for experiment in experiments:
        print(experiment)
        analyze(experiment)
        print()


if __name__ == '__main__':
    main()
