import pandas as pd
from scipy.stats import ttest_ind

import statsmodels.api as sm
from statsmodels.formula.api import ols


def analyze(experiment):
    # Read in the Excel file
    df = pd.read_excel('results.xlsx')

    # Define variables to filter and variables to average over
    filter_vars = {'experiment': [experiment]}

    # Filter the data
    for var, values in filter_vars.items():
        df = df.loc[df[var].isin(values)]

    print(f'Mean with small anchor: {df.loc[df["anchor"] == "small", "estimation"].mean()}')
    print(f'Mean with large anchor: {df.loc[df["anchor"] == "large", "estimation"].mean()}')

    ttest_results = ttest_ind(df.loc[df['anchor'] == 'small', 'estimation'],
                              df.loc[df['anchor'] == 'large', 'estimation'])

    print(f'Two-sided p-value: {"<0.001" if ttest_results.pvalue < 0.001 else "{:.16f}".format(ttest_results.pvalue)}')
    print(f't-statistic: {ttest_results.statistic}')
    print(f'DF: {len(df[df["anchor"] == "small"]) - 1}')


def main():
    experiments = ['relevant1', 'relevant2', 'irrelevant1', 'irrelevant2']

    for experiment in experiments:
        print(experiment)
        analyze(experiment)
        print()


if __name__ == '__main__':
    main()
