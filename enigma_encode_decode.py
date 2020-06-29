import pickle

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'

File = open('./enigma_state.enigma', 'rb')
rotor1, rotor2, rotor3 = pickle.load(File)
File.close()

def reflector(character):
    return alphabet[len(alphabet) - alphabet.find(character) - 1]

def encoder(character):
    c1 = rotor1[alphabet.find(character)]
    c2 = rotor2[alphabet.find(c1)]
    c3 = rotor3[alphabet.find(c2)]
    reflected = reflector(c3)
    c3 = alphabet[rotor3.find(reflected)]
    c2 = alphabet[rotor2.find(c3)]
    c1 = alphabet[rotor1.find(c2)]
    return c1

def rotate_rotors():
    global rotor1, rotor2, rotor3
    rotor1 = rotor1[1:] + rotor1[0]
    if count % 26 == 0:
        rotor2 = rotor2[1:] + rotor2[0]
    if count % (26*26) == 0:
        rotor3 = rotor3[1:] + rotor3[0]

plain = input('--> ')
cipher = ''
count = 0

for i in plain:
    cipher += encoder(i)
    count += 1
    rotate_rotors()

print(cipher)
