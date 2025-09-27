# Tokenize using tiktoken
# pip install tiktoken

import tiktoken

def main():
    # tiktoken for OpenAI
    print("Using tiktoken for tokenization...")
    encoding = tiktoken.get_encoding("cl100k_base")
    prompt = ""
    while prompt.lower() != "quit":
        prompt = input("Enter your prompt (or 'q' to exit): ")
        tokens = encoding.encode(prompt)
        print(f"Token count: {len(tokens)}")
        print(f"Tokens: {tokens}")

if __name__ == "__main__":
    main()