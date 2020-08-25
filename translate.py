import requests


def translate_en_ru(word):
    url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ru&dt=t&q={word}'
    word_lst = requests.post(url)
    translate_word = word_lst.json()
    return translate_word[0][0][0]


def translate_ru_en(word):
    url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=ru&tl=en&dt=t&q={word}'
    word_lst = requests.post(url)
    translate_word = word_lst.json()
    return translate_word[0][0][0]


print(translate_en_ru('dog'))
print(translate_ru_en('собака'))

