import pandas as pd
from scipy.stats import ttest_ind


def analyze(experiment, word_length):
    # Read in the Excel file
    df = pd.read_excel('filtered.xlsx')

    # Define variables to filter and variables to average over
    filter_vars = {'experiment': [experiment], 'word length': [word_length]}
    avg_vars = ['actual primer', 'actual word', 'primer', 'question', 'word length', 'variation']

    # Filter the data
    for var, values in filter_vars.items():
        df = df.loc[df[var].isin(values)]

    # Average the results
    df = df.groupby(avg_vars).mean().reset_index()

    print(f'Mean without priming: {df.loc[df["actual primer"] == False, "confidence"].mean()}')
    print(f'Mean with priming: {df.loc[df["actual primer"] == True, "confidence"].mean()}')

    # Perform t-test on the averaged results
    ttest_results = ttest_ind(df.loc[df['actual primer'] == False, 'confidence'],
                              df.loc[df['actual primer'] == True, 'confidence'])

    print(f'Two-sided p-value: {"<0.001" if ttest_results.pvalue < 0.001 else "{:.16f}".format(ttest_results.pvalue)}')
    print(f't-statistic: {ttest_results.statistic}')
    print(f'DF: {len(df[df["actual primer"] == False]) - 1}')


def main():
    for experiment in ['sentence', 'question', 'simple']:
        for word_length in [4, 5, 6]:
            print(f'{experiment} {word_length}')
            analyze(experiment, word_length)
            print()


if __name__ == '__main__':
    main()
