import pandas as pd
from moetaigi import numberize_tone, make_headers

full_list = pd.read_csv('source_data/詞目總檔.csv')

with open('moetaigi-raw.yaml', 'w') as f:
    make_headers(f)
    
    for idx, row in full_list.iterrows():
        
        if row['屬性'] == 12:    # 屬性 12 是外來語，暫時先不處理
            pass
        word = row['詞目']
        if type(row['音讀']) is str:
            prns = row['音讀'].split('/')
        else:    # 無發音的詞語
            prns = ['']
        for prn in prns:
            prn = prn.replace('--', ' ')
            prn = prn.replace('-', ' ')
            prn = numberize_tone(prn)
            f.write('{}\t{}\n'.format(word, prn))
