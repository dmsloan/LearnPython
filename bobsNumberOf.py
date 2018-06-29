s = 'azcbobobegghakl'
bobs = 0

for l in range((len(s)-2)):
    print(s[l:l+3])
    if s[l:l+3] == ("bob"):
        bobs += 1
        
print("Number of times bob occurs is: " + str(bobs))