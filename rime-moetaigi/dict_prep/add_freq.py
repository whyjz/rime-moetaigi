import pandas as pd
import numpy as np
import sys
sys.path.append('source_data')
from gen_dict import numberize_tone

char_freq_file = 'char_freq_merged.txt'
dict_raw_file = 'moetaigi-raw.dict.yaml'
dict_target_file = 'moetaigi-new.dict.yaml'

df_freq = pd.read_csv(char_freq_file, sep='\t')
df_freq_updated = df_freq.copy(deep=True)
df_dict = pd.read_csv(dict_raw_file, sep='\t', header=None, names=['Name', 'Pronunciation'], skiprows=13)

for index, row in df_freq.iterrows():
    pronunc = row['Pronunciation']
    new_pronunc = numberize_tone(pronunc)
    df_freq_updated.loc[index, 'Pronunciation'] = new_pronunc
    
with open(dict_raw_file) as f, open(dict_target_file, 'w') as g:

    # Write the same headers in g
    for line in f:
        g.write(line)
        if line == '...\n':
            break

    # Dictionary
    for line in f:
        cells = line.split('\t')
        word = cells[0].rstrip()   # removing '\n'
        if len(cells) >= 2:
            entry_pronunc = cells[1].rstrip()
        else:
            entry_pronunc = None
        
        # adding frequency to single-char words
        if len(word) == 1 and word != '':
            # 1. if there's already a pronunciation in moetaigi-raw.dict.yaml...
            if entry_pronunc is not None:
                # print(entry_pronunc)
                lkup_row = df_freq_updated.loc[(df_freq_updated['Name'] == word) & (df_freq_updated['Pronunciation'] == entry_pronunc)]
                # print(lkup_row)
                if len(lkup_row) == 0:
                    g.write(line)
                elif len(lkup_row) == 1:
                    g.write(line.rstrip() + '\t' + lkup_row['New_Freq'].to_string(index=False) + '\n')
                else:
                    raise ValueError('There are some bugs - check the code!')
                    # print(lkup_row)
            # 2. if there's no pronunciation for a certain word...
            else:
                lkup_row = df_freq_updated.loc[df_freq_updated['Name'] == word]
                # print(df_freq_updated.loc[df_freq_updated['Name'] == word])
                if len(lkup_row) == 0:
                    g.write(line)
                elif len(lkup_row) == 1:
                    g.write(line.rstrip() + '\t' + lkup_row['Pronunciation'].to_string(index=False) + '\t' + lkup_row['New_Freq'].to_string(index=False) + '\n')
                else:
                    for lkup_row_index, lkup_row_each in lkup_row.iterrows():
                        g.write(line.rstrip() + '\t' + lkup_row_each['Pronunciation'] + '\t' + str(lkup_row_each['New_Freq']) + '\n')
                    # raise ValueError('There are some bugs - check the code!')
                    # print(lkup_row)
        else:
            g.write(line)
    
    # 3. if both pronunciation and frequency are provided, but the corrsponding word does not exist in moetaigi-raw.dict.yaml...
    for index, row in df_freq_updated.iterrows():
        match = df_dict[df_dict['Name'] == row['Name']]
        if len(match) == 0:
            g.write(row['Name'] + '\t' + row['Pronunciation'] + '\t' + str(row['New_Freq']) + '\n')
            # print(row['Name'])
            
    # 4. if a word has pronunciation but we can't find frequency: skip now
    # 5. if a word does not have pronunciation and frequency: skip now