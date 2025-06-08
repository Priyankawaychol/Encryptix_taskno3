import random 
import string

def gen_password(length:int)->str:
   
    if length <4:
        raise ValueError("Password length should be at least 4 characters for strength")
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digits_chars = string.digits
    punctuation_chars= string.punctuation
    
    password_chars=[random.choice(lowercase_chars),random.choice(uppercase_chars),random.choice(digits_chars),random.choice(punctuation_chars)]
    
    all_chars=lowercase_chars + uppercase_chars + digits_chars+ punctuation_chars
    password_chars += random.choices(all_chars , k=length-4)
    
    random.shuffle(password_chars)
    return ''.join(password_chars)


def main():
    print("Password Generator")
    while True:
     try:
         length_input=input("Enter the password length(mininumm 4): ").strip()
         length=int(length_input)
         if length <4:
          print("Please enter a number 4 or greater for a strong password ")
          continue
         if length >128:
          print("Please enter a smaller number(max 128) for performance reasons ")
          continue
         password = gen_password(length)
         print("\n Your Generated password is:\n" +password +"\n")
         break
     except ValueError:
        print("Invalid input! Please enter a valid  integer ")
        
       
if __name__== '__main__':
    main()
