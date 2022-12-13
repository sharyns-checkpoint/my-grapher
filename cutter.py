import sys
import pandas as pd
import matplotlib.pyplot as plt

def run(username):
    rawname = username + '2.csv'
    outname = username + '.csv'

    df = pd.read_csv(rawname)
    odf = df[['lastUpdated', 'number']].groupby('lastUpdated')['lastUpdated'].count()
    odf.to_csv(outname)

if __name__ == '__main__':
    username = sys.argv[1]
    run(username)

