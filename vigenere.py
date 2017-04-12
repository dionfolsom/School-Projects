import sys

def main():
    type_util = sys.argv[1]
    file_input = sys.argv[2]
    file_output = sys.argv[3]
    cipher_key = sys.argv[4]
    try:
        open_file = open(file_input,'r')
    except IOError:
        print('That file does not exist')
        return
    if len(cipher_key) < 3:
        print('Encryption Key Too Short')
        return
    list_of_char = create_list()
    full_list = [] #List of all rotated cipher lists after for-loop
    for x in cipher_key:
        full_list.append(cipher_rotate(x,list_of_char))
    unedited_message = file_read(file_input)
    message = unedited_message.strip()
    count = 0 #Used to determine which rotated cipher to use
    if type_util == '-e':
        figure_out(count,file_output,message,'e',full_list,list_of_char)
    elif type_util == '-d':
        figure_out(count,file_output,message,'d',full_list,list_of_char)
    else:
        print('Please enter either -d or -e to encrypt or decrypt a file')
        main()


def create_list(): #Creates list with necessary characters
    main_list = []
    for x in range(65,91):
        main_list.append(chr(x))
    for x in range(97,123):
        main_list.append(chr(x))
    for x in range(48,58):
        main_list.append(chr(x))
    symbol_list = [' ','.',',','!','?','$','&',';',':']
    for x in symbol_list:
        main_list.append(x)
    return main_list

def translate(lists,letter,count,original_list): #Changes chars to coded chars
    number = original_list.index(letter)
    new_list = lists[count]
    return new_list[number]

def decode(lists,letter,count,original_list): #Decodes from encrypted message
    new_list = lists[count]
    number = new_list.index(letter)
    return original_list[number]

def cipher_rotate(letter,list_main): #Rotates list based on cipher
    letter_ciph = []
    start_pos = list_main.index(letter)
    letter_ciph.extend(list_main[start_pos:])
    letter_ciph.extend(list_main[:start_pos])
    return letter_ciph

def file_read(filename): #Returns Input File
    file_to_read = open(filename,'r')
    message = file_to_read.read()
    file_to_read.close()
    return message

def figure_out(count_og,file_output,message,d_or_e,full_list,list_of_char):
    #Encodes or Decodes the Message Depending on var d_or_e
    file_to_write = open(file_output,'w')
    for x in message:
        if count_og > len(full_list)-1:
            count_og = 0
        if d_or_e == 'd':
            output = decode(full_list,x,count_og,list_of_char)
            file_to_write.write(output)
        elif d_or_e == 'e':
            output = translate(full_list,x,count_og,list_of_char)
            file_to_write.write(output)
        count_og += 1
    file_to_write.close()
    file_finished = open(file_output,'r')
    text_output = file_finished.read()
    file_finished.close()
    print(text_output)
    for x in full_list:
        print(x)


if __name__ == '__main__': #Runs Program
    main()
