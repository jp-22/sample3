d1 = {}

def character_range(char1, char2):
    for char in range(ord(char1), ord(char2) + 1):
        d1[chr(char)]=ascii(char)
    print (d1)

# character_range('A','Z')
# character_range('a','z')
character_range('0','9')

