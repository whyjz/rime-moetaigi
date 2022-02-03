from urllib.parse import quote
from urllib.request import urlopen
from urllib.error import HTTPError
import json 
from moetaigi import numberize_tone, make_headers

def count_pronunciation(word_json):
    count = 0
    for each_explanation in word_json['h']:
        pronunciation = each_explanation['T']
        count += len(pronunciation.split('/'))
    return count

if __name__ == "__main__":
    
    words_list_url = 'https://raw.githubusercontent.com/g0v/moedict-webkit/master/t/index.json'

    with urlopen(words_list_url) as url:
        data = json.loads(url.read().decode())
        
    no_pronunc_words_list = ''
        
    with open('moetaigi-raw_fromAPI.dict.yaml', 'w') as w, open('gen_dict_fromAPI.log', 'w') as log:

        
        # Make headers in w
        make_headers(w)
    
        i = 0
        #### Testing data sets:
        # [11580:11620] 熱
        # [40:80] 諺語
        ####
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
                no_pronunc_words_list += word + '\n'
                continue

            pronun_count = count_pronunciation(word_json)

            for each_explanation in word_json['h']:
                pronunciation = each_explanation['T']
                # print(pronunciation)
                pronun_list = pronunciation.split('/')
                if pronun_count == 1:
                    pronunciation = pronunciation.replace('-', ' ')
                    pronunciation = numberize_tone(pronunciation)
                    w.write('{}\t{}\n'.format(word, pronunciation))
                else:
                    weight = 1 / pronun_count
                    for each_pronun in pronun_list:
                        each_pronun = each_pronun.replace('-', ' ')
                        each_pronun = numberize_tone(each_pronun)
                        # w.write('{}\t{}\t{:.0%}\n'.format(word, each_pronun, weight))
                        w.write('{}\t{}\n'.format(word, each_pronun))

        w.write(no_pronunc_words_list)
                
###### Test codes...
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