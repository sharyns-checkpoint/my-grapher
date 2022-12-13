import sys
import pandas as pd
import numpy as np
import datetime
import os

def gen_cmd(username: str):
    return f"ssh -p 29418 sharyns@perkins.checkpoint.com gerrit query owner:{username}@checkpoint.com status:merged --format json > {username}.json"


def preprocess(input_name: str) -> pd.DataFrame:
    
    try:
        with open(input_name, encoding='utf-8') as file:
            df = None

            for line in file.read().splitlines():
                df1 = pd.read_json(line)
                df1.drop(['email', 'name'], inplace=True)
                df1.reset_index()

                if df is None:
                    df = df1
                else:
                    df = pd.concat([df, df1])

            print(f'Loaded and finished with file {input_name}')
            print('HEAD:\n')
            df.head()
            print('All done')

            df = df[['topic', 'number', 'lastUpdated']]  # filter columns
            df.reset_index()  # get rid of weird index

            # convert unix epochs
            #df['createdOn'] = df['createdOn'].astype(int).apply(datetime.datetime.fromtimestamp)
            df['lastUpdated'] = df['lastUpdated'].astype(int).apply(datetime.datetime.fromtimestamp)

            # convert to just date
            #df['createdOn'] = pd.to_datetime(df['createdOn']).dt.date
            df['lastUpdated'] = pd.to_datetime(df['lastUpdated']).dt.date

            # temp - test
            #print(df[['createdOn', 'lastUpdated']])

            return df
    except Exception as ex:
        print('Error while processing file: ' + str(ex))
        return

def fix_file(filename: str, newname) -> None:
    newlines = []

    with open(filename, 'r') as f:
        newlines = []
        lines = f.readlines()

        for line in lines:
            if line != '' and 'type' not in line:
                newlines.append(line)
            
    with open(newname, 'w') as of:
        of.writelines(newlines)

def main(username):
    cmd = gen_cmd(username)

    print('Fetching data')
    os.system(cmd)
    filename = username + '.json'

    print('Fixing file')
    newname = username + '2.json'
    fix_file(filename, newname)
    print('File ready: ' + newname)

    print('Began pre-processing')
    df = preprocess(newname)
    df.to_csv(username + '2.csv')  # obviously, temp

if __name__ == '__main__':
    username = sys.argv[1]
    main()
