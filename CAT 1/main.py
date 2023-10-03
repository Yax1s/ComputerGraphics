import json
import pandas as pd
import glob

'''Initializing an empty list to store data from data folder'''
data = []

'''File path containing for the directory all the JSONL files'''
jsonl_files = glob.glob('amazon-massive-dataset/data/*.jsonl')
df = pd.concat([pd.read_json(f) for f in jsonl_files])
df.head()



# df = pd.read_json(jsonl_files[0], lines=True)
# first = df["id"]

# print(first)


# '''Iterate over each JSONL file'''
# for jsonl_file in jsonl_files:
#     with open(jsonl_file, 'r', encoding='utf-8') as file:
#         for line in file:
#             record = json.loads(line)
#             data.append(record)

# '''Create a DataFrame from the data'''
# df = pd.DataFrame(data)

# intialise data of lists.



# '''Create an Excel writer object to save the data to an Excel file'''
# excel_writer = pd.ExcelWriter('en-xx.xlsx', engine='openpyxl')

# '''Group the data by 'locale' and iterate over each language'''
# for lang, lang_df in df.groupby('locale'):
#     '''Save the data to the Excel sheet named with the language code'''
#     lang_df[['id', 'utt', 'annot_utt']].to_excel(excel_writer, sheet_name=lang, index=False)

# '''Save the Excel file'''
# excel_writer._save()

# print('Excel file generated successfully.')
