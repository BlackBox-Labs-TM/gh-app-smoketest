# trigger_policy_test.py
# This file intentionally contains patterns that should trip the BlackBox audit regex rules.
# All keys and tokens below are dummy values and non‑functional.

import requests

# Keys and tokens (dummy placeholders)
DUMMY_OPENAI_KEY = "sk-0123456789abcdefghijklmnopqrstuvwxyzABC"
DUMMY_AWS_ACCESS_KEY = "AKIA1234567890ABCD"
DUMMY_AWS_SESSION_KEY = "ASIAABCDEFGHIJKLMNOP"
DUMMY_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.e30.Vg9GUmyUOS-a-U9O_W3mgN"
API_KEY = "MYAPIKEY123"
SECRET = "supersecret"
PASSWORD = "password123"
PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----"
ACCESS_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz012345"
bearer_token = "Bearer ABCDEFGHIJKLMNOPQRSTUVWXYZ123456"

def trigger_policy():
    # insecure function calls
    eval("print('eval triggered')")
    exec("print('exec triggered')")

    # print or otherwise use the dummy values
    print(
        DUMMY_OPENAI_KEY,
        DUMMY_AWS_ACCESS_KEY,
        DUMMY_AWS_SESSION_KEY,
        DUMMY_JWT,
        API_KEY,
        SECRET,
        PASSWORD,
        PRIVATE_KEY,
        ACCESS_TOKEN,
        bearer_token,
    )

    # insecure URL access
    response = requests.get("http://example.com")
    print("HTTP response status:", response.status_code)

if __name__ == "__main__":
    trigger_policy()

