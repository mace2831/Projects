#Created by Aaron Maciag 8/5/2024

def converter():
    user_in = ''
    converted=''
    morse_code = {'a': '* --', 'b': '-- * * *', 'c': '-- * -- *', 'd': '-- * *', 'e': '*', 'f':'* * -- *',
                 'g':'-- -- *','h':'* * * *', 'i':'* *', 'j':'* -- -- --', 'k':'-- * --', 'l':'* -- * *',
                 'm':'-- --', 'n':'-- *', 'o':'-- -- --','p':'* -- -- *','q':'-- -- * --', 'r':'* -- *',
                 's':'* * *','t':'--','u':'* * --','v':'* * * --','w':'* -- --','x':'-- * * --','y':'-- * -- --',
                 'z':'-- -- * *'}

    while user_in.lower() != 'n':
        user_in = input('Enter the string you would like to convert to Morse Code:\n')

        for letter in user_in:
            if letter == ' ':
                converted += '  '
            else:
                converted += morse_code[letter.lower()]
                converted += '  '

        print('Your sentence in Morse Code is: ', converted)
        user_in = input('Would you like to enter another sentence? (y/n)')




if __name__ == '__main__':
    converter()