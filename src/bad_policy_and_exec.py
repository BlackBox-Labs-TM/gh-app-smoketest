# 🚨 Triggers your regex rule + CodeQL

# Policy violation: wildcard import
from typing import *

def run_user_code(code_str):
    # CodeQL should flag use of exec
    exec(code_str)  # 🚨
