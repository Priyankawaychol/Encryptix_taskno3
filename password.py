import random 
import string

def gen_password(length:int)->str:
   
    
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
         length_input=input("Enter the password length(mininumm 4): ")
         length=int(length_input)
         if length <4:
          print("Please enter a password length should be atleast 4 ")
          continue
         break
     except ValueError:
        print("Invalid input! Please enter a valid  integer ")
        
    
    password = gen_password(length)
    print("\n Your Generated password is:")
    print(password)
        
if __name__== '__main__':
    main()
