import os

def main():
    api_key = os.getenv("API_KEY")

    if api_key:
        print("API Key loaded securely")
    else:
        print("API Key not found")

if __name__ == "__main__":
    main()