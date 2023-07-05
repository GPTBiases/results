import pandas as pd
from scipy.stats import ttest_ind

import statsmodels.api as sm
from statsmodels.formula.api import ols


def analyze(experiment):
    # Read in the Excel file
    df = pd.read_excel('filtered.xlsx')

    # Define variables to filter and variables to average over
    filter_vars = {'experiment': [experiment]}
    avg_vars = ['congruent', 'word', 'variation']

    # Filter the data
    for var, values in filter_vars.items():
        df = df.loc[df[var].isin(values)]
    
    df = df.groupby(avg_vars).mean().reset_index()

    print(f'Mean without congruence: {df.loc[df["congruent"] == False, "confidence"].mean()}')
    print(f'Mean with congruence: {df.loc[df["congruent"] == True, "confidence"].mean()}')

    # Perform t-test on the averaged results
    ttest_results = ttest_ind(df.loc[df['congruent'] == False, 'confidence'],
                              df.loc[df['congruent'] == True, 'confidence'])

    print(f'Two-sided p-value: {"<0.001" if ttest_results.pvalue < 0.001 else "{:.16f}".format(ttest_results.pvalue)}')
    print(f't-statistic: {ttest_results.statistic}')
    print(f'DF: {len(df) - 2}')


def main():
    experiments = ['snarc', 'vertical_snarc', 'simple_snarc', 'simple_vertical_snarc', 'simple_snarc_parity',
                   'simple_vertical_snarc_parity',
                   'simple_snarc_parity_disclaimer', 'simple_vertical_snarc_parity_disclaimer',
                   'simple_snarc_parity_disclaimer_', 'simple_vertical_snarc_parity_disclaimer_']

    for experiment in experiments:
        print(experiment)
        analyze(experiment)
        print()


if __name__ == '__main__':
    main()
