fruit = "banana"
for c in fruit:
    print(c)

prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    if p =="Q" or p =="O":
        print(p + "u" + suffix)
    else:
        print(p + suffix)

s = "Pirates of the caribbean"
print(s[0:7])

friends = ["Joe","Zoe","Brad","Angelina","Zuki","Thandi","Paris"]
print(friends[4:])

print(s[:])

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    s_sans_vowels = ""
    for x in s:
        if x not in vowels:
            s_sans_vowels += x
    return s_sans_vowels
remove_vowels("aABEeflijOopUus")

def find2(s,ch,start):
    x = start
    while x <len(s):
        if s[x] == ch:
            return x
        x += 1
    return -1
find2("banana","a",2)

ss = "Well I never did said Alice"
wds = ss.split()
print(wds)

