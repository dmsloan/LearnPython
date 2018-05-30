def reverse(text):
  newText = list()
  for num in range(len(text)):
    newText.append(text[len(text)-num-1])
  print (newText)
  newText = (''.join(newText))
  #return(newText)

  print(newText)

  text = list(text)    #convert incomming text to a list
  for letter in text:  #create a for loop
    print(letter)      #print the letter of the loop we are in
    print(text[0])     #print the letter at index 0

reverse("Ralph and Sam")