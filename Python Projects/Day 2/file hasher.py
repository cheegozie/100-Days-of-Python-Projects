import argparse
import hashlib

# 1. Set up argument parser
parser = argparse.ArgumentParser(description="Hash a file using MD5, SHA1, or SHA256")
parser.add_argument("filename", help="Path to the file you want to hash")
parser.add_argument("--algo", choices=["md5", "sha1", "sha256"], default="sha256", help="Hash algorithm to use (default: sha256)")
parser.add_argument("--show-bytes", action="store_true", help="Print raw file bytes before hashing")

# 2. Parse the arguments
args = parser.parse_args()

# 3. Read the file
with open(args.filename, "rb") as f:
    file_content = f.read()

# 4. Optionally print the file content
if args.show_bytes:
    print("\nRaw file bytes:\n", file_content, "\n")

# 5. Pick the algorithm
if args.algo == "md5":
    hasher = hashlib.md5(file_content)
elif args.algo == "sha1":
    hasher = hashlib.sha1(file_content)
else:
    hasher = hashlib.sha256(file_content)

# 6. Print the hash
print(f"{args.algo.upper()} hash of {args.filename}:\n{hasher.hexdigest()}")
