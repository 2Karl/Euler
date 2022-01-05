def morse_encode(in_string):
    table = {"A": ".- ",
             "B": "-... ",
             "C": "-.-. ",
             "D": "-.. ",
             "E": ". ",
             "F": "..-. ",
             "G": "--. ",
             "H": ".... ",
             "I": ".. ",
             "J": ".--- ",
             "K": "-.-. ",
             "L": ".-.. ",
             "M": "-- ",
             "N": "-. ",
             "O": "--- ",
             "P": ".--. ",
             "Q": "--.- ",
             "R": ".-. ",
             "S": "... ",
             "T": "- ",
             "U": "..- ",
             "V": "...- ",
             "W": ".-- ",
             "X": "-..- ",
             "Y": "-.-- ",
             "Z": "--.. ",
             "1": ".---- ",
             "2": "..--- ",
             "3": "...-- ",
             "4": "....- ",
             "5": "..... ",
             "6": "-.... ",
             "7": "--... ",
             "8": "---.. ",
             "9": "----. ",
             "0": "----- "}
    return in_string.upper().translate(in_string.maketrans(table))


print(morse_encode("Some text"))
MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }


def morse_decoder(code):
    return " ".join("".join(MORSE[x] for x in y.split()) for y in code.split("   ")).capitalize()


# print(morse_decoder("... --- -- .   - . -..- -"))
# morse_decoder("..--- ----- .---- ---..") == "2018"
# morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"

MORSE_TREE = {
    "START": {".": "E", "-": "T"}, "E": {".": "I", "-": "A"},
    "I": {".": "S", "-": "U"}, "S": {".": "H", "-": "V"},
    "H": {".": "5", "-": "4"}, "V": {".": "Ŝ", "-": "3"},
    "U": {".": "F", "-": "Ü"}, "F": {".": "É"},
    "Ü": {".": "Ð", "-": "2"}, "Ð": {".": "?", "-": "_"},
    "A": {".": "R", "-": "W"}, "R": {".": "L", "-": "Ä"},
    "L": {"-": "È"}, "È": {".": "\""},
    "Ä": {".": "+"}, "+": {"-": "."},
    "W": {".": "P", "-": "J"}, "P": {".": "Þ", "-": "À"},
    "À": {".": "@"}, "J": {".": "Ĵ", "-": "1"},
    "1": {".": "'"}, "T": {".": "N", "-": "M"},
    "N": {".": "D", "-": "K"}, "D": {".": "B", "-": "X"},
    "B": {".": "6", "-": "="}, "6": {"-": "-"},
    "X": {".": "/", }, "K": {".": "C", "-": "Y"},
    "C": {".": "Ç", "-": None}, None: {".": ";", "-": "!"},
    "Y": {".": "Ĥ"}, "M": {".": "G", "-": "O"},
    "G": {".": "Z", "-": "Q"}, "Z": {".": "7"},
    "Q": {".": "Ĝ", "-": "Ñ"}, "O": {".": "Ö", "-": "CH"},
    "Ö": {".": "8"}, "8": {"-": ":"},
    "CH": {".": "9", "-": "0"},
}


def morse_decoder(code):
    words = code.split("   ")  # split the code into words
    message = []
    for word in words:  # loop through each word
        message.append("")
        for letter in word.split():  # loop through each letter in the word - this will comprise dots and dashes
            node = "START"  # the START node is the starting point in the MORSE TREE
            for char in letter:  # check each individual dot and dash in the letter
                node = MORSE_TREE[node][char]  # if it's a dot, we take the left path, dash we take the right
            # Once we've traversed the tree and run out of dots and dashes, we note the
            # node we got up to - in theory this will also allow the addition of extra characters to the set
            message[-1] += node
    # join the words with spaces and make the first letter in the string a capital before sending it back
    return " ".join(message).strip().capitalize()


print(morse_decoder("----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.   .- .-. .   -.. .. --. .. - ..."))
