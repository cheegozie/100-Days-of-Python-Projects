import random
import string
import argparse

parser = argparse.ArgumentParser(description="Generate a secure random password.")
parser.add_argument('--length', type=int, default=12, help='Length of the password (default: 12)')
args = parser.parse_args()

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("🔐 Your Secure Password:", generate_password(args.length))
