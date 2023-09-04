import random
# Define Morse code dictionaries
morse_code_dict_1 = {
    '.-': 'A',   '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K',  '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U',  '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', 
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', 
    ' ': ' '
    }
morse_code_dict_2 = {
    '.-': 'Z',   '-...': 'Y', '-.-.': 'X', '-..': 'W', '.': 'V',
    '..-.': 'U', '--.': 'T', '....': 'S', '..': 'R', '.---': 'Q',
    '-.-': 'P',  '.-..': 'O', '--': 'N', '-.': 'M', '---': 'L',
    '.--.': 'K', '--.-': 'J', '.-.': 'I', '...': 'H', '-': 'G',
    '..-': 'F',  '...-': 'E', '.--': 'D', '-..-': 'C', '-.--': 'B',
    '--..': 'A',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', 
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', 
    ' ': ' '
    }
morse_code_dict_3 = {
    '.-': 'M',   '-...': 'N', '-.-.': 'V', '-..': 'C', '.': 'Z',
    '..-.': 'L', '--.': 'O', '....': 'P', '..': 'Y', '.---': 'E',
    '-.-': 'J',  '.-..': 'U', '--': 'B', '-.': 'Q', '---': 'D',
    '.--.': 'T', '--.-': 'A', '.-.': 'W', '...': 'R', '-': 'S',
    '..-': 'I',  '...-': 'F', '.--': 'G', '-..-': 'X', '-.--': 'H',
    '--..': 'K',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', 
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', 
    ' ': ' '
}

# Function to select a dictionary based on user input
def select_random_dictionary():
    random_num= random.randint(1,3)
    # Generate a random number between 1 and 3
    if random_num == 1:
        return morse_code_dict_1
    elif random_num == 2:
        return morse_code_dict_2
    elif random_num == 3:
        return morse_code_dict_3
    
# Function to decode Morse code to text
def morse_to_text(morse_code, selected_dict):
    morse_code = morse_code.split(' ')
    text = ''
    for symbol in morse_code:
        if symbol in selected_dict:
            text += selected_dict[symbol]
        else:
            text += ' '
    return text



n=1

while n!=0 :

    select_dict=select_random_dictionary()
    morse_code_input = input("Enter Morse Code:")
    decoded_message = morse_to_text(morse_code_input,select_dict )
    print(f"Decoded Text: {decoded_message}")

    n+=1

    print("MORSE CODE PROCESSING COMPLETED.")
