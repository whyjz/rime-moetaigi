import pandas as pd
import numpy as np

char_freq_base_file = 'source_data/char_freq_source2_processed.txt'
char_freq_secondary_file = 'source_data/char_freq_source1_processed.txt'

df_base1 = pd.read_csv(char_freq_base_file, sep='\t')
df_base2 = pd.read_csv(char_freq_secondary_file, sep='\t')
df_merged = df_base1.copy(deep=True)

for index, row in df_base1.iterrows():
    # 1: make all the letters lower cased
    df_merged.loc[index, 'Pronunciation'] = row['Pronunciation'].lower()
    if '/' in row['Pronunciation']:
        # 2: split alternative pronunciations (up to two pronunciations)
        tmp = row['Pronunciation'].split('/')
        df_merged.loc[index, 'Pronunciation'] = tmp[0].lower()
        row_new = row.copy(deep=True)
        row_new['Pronunciation'] = tmp[1].lower()
        df_merged.loc[len(df_merged.index)] = row_new        
        

# merging base2 with base1
for index, row in df_base2.iterrows():
    if '(' in row['Name']:
        target_char = row['Name'].split(' ')[0]
        target_pronunc = row['Name'][row['Name'].find("(")+1:row['Name'].find(")")]
    else:
        target_char = row['Name']
        target_pronunc = None
    char_pronunciations = df_merged.loc[df_merged['Name'] == target_char]
    if target_pronunc is None:
        pronunciation_distribution = char_pronunciations['New_Freq'].to_numpy()
        pronunciation_ratio = pronunciation_distribution / pronunciation_distribution.sum()
        new_distri = row['New_Freq'] * pronunciation_ratio + pronunciation_distribution
        new_distri = new_distri.astype(np.int64)
        df_merged.loc[df_merged['Name'] == target_char, 'New_Freq'] = new_distri
    else:
        target_row = char_pronunciations.loc[char_pronunciations['Pronunciation'] == target_pronunc]
        df_merged.loc[target_row.index[0], 'New_Freq'] += row['New_Freq']

df_merged_final = df_merged.sort_values(by=['New_Freq'], ascending=False)
df_merged_final.to_csv('char_freq_merged.txt', sep='\t', index=False)