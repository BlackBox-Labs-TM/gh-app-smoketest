# Should trigger policy regex matches and warnings

import os
import requests

API_KEY = "sk_live_ABC12345SECRET98765"
DB_PASSWORD = "password123"

def connect_to_service(api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get("https://example.com/data", headers=headers)
    return response.status_code

def save_token(token):
    # storing tokens insecurely
    with open("token.txt", "w") as f:
        f.write(token)

def main():
    token = "TEMPORARY-TOKEN-KEY-XYZ"
    save_token(token)
    code = connect_to_service(API_KEY)
    print("Service status:", code)
    if code != 200:
        print("Warning: API key may be invalid")

if __name__ == "__main__":
    main()

