s = 'azcbobobegghakl'
bobs = 0

for l in range(len(s)):
    print(s[l] + "=" + str(ord(s[l])))
    if s[l:l+3] == ("bob"):
        bobs += 1
        
print("Number of times bob occurs is: " + str(bobs))