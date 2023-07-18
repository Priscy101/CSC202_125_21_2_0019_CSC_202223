#Day_8

#Ceasar Cipher
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w","x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
direct = input(f"type 'encode' to encrypt, type 'decode' to decrypt \n" ).lower()
tec = input("type your message \n").lower()
shift = int(input("type your shift number \n"))
#Encrypt function
#if direct == "encode"
#    encrypt (text = tec, sh_num = shift)
#elif direct == "decode":
#    decrypt(ted = tec, shif = shift)
def caesar(start_txt, sh_num, cipher_direct):
    end_txt = ""
    for letter in start_txt:
        position = alphabet.index(letter)

        if cipher_direct == "decode":
            sh_num *= -1
            new_pos = position + sh_num
            end_txt += alphabet[new_pos]
        elif cipher_direct == "encode":
            sh_num *= 1
        new_pos = position + sh_num
        end_txt += alphabet[new_pos]

print(f"The {cipher_direct} text is {end_txt}")
caesar(start_txt= tec, sh_num= shift, cipher_direct= direct)

