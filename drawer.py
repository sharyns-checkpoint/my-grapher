import sys
import pandas as pd
import matplotlib.pyplot as plt


username = sys.argv[1]
filename = username + '.csv' 

df = pd.read_csv(filename)
x = df['date']
y = df['num']

plt.plot(df['date'], df['num'])
plt.title('merged commits by ' + username)
plt.xticks(x[::5], rotation='vertical')
plt.xlabel('Day')
plt.ylabel('# of commits')
plt.show()
