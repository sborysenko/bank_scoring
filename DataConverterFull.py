import os
import pandas as pd

extended = True


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.rstrip('\n') for line in file]
    return lines


def val(value):
    return str(value).strip().replace(' ', '').replace('%', '').replace('-', '0').replace(',', '.')


def getIndex(value):
    if value == '-':
        return 0.0
    index = value.index("/")
    substring = value[index + 1:]
    return substring.replace(',', '.')


def process_file(file_name):
    df = pd.DataFrame()

    lines = read_file(file_name)
    index = 2;

    index_col = [getIndex(lines[index + 1]), getIndex(lines[index + 2]), getIndex(lines[index + 3]), getIndex(lines[index + 4]), getIndex(lines[index + 5])]
    df['Індекс'] = index_col
    index = index + 6

    if not extended:
        index = 93

    while index < len(lines):
        if not extended and index == 178:
            break
        if index == 8 or index == 93 or index == 178:
            index = index + 1

        name = str(lines[index]).strip()
        index = index + 1

        col = [val(lines[index + 1]), val(lines[index + 2]), val(lines[index + 3]), val(lines[index + 4]), val(lines[index + 5])]
        df[name] = col
        index = index + 6

    # df.to_csv(file_name + ".csv", index=False)
    return df


folder_path = 'data/extended'
files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

frames = []
for file in files:
    print("Processing file : " + file)
    file_path = os.path.join(folder_path, file)
    frames.append(process_file(file_path))

df = pd.concat(frames, ignore_index=True)
print(df)

df.to_csv("dataframe.csv", index=False)

