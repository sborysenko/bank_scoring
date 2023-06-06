import os
import pandas as pd


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.rstrip('\n') for line in file]
    return lines


def val(value):
    return str(value).strip().replace('%', '').replace('-', '').replace(',', '.')


def getIndex(value):
    index = value.index("/")
    substring = value[index + 1:]
    return substring.replace(',', '.')


def process_file(file_name):
    lines = read_file(file_name)
    columns = [val(lines[1]),
               val(lines[7]),
               val(lines[13]),
               val(lines[19]),
               val(lines[25]),
               val(lines[31]),
               val(lines[37]),
               val(lines[43]),
               val(lines[49]),
               val(lines[55]),
               val(lines[61]),
               val(lines[67]),
               val(lines[73])]

    all_frames = []

    all_frames.append(pd.DataFrame([[getIndex(lines[2]), val(lines[8]),  val(lines[14]), val(lines[20]), val(lines[26]), val(lines[32]), val(lines[38]), val(lines[44]), val(lines[50]), val(lines[56]), val(lines[62]), val(lines[68]), val(lines[74])]], columns=columns))
    all_frames.append(pd.DataFrame([[getIndex(lines[3]), val(lines[9]),  val(lines[15]), val(lines[21]), val(lines[27]), val(lines[33]), val(lines[39]), val(lines[45]), val(lines[51]), val(lines[57]), val(lines[63]), val(lines[69]), val(lines[75])]], columns=columns))
    all_frames.append(pd.DataFrame([[getIndex(lines[4]), val(lines[10]), val(lines[16]), val(lines[22]), val(lines[28]), val(lines[34]), val(lines[40]), val(lines[46]), val(lines[52]), val(lines[58]), val(lines[64]), val(lines[70]), val(lines[76])]], columns=columns))
    all_frames.append(pd.DataFrame([[getIndex(lines[5]), val(lines[11]), val(lines[17]), val(lines[23]), val(lines[29]), val(lines[35]), val(lines[41]), val(lines[47]), val(lines[53]), val(lines[59]), val(lines[65]), val(lines[71]), val(lines[77])]], columns=columns))
    all_frames.append(pd.DataFrame([[getIndex(lines[6]), val(lines[12]), val(lines[18]), val(lines[24]), val(lines[30]), val(lines[36]), val(lines[42]), val(lines[48]), val(lines[54]), val(lines[60]), val(lines[66]), val(lines[72]), val(lines[78])]], columns=columns))

    df = pd.concat(all_frames, ignore_index=True)
    return df


folder_path = 'data/raw'
files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

frames = []
for file in files:
    print("Processing file : " + file)
    file_path = os.path.join(folder_path, file)
    frames.append(process_file(file_path))

df = pd.concat(frames, ignore_index=True)
print(df)

df.to_csv("dataframe.csv", index=False)

