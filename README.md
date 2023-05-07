# gpt3-effects-results

The repository contains the results, including raw data of our experiments with GPT-3 [see paper], in addition to python scripts used to analyzed the statistical significance of the results.

## Directories
Each directory corresponds to one effect we tested, and its subdirectories are the raw data of the experiments done on this effect.
In addition, every directory contains "results.xlsx", which is an excel file with the data of all the experiments. However, this excel doesn't contain all the information about the experiments, but only what was relevant for the statistical tests.
For experiments with some filtering before the analysis of the results [see paper] additional file, "filtered.xlsx", is included.
Each directory also constains "script.py", a python script used to analyzed the statistical significance of the results, using ANOVA for the distance effect and T-Test for the rest of the experiments.

## Subdirectories
Subdirectories contain the following files:
* answers.txt - dictionaries that map the possible completions to the probability assigned to them by GPT-3.
* text.txt - the prompts to GPT, seperated by '\n\n'
