from subprocess import check_call


args = ["pyinstaller", "phishforall.spec"]

check_call(args)
