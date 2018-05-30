def anti_vowel(text):
    vowel = list("aeiouAEIOU")
    newText = list()

    #for letter in range(len(text)):
    for letter in list(text):
        for vwl in vowel:
            if letter != vwl:
                continue
            elif letter == vwl:
                break
        else:
            newText.append(letter)
    print ("".join(newText))
    newText = "".join(newText)
    print(newText)
    print(vowel)
    return(newText)

anti_vowel("Ralph and Sam")