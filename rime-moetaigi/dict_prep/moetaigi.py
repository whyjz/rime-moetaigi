def make_headers(f):
    f.write('# Rime dictionary\n')
    f.write('# encoding: utf-8\n')
    f.write('#\n')
    f.write('# 依據萌典 API 自動產生。如欲新增詞彙請至 moetaigi.extended.dict.yaml。\n')
    f.write('\n')
    f.write('---\n')
    f.write('name: moetaigi\n')
    f.write('version: "0.3"\n')
    f.write('sort: by_weight\n')
    f.write('use_preset_vocabulary: false\n')
    f.write('import_tables:\n')
    f.write('  - moetaigi.extended\n')
    f.write('...\n')

def numberize_tone(pronunciation):
    d_fin = []
    pronunciation = pronunciation.replace('.', '')
    pronunciation = pronunciation.replace(',', '')
    pronunciation = pronunciation.replace('?', '')
    pronunciation = pronunciation.replace(';', '')
    pronunciation = pronunciation.lower()
    for c in pronunciation.split():
        if b'\xcc\x8d'.decode() in c:
            d = c.replace(b'\xcc\x8d'.decode(), '') + '8'
        ## all are already included (as b'x\xcc\x8d')
        # elif 'a̍' in c:
        #     d = c.replace('a̍', 'a') + '8'
        # elif 'e̍' in c:
        #     d = c.replace('e̍', 'e') + '8'
        # elif 'i̍' in c:
        #     d = c.replace('i̍', 'i') + '8'
        # elif 'o̍' in c:
        #     d = c.replace('o̍', 'o') + '8'
        # elif 'u̍' in c:
        #     d = c.replace('u̍', 'u') + '8'
        # elif 'n8' in c: non-existent
        # elif 'm8' in c: non-existent
        elif b'\xcc\x84'.decode() in c:
            d = c.replace(b'\xcc\x84'.decode(), '') + '7'
        elif 'ā' in c:
            d = c.replace('ā', 'a') + '7'
        elif 'ē' in c:
            d = c.replace('ē', 'e') + '7'
        elif 'ī' in c:
            d = c.replace('ī', 'i') + '7'
        elif 'ō' in c:
            d = c.replace('ō', 'o') + '7'
        elif 'ū' in c:
            d = c.replace('ū', 'u') + '7'
        ## 'n̄' and 'm̄' are already included (as b'n\xcc\x84' and b'm\xcc\x84')
        # elif 'n̄' in c:
        #     d = c.replace('n̄', 'n') + '7'
        # elif 'm̄' in c:
        #     d = c.replace('m̄', 'm') + '7'
        elif b'\xcc\x82'.decode() in c:
            d = c.replace(b'\xcc\x82'.decode(), '') + '5'
        elif 'â' in c:
            d = c.replace('â', 'a') + '5'
        elif 'ê' in c:
            d = c.replace('ê', 'e') + '5'
        elif 'î' in c:
            d = c.replace('î', 'i') + '5'
        elif 'ô' in c:
            d = c.replace('ô', 'o') + '5'
        elif 'û' in c:
            d = c.replace('û', 'u') + '5'
        ## 'n̂' and 'm̂' are already included (as b'n\xcc\x82' and b'm\xcc\x82')
        # elif 'n̂' in c:
        #     d = c.replace('n̂', 'n') + '5'
        # elif 'm̂' in c:
        #     d = c.replace('m̂', 'm') + '5'
        elif b'\xcc\x80'.decode() in c:
            d = c.replace(b'\xcc\x80'.decode(), '') + '3'
        elif 'à' in c:
            d = c.replace('à', 'a') + '3'
        elif 'è' in c:
            d = c.replace('è', 'e') + '3'
        elif 'ì' in c:
            d = c.replace('ì', 'i') + '3'
        elif 'ò' in c:
            d = c.replace('ò', 'o') + '3'
        elif 'ù' in c:
            d = c.replace('ù', 'u') + '3'
        elif 'ǹ' in c:
            d = c.replace('ǹ', 'n') + '3'
        # elif 'm3' in c: non-existent
        elif b'\xcc\x81'.decode() in c:
            d = c.replace(b'\xcc\x81'.decode(), '') + '2'
        elif 'á' in c:
            d = c.replace('á', 'a') + '2'
        elif 'é' in c:
            d = c.replace('é', 'e') + '2'
        elif 'í' in c:
            d = c.replace('í', 'i') + '2'
        elif 'ó' in c:
            d = c.replace('ó', 'o') + '2'
        elif 'ú' in c:
            d = c.replace('ú', 'u') + '2'
        elif 'ń' in c:
            d = c.replace('ń', 'n') + '2'
        elif 'ḿ' in c:
            d = c.replace('ḿ', 'm') + '2'
        elif c.endswith('p') or c.endswith('t') or c.endswith('k') or c.endswith('h'):
            d = c + '4'
        else:
            d = c + '1'
        d_fin.append(d)
    final_pronun = ' '.join(d_fin)
    return final_pronun