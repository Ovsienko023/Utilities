import requests


def translate(word):
    url = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=ru&dt=t&q={word}'
    word_lst = requests.post(url)
    translate_word = word_lst.json()
    return translate_word[0][0][0]

translate('dog')