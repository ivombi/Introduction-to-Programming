import sys
sentence = sys.argv[1]

alphabet_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
                 "p","q","r","r","s","t","u","v","w","q","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M",
                 "0","P","Q","R","S","T","U","V","W","X","Y","Z"]

def check_isogram(sentence):
    word = ''
    for letter in sentence:
        if letter in alphabet_list:
            if letter not in word:
                word += letter
            else:
                return False
        elif letter not in alphabet_list:
            word = ''
    return True
print(check_isogram(sentence))



