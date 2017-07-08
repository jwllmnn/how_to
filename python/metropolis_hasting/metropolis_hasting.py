import numpy as np
import pandas as pd
import random
import numpy as np
import pylab as pl
import scipy.special as ss

pl.rcParams['figure.figsize'] = (17.0, 4.0)

def import_clean_data():
    """
    Method imports dataframe, selects relevant variables, and drops observations with missing values.
    :return:
    """
    df_full = pd.read_csv("/Users/johanneswillmann/Documents/UNI/MSc0_Hiwi/how_to/python/metropolis_hasting/Bayes_Student_Survey.csv")

    # Subset protest variables.
    df = df_full.filter(like="protest")

    # Exclude observations with one or more missing values.
    return df.dropna()


df = import_clean_data()


def metropolis_hastings(iterations, initial_value, proposal_sd):

    for i in range(iterations):

        # Draw candidate from proposal.
        candidate = np.random.normal(loc=initial_value, scale=proposal_sd)

        # Calculate alpha.




def irt_model(df):
    Y = df.as_matrix()
    N = len(Y)
    J = len(Y[1])

    x = np.array
    beta = np.array
    # PRIORS:
    for i in range(N):
        x[i] = np.random.normal(0, 0.1)

    for j in range(J):
        beta[j] = np.random.normal(0, 0.01)

    # Loop over respondents.
    for i in range(N):
        # Loop over items.
        for j in range(J):
            candidate = np.random.binomial(1, )


Y = df.as_matrix()
N = len(Y)
J = len(Y[1])

x = np.array(N)
x[0]
beta = np.array
# PRIORS:
for i in range(N):
    x[0]

for j in range(J):
    beta[j] = np.random.normal(0, 0.01)