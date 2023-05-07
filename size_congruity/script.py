import pandas as pd
from scipy.stats import ttest_ind


def analyze(experiment):
    # Read in the Excel file
    df = pd.read_excel('filtered.xlsx')

    # Define variables to filter and variables to average over
    filter_vars = {'experiment': [experiment]}

    # Filter the data
    for var, values in filter_vars.items():
        df = df.loc[df[var].isin(values)]

    print(f'Mean without congruence: {df.loc[df["congruent"] == False, "confidence"].mean()}')
    print(f'Mean with congruence: {df.loc[df["congruent"] == True, "confidence"].mean()}')

    # Perform t-test on the averaged results
    ttest_results = ttest_ind(df.loc[df['congruent'] == False, 'confidence'],
                              df.loc[df['congruent'] == True, 'confidence'])

    print(f'Two-sided p-value: {"<0.001" if ttest_results.pvalue < 0.001 else "{:.16f}".format(ttest_results.pvalue)}')
    print(f't-statistic: {ttest_results.statistic}')
    print(f'DF: {len(df[df["congruent"] == False]) - 1}')


def main():
    experiments = ['animals_3w', 'animals_3w_spaces', 'animals_4w', 'animals_4w_spaces', 'animals_5w', 'animals_5w_spaces',
                   'animals_pavio', 'textual_all_cap_xy', 'textual_all_cap_xy_smaller_larger']

    for experiment in experiments:
        print(experiment)
        analyze(experiment)
        print()


if __name__ == '__main__':
    main()
