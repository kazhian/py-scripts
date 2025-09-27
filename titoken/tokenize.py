# Tokenize using tiktoken
# pip install tiktoken

import tiktoken

def main():
    # tiktoken for OpenAI
    print("Using tiktoken for tokenization...")
    encoding = tiktoken.get_encoding("cl100k_base")
    prompt = ""
    while prompt != "quit":
        prompt = input("Enter your prompt: ")
        tokens = encoding.encode(prompt)
        print(f"tiktoken tokens: {tokens}\n")

if __name__ == "__main__":
    main()