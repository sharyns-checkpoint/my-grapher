import sys
import pandas as pd

input_name = sys.argv[1]
output_name = sys.argv[2]

# check args
if input_name == "" or input_name.isspace():
    print("Missing first arg: input filename")
    exit
elif input_name == "" or input_name.isspace():
    print("Missing second arg: output filename")
    exit

# process
with open(input_name, encoding='utf-8') as file:
    df = pd.read_json(file)
    print(f'Loaded and finished with file {input_name}')

df.to_csv(output_name, encoding='utf-8', index=False)
