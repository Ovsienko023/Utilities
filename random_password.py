import random
import string


def get_rand_password():
    letters = string.ascii_lowercase # прописные
    letters = string.ascii_letters # Заглавные и прописные
    numb = string.digits # цифры от 0 до 9
    letters += numb

    fin_str = ''
    for _ in range(15):
        fin_str += random.choice(letters)
        
    print(fin_str)


get_rand_password()
