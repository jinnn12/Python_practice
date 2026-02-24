from .graphic.render import render_test

VERSION = 3.5


def print_version_info():
    print(f"The version of this game is {VERSION}")

print("Initializing game ...") # 초기화 코드는 한 번 실행된 후, 다시 import 해도 실행되지 않음