def space_repl(word: str) -> str:
    new_word = word.split(' ')
    mod_word = str()
    for i in new_word:
        if i:
            mod_word += i + '%20'
        continue
    if new_word[-1]:
        mod_word = mod_word[:-3]
    print(mod_word)
    return mod_word

    
word = 'Mr Join Smit   sd '
space_repl(word)
