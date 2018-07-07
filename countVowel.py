s = 'azcbobobegghakl'
vowels = 0

for l in range(len(s)):
    if s[l] in ("aeiou"):
        vowels += 1
        
print("Number of vowels: " + str(vowels))