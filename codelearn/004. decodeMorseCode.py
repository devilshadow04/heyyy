def decodeMorseCode(s):
    string = s.split()
    result = ''
    for i in range(len(string)):
        if string[i] == '.-':
            result += 'a'
        elif string[i] == '-...':
            result += 'b'
        elif string[i] == '-.-.':
            result += 'c'
        elif string[i] == '-..':
            result += 'd'
        elif string[i] == '.' :
            result += 'e'
        elif string[i] == '..-.':
            result += 'f'
        elif string[i] == '--.':
            result += 'g'
        elif string[i] == '....':
            result += 'h'
        elif string[i] == '..':
            result += 'i'
        elif string[i] == '.---':
            result += 'j'
        elif string[i] == '-.-':
            result += 'k'
        elif string[i] == '.-..':
            result += 'l'
        elif string[i] == '--':
            result += 'm'
        elif string[i] == '-.':
            result += 'n'
        elif string[i] == '---':
            result += 'o'
        elif string[i] == '.--.':
            result += 'p'
        elif string[i] == '--.-':
            result += 'q'
        elif string[i] == '.-.':
            result += 'r'
        elif string[i] == '...':
            result += 's'
        elif string[i] == '-':
            result += 't'
        elif string[i] == '..-':
            result += 'u'
        elif string[i] == '...-':
            result += 'v'
        elif string[i] == '.--':
            result += 'w'
        elif string[i] == '-..-':
            result += 'x'
        elif string[i] == '-.--':
            result += 'y'
        elif string[i] == '--..':
            result += 'z'
        elif string[i] == '.----':
            result += '1'
        elif string[i] == '..---':
            result += '2'
        elif string[i] == '...--':
            result += '3'
        elif string[i] == '....-':
            result += '4'
        elif string[i] == '.....':
            result += '5'
        elif string[i] == '-....':
            result += '6'
        elif string[i] == '--...':
            result += '7'
        elif string[i] == '---..':
            result += '8'
        elif string[i] == '----.':
            result += '9'
        elif string[i] == '-----':
            result += '0'
        elif string[i] == '/':
            result += ' '
    return result

n = input()
print(decodeMorseCode(n))