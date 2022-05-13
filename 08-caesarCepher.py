alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#CAESAR FUNCTION
def caesar():
  run_program = "yes"
  while run_program == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    start_text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))
    end_text = ""
    #encode or decode direction
    if direction == "decode":
        shift_amount *= -1
    for char in start_text:
      #check if it's a letter
      if char in alphabet:
        position = alphabet.index(char)
        if shift_amount > 26:
          shift_amount -= 26
        #replace the letter
        new_position = position + shift_amount
        end_text += alphabet[new_position]
      #else keep the initial character
      else:
        end_text += char
    print(f"The {direction}d text is {end_text}")
    #run again the loop or not
    run_program = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

#calling function
caesar()