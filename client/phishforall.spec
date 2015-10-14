# -*- mode: python -*-

from os import path
from platform import system
from random import choice
from site import getsitepackages


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
    icon_path = path.join("icons", "pdf.icns")
    name = "{}".format(base_name)

block_cipher = pyi_crypto.PyiBlockCipher(key=gen_key())

netaddr_path = None
for site_path in getsitepackages():
    test_path = path.join(site_path, "netaddr")
    if path.isdir(test_path):
        netaddr_path = test_path
        break
if netaddr_path is None:
    raise RuntimeError("Could not find the netaddr package in site-packages")

add_files = [
    ("templates", ""),
    ("logo.png", ""),
     (netaddr_path, "netaddr")
]

a = Analysis(['__main__.py'],
             pathex=['.'],
             binaries=None,
             datas=add_files,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=name,
          debug=False,
          strip=None,
          upx=False, # UPX triggers AV alarms
          console=False, icon=icon_path)

if platform_name == "Darwin":
    app = BUNDLE(exe,
                 name='{}.pdf.app'.format(name),
                 icon=icon_path,
                 bundle_identifier=None)
