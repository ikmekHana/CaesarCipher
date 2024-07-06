def direction_input():
    '''
    Function for requesting from the user the direction of
    programme operation (encryption or decryption)
    '''
    while True:    
        print('Enter the operating direction of the programme')
        print('Enter "1" if you want to encrypt the text')
        print('Enter "2" if you want to decrypt the text')
        answer = input()
        if answer == '1':
            return 'encryption'
        elif answer == '2':
            return 'decryption'
        else:
            print('Enter the correct value')

def language_request():
    '''
    Function for requesting from the user the language
    of the text to be converted (English or Russian)
    '''
    while True:
        print('Select the language in which the text is written')
        print('Enter "en" to select English')
        print('Enter "ru" to select Russian')
        answer = input()
        if answer != 'en' and answer != 'ru':
            print('Enter the correct value')
        else:
            return answer

def shift_step_input():
    '''
    Function for requesting a text shift step from the user
    '''
    while True:
        print('Enter the shift step - a positive integer')
        shift_step = input()
        if shift_step.isdigit() is False:
            print('Enter the correct value')
        else:
            return int(shift_step)
    
def encryption():
    '''
    Function for encrypting text
    '''
    result = ''
    for i in range(len(text)):
        letter = text[i]
        if letter in uppercase:
            letter = uppercase[(uppercase.find(letter) + shift_step) % alphabet_capacity]
        elif letter in lowercase:
            letter = lowercase[(lowercase.find(letter) + shift_step) % alphabet_capacity]
        result += letter
    return result

def decryption():
    '''
    Function for decrypting text
    '''
    result = ''
    for i in range(len(text)):
        letter = text[i]
        if letter in uppercase:
            letter = uppercase[(uppercase.find(letter) - shift_step) % alphabet_capacity]
        elif letter in lowercase:
            letter = lowercase[(lowercase.find(letter) - shift_step) % alphabet_capacity]
        result += letter
    return result
def repeat_request():
    '''
    Function for requesting the user to convert another text
    '''
    while True:
        print('Want to convert another text?')
        print('Enter "y" if yes or "n" if no')
        answer = input()
        if answer == 'y' or answer == 'Y':
            return True
        elif answer == 'n' or answer == 'N':
            return False
        else:
            print('Enter the correct value')

while True:
    direction = direction_input()
    if language_request() == 'en':
        alphabet_capacity = 26
        uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lowercase = 'abcdefghijklmnopqrstuvwxyz'
    else:
        alphabet_capacity = 33
        uppercase = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        lowercase = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    shift_step = shift_step_input()
    print('Enter the text to be converted')
    text = input()
    if direction == 'encryption':
        print(encryption())
    else:
        print(decryption())
    repeat = repeat_request()
    if repeat is True:
        continue
    else:
        break

