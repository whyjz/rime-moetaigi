from urllib.parse import quote
from urllib.request import urlopen
import json 

words_list_url = 'https://raw.githubusercontent.com/g0v/moedict-webkit/master/t/index.json'

with urlopen(words_list_url) as url:
    data = json.loads(url.read().decode())

with open('moetaigi.dict.yaml', 'w') as w:
    
    for word in data[4500:4520]:
        word_quote = quote(word)
        word_url = 'https://www.moedict.tw/t/' + word_quote + '.json'
        with urlopen(word_url) as url:
            word_json = json.loads(url.read().decode())
            
        pronunciation = word_json['h'][0]['T']
        pronunciation = pronunciation.replace('-', ' ')
        pronunciation = pronunciation.split('/')[0]
        w.write('{}\t{}\n'.format(word, pronunciation))


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
