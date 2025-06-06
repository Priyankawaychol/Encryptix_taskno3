import random 
import string

def gen_password(length):
    if length <4:
        print("password length should be atleast 4 ")
        return None
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars= string.punctuation
    
    password_chars=[random.choice(lowercase),random.choice(uppercase),random.choice(digits),random.choice(special_chars)]
    
    all_chars=lowercase + uppercase + digits + special_chars
    password_chars += random.choices(all_chars , k=length-4)
    
    random.shuffle(password_chars)
    return ''.join(password_chars)


def main():
    try:
       length=int(input("Enter the password length(mininumm 4): "))
    except ValueError:
        print("Invalid input! Please enter a valid input as integer")
        return
    
    password = gen_password(length)
    if password:
        print(f"Generated password: {password}")
        
if __name__== "__main__":
    main()
