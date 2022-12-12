import sys
import pandas as pd

def process(input_name: str, output_name: str):
    
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
    except Exception as ex:
        print('Error while processing file: ' + str(ex))
        return

    df = df[['topic', 'number', 'createdOn', 'lastUpdated']]  # filter columns
    df.to_csv(output_name, encoding='utf-8', index=False)


def main():
    input_name = sys.argv[1]
    output_name = sys.argv[2]

    # check args
    if input_name == "" or input_name.isspace():
        print("Missing first arg: input filename")
        exit
    elif input_name == "" or input_name.isspace():
        print("Missing second arg: output filename")
        exit

    process(input_name, output_name)

if __name__ == '__main__':
    main()
