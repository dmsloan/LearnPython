def anti_vowel(text):
    vowel = list("aeiouAEIOU")
    newText = list()

    for num in range(len(text)):
        for vwl in vowel:
            if text[num] == vwl:
                break
        newText.append(text[num])
    print ("".join(newText))
    return("".join(newText))
    print(vowel)

anti_vowel("Ralph and Sam")