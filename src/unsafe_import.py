# 🚨 Should still trigger CodeQL, even without policy
from typing import *

def run_user_code(code_str):
    exec(code_str)  # 🚨 CodeQL should flag this
