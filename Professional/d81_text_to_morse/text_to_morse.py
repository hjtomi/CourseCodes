print('''MORSE - TEXT
TEXT - MORSE
 CONVERTER
 
Sample Text Input:   I love you
Sample Morse Input:   .. | .-.. --- ...- . | -.-- --- ..-   ### Each letter seperated by a space and each word seperated by a '|'
''')


TEXT_TO_MORSE = {'A': '.-', 'B': '-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                 '7':'--...', '8':'---..', '9':'----.',
                 '0':'-----', ',':'--..--', '.':'.-.-.-',
                 '?':'..--..', '/':'-..-.', '-':'-....-',
                 '(':'-.--.', ')':'-.--.-'}

MORSE_TO_TEXT = {value: key for key, value in TEXT_TO_MORSE.items()}


def encrypt():
    error = False
    morse = ''
    text = input('Enter a text: ').strip()

    for letter in text:
        letter = letter.upper()

        if letter in TEXT_TO_MORSE.keys():
            morse += TEXT_TO_MORSE[letter] + ' '
        elif letter == ' ':
            morse += ' | '
        else:
            print('bad input (one or more letter not in the morse code)')
            error = True
            break

    if not error:
        print(morse)


def decrypt():
    error = False
    text = ''
    codes = input("Enter a morse code: ").strip().split()

    for code in codes:
        if code in MORSE_TO_TEXT.keys():
            text += MORSE_TO_TEXT[code]
        elif code == '|':
            text += ' '
        else:
            print('bad input')
            error = True
            break

    if not error:
        print(text)


while True:
    choice = input('Encrypt or Decrypt? (e/d) ')

    if choice == 'e':
        encrypt()

    elif choice == 'd':
        decrypt()

    else:
        print('bad input')
