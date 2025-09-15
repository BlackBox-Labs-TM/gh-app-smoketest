# insecure code: CodeQL should flag use of exec()
def run_user_code(code_str):
    exec(code_str)
