import random
import string

def generate_password(length):
    if length < 4:
        return "Password must be at least 4 characters long"
    
    # Guarantee one of each required type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill remaining length with random characters from all types
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password.extend(random.choices(all_chars, k=length-4))
    
    # Shuffle to randomize order
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        print(f"Generated password: {generate_password(length)}")
    except ValueError:
        print("Please enter a valid number")