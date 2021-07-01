from urllib.parse import quote
from urllib.request import urlopen
from urllib.error import HTTPError
import json 

def count_pronunciation(word_json):
    count = 0
    for each_explanation in word_json['h']:
        pronunciation = each_explanation['T']
        count += len(pronunciation.split('/'))
    return count

def numberize_tone(pronunciation):
    d_fin = []
    pronunciation = pronunciation.replace('.', '')
    pronunciation = pronunciation.replace(',', '')
    pronunciation = pronunciation.replace('?', '')
    pronunciation = pronunciation.replace(';', '')
    pronunciation = pronunciation.lower()
    for c in pronunciation.split():
        if 'a̍' in c:
            d = c.replace('a̍', 'a') + '8'
        elif 'e̍' in c:
            d = c.replace('e̍', 'e') + '8'
        elif 'i̍' in c:
            d = c.replace('i̍', 'i') + '8'
        elif 'o̍' in c:
            d = c.replace('o̍', 'o') + '8'
        elif 'u̍' in c:
            d = c.replace('u̍', 'u') + '8'
        # elif 'n8' in c: non-existent
        # elif 'm8' in c: non-existent
        elif 'ā' in c:
            d = c.replace('ā', 'a') + '7'
        elif 'ē' in c:
            d = c.replace('ē', 'e') + '7'
        elif 'ī' in c:
            d = c.replace('ī', 'i') + '7'
        elif 'ō' in c:
            d = c.replace('ō', 'o') + '7'
        elif 'ū' in c:
            d = c.replace('ū', 'u') + '7'
        elif 'n̄' in c:
            d = c.replace('n̄', 'n') + '7'
        elif 'm̄' in c:
            d = c.replace('m̄', 'm') + '7'
        elif 'â' in c:
            d = c.replace('â', 'a') + '5'
        elif 'ê' in c:
            d = c.replace('ê', 'e') + '5'
        elif 'î' in c:
            d = c.replace('î', 'i') + '5'
        elif 'ô' in c:
            d = c.replace('ô', 'o') + '5'
        elif 'û' in c:
            d = c.replace('û', 'u') + '5'
        elif 'n̂' in c:
            d = c.replace('n̂', 'n') + '5'
        elif 'm̂' in c:
            d = c.replace('m̂', 'm') + '5'
        elif 'à' in c:
            d = c.replace('à', 'a') + '3'
        elif 'è' in c:
            d = c.replace('è', 'e') + '3'
        elif 'ì' in c:
            d = c.replace('ì', 'i') + '3'
        elif 'ò' in c:
            d = c.replace('ò', 'o') + '3'
        elif 'ù' in c:
            d = c.replace('ù', 'u') + '3'
        elif 'ǹ' in c:
            d = c.replace('ǹ', 'n') + '3'
        # elif 'm3' in c: non-existent
        elif 'á' in c:
            d = c.replace('á', 'a') + '2'
        elif 'é' in c:
            d = c.replace('é', 'e') + '2'
        elif 'í' in c:
            d = c.replace('í', 'i') + '2'
        elif 'ó' in c:
            d = c.replace('ó', 'o') + '2'
        elif 'ú' in c:
            d = c.replace('ú', 'u') + '2'
        elif 'ń' in c:
            d = c.replace('ń', 'n') + '2'
        elif 'ḿ' in c:
            d = c.replace('ḿ', 'm') + '2'
        elif c.endswith('p') or c.endswith('t') or c.endswith('k') or c.endswith('h'):
            d = c + '4'
        else:
            d = c + '1'
        d_fin.append(d)
    final_pronun = ' '.join(d_fin)
    return final_pronun

words_list_url = 'https://raw.githubusercontent.com/g0v/moedict-webkit/master/t/index.json'

with urlopen(words_list_url) as url:
    data = json.loads(url.read().decode())
        

with open('moetaigi-autogen.dict.yaml', 'w') as w:
    
    i = 0
    log = open('moetaigi-autogen.log', 'w')
    # [11580:11620] 熱
    # [40:80] 諺語
    for word in data:
        i += 1
        word_quote = quote(word)
        word_url = 'https://www.moedict.tw/t/' + word_quote + '.json'
        
        try: 
            with urlopen(word_url) as url:
                word_json = json.loads(url.read().decode())
        except HTTPError:
            txt = '==== 警告 ==== 揣無 "' + word + '" 的發音！ ({})'.format(i)
            print(txt)
            log.write(txt + '\n')
            continue
        
        pronun_count = count_pronunciation(word_json)
        
        for each_explanation in word_json['h']:
            pronunciation = each_explanation['T']
            # print(pronunciation)
            pronun_list = pronunciation.split('/')
            if pronun_count == 1:
                pronunciation = pronunciation.replace('-', ' ')
                # w.write('{}\t{}\n'.format(word, pronunciation))
                pronunciation = numberize_tone(pronunciation)
                w.write('{}\t{}\n'.format(word, pronunciation))
            else:
                weight = 1 / pronun_count
                for each_pronun in pronun_list:
                    each_pronun = each_pronun.replace('-', ' ')
                    # w.write('{}\t{}\t{:.0%}\n'.format(word, each_pronun, weight))
                    each_pronun = numberize_tone(each_pronun)
                    w.write('{}\t{}\t{:.0%}\n'.format(word, each_pronun, weight))
                    
    log.close()
                
                
                

                
                
#         pronunciation = pronunciation.replace('-', ' ')
#         pronunciation = pronunciation.split('/')[0]
#         w.write('{}\t{}\n'.format(word, pronunciation))


# word = '夭壽'
# word_n = quote(word)

# words_list_url = 'https://www.moedict.tw/t/' + word_n + '.json'
# print(words_list_url)

# with open('tmp.moetaigi.yaml', 'w') as w:
#     with urlopen(words_list_url) as url:
#         data = json.loads(url.read().decode())
#         pron = data['h'][0]['T']
#     w.write('{}\t{}'.format(word, pron))





# print(data[:10])
