import random
import string

def generate_big_dictionary(filename='data/dictionary.txt', size=1_000_000):
    print(f"[*] Generating a dictionary of {size} words...")
    
    # A few common/known passwords we want the dictionary to include
    real_passwords = ["password123", "admin", "secret", "mypassword", "testing1_pass", "admin2024!", "qwerty2026@"]
    
    # Words, years, symbols to combine
    words = ["user", "root", "super", "hello", "world", "dragon", "star", "cyber", "data", "sec"]
    years = [str(y) for y in range(2010, 2030)]
    symbols = ["!", "@", "#", "$", "*", "-", "_"]

    with open(filename, 'w') as f:
        # Seed the dictionary with those known passwords first
        for p in real_passwords:
            f.write(p + '\n')
            
        # Then add randomly generated entries to reach the target size
        for _ in range(size):
            pattern = random.choice([1, 2, 3])
            if pattern == 1:
                # Word + Year + Symbol (e.g. cyber2024!)
                random_pass = random.choice(words) + random.choice(years) + random.choice(symbols)
            elif pattern == 2:
                # Symbol + Word + Year (e.g. !dragon2015)
                random_pass = random.choice(symbols) + random.choice(words) + random.choice(years)
            else:
                # Random 8 char like before
                random_pass = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            f.write(random_pass + '\n')
            
    print(f"[+] Done! File {filename} was created. The size is ~{size/100000:.1f} MB.")

if __name__ == "__main__":
    generate_big_dictionary()