with open('../moetaigi.dict.yaml') as f, open('../moetaigi.unspaced.dict.yaml', 'w') as g:

    # Make headers in g
    g.write('# Rime dictionary\n')
    g.write('# encoding: utf-8\n')
    g.write('#\n')
    g.write('# 不含空格的萌典 API 台語詞條，自動產生，供注音反查之用。\n')
    g.write('\n')
    g.write('---\n')
    g.write('name: moetaigi.unspaced\n')
    g.write('version: "0.1"\n')
    g.write('sort: by_weight\n')
    g.write('use_preset_vocabulary: false\n')
    g.write('...\n')
    
    # Skip headers in f
    for line in f:
        if line == '...\n':
            break

    # Dictionary
    for line in f:
        g.write(line.replace(' ', "'"))