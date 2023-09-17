from tkinter import messagebox, simpledialog, Tk


def is_even(number):
    # even check
    return number % 2 == 0


def get_even_letters(message):
    # getting even pos characters
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters


def get_odd_letters(message):
    # getting odd pos characters
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters


def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message) / 2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

def get_task():
    choice = simpledialog.askstring('Choice', 'Do you want to encrypt or decrypt?')
    return choice


def get_message():
    text = simpledialog.askstring('Message', 'Enter the text')
    return text


root = Tk()
root.withdraw()
# infinite loop for the user
while True:
    # choice for encyption or decryption
    task = get_task()

    if task == 'encrypt':
        # message from the user
        message = get_message()
        encrypted = swap_letters(message)
        # to show the encrypted message
        messagebox.showinfo('Ciphertext of the secret message is:', encrypted)

    elif task == 'decrypt':
        # message from the user
        message = get_message()
        decrypted = swap_letters(message)
        # to showthe encrypted message
        messagebox.showinfo('Plaintext of the secret message is:', decrypted)
    else:
        break

































