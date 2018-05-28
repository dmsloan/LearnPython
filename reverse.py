def reverse(text):
  newText = list()
  for num in range(len(text)):
    print(text[len(text)-num-1])
    newText.append(text[len(text)-num-1])
    print ("".join(newText))
  return("".join(newText))

reverse("Ralph and Sam")