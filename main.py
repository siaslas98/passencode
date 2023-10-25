# Tre Huang Encoder


# This function properly encodes a password based on the rules given by assignment
def encode_password(password):
    while True:
        if len(password) != 8:
            while len(password) != 8:
                password = input('Enter an 8 digit password to be encoded: ')
        if password.isdigit():
            break
        else:
            password = input('Enter an 8 digit password to be encoded: ')
            continue

    list_digits = list(password)

    for i in range(8):
        list_digits[i] = int(list_digits[i])

    for i in range(8):
        if list_digits[i] in range(7):
            list_digits[i] = str(list_digits[i] + 3)
        elif list_digits[i] == 7:
            list_digits[i] = str(0)
        elif list_digits[i] == 8:
            list_digits[i] = str(1)
        elif list_digits[i] == 9:
            list_digits[i] = str(2)

    encoded_password = ''.join(list_digits)
    return encoded_password

# Tom's Decode Function
def decode_password(password):
    decoded_string = ""
    for digit in password:
        digit = int(digit) - 3
        if digit == -1:
            digit = 9
        elif digit == -2:
            digit = 8
        elif digit == -3:
            digit = 7
        decoded_string += str(digit)
    return decoded_string


# This function is has multiple print statements for displaying the menu
def display_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('2. Quit')
    print()


# main code block

if __name__ == "__main__":

    menu_option = ''

    encoded_password = ''

    while menu_option != '3':
        display_menu()
        menu_option = input('Please enter an option: ')

        if menu_option == '1':
            password = input('Enter an 8 digit password to be encoded: ')
            encoded_password = encode_password(password)
            print('Your password has been encoded and stored!')
            print()

        elif menu_option == '2' and (not encoded_password):
            print('You didn\'t type a password to encode yet')
            print()
            continue
        elif menu_option == '2' and (encoded_password):
            print(f'The encoded password is {encoded_password}, and the original password is {decode_password(encoded_password)}')  # Any ... is meant to be replaced
            print()
        elif menu_option == '3':
            break
















