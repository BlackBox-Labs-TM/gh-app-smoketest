"""
mock_vuln.py
Safe-for-testing example file that contains patterns commonly flagged by scanners.
Do NOT use this file in production. Only commit to a disposable test repository.
"""

# --- Hardcoded "secret" (intentionally benign placeholder) ---
API_KEY = "TEST_ONLY_DO_NOT_USE_0123456789"

def get_api_key():
    return API_KEY

def run_untrusted_expression(expr: str):
    # insecure pattern for static analysis tests (do not call)
    return eval(expr)

import subprocess
def run_command(cmd: str):
    subprocess.run(cmd, shell=True)

import pickle
def load_pickle_bytes(b: bytes):
    return pickle.loads(b)

import random
def insecure_token():
    choices = "abcdefghijklmnopqrstuvwxyz0123456789"
    return "".join(random.choice(choices) for _ in range(16))

import hashlib
def md5_hash(s: str):
    return hashlib.md5(s.encode()).hexdigest()

if __name__ == "__main__":
    print("This module is a static test artifact for security scanning only.")
