from art import logo
from alphabet_list import alphabet

def ceasar(text, shift):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  encryption_text="" 
  for i in text:   
    if i in alphabet:
      position=alphabet.index(i)
      if direction=="encode":  
            encryption_text+=alphabet[position+shift]
      elif direction=="decode":      
          encryption_text+= alphabet[position-shift]
    else:
      encryption_text+=i

  if direction=="encode" or direction=="decode":
    print(f"The {direction}d text is '{encryption_text}'.")
  else:
    print("Wrong direction, please try again!")
  

print(logo)
input_text = input("Type your message:\n").lower()
input_shift = int(input("Type the shift number:\n"))
input_shift = input_shift % 26

ceasar(input_text, input_shift)

confirmation=input("Do you want to continue? Type 'yes' or 'no'.")
while confirmation=='yes':
  input_text = input("Type your message:\n").lower()
  input_shift = int(input("Type the shift number:\n"))
  input_shift = input_shift % 26
  ceasar(input_text, input_shift)
  confirmation=input("Do you want to continue? Type 'yes' or 'no'.")
else:
  print("The program has stopped. Good Bye!")


