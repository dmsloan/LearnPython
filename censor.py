def censor(text, word):
    print(text.replace(word, "*" * (len(word))))
    return(text.replace(word, "*" * (len(word))))


censor("this hack is wack hack", "hack")