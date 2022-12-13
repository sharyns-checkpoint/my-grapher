import sys
import pandas as pd
import matplotlib.pyplot as plt

def run(username):
    filename = username + '.csv' 

    df = pd.read_csv(filename)
    x = df['date']
    y = df['num']

    plt.figure(figsize=(12, 8))
    plt.plot(df['date'], df['num'])
    plt.title('merged commits by ' + username, pad=20)
    plt.xticks(x[::5], rotation='vertical')
    plt.xlabel('day', labelpad=30)
    plt.ylabel('# of commits', labelpad=25)
    #plt.savefig(username + '.pdf', format='pdf')
    plt.tight_layout()
    plt.subplots_adjust(left=0.076, bottom=0.2, right=0.95, top=0.92)
    plt.show()

if __name__ == '__main__':
    username = sys.argv[1]
    run(username)

