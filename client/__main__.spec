# -*- mode: python -*-

block_cipher = None


a = Analysis(['__main__.py'],
             pathex=['/Users/sean/dev/tattle/client'],
             binaries=None,
             datas=None,
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
          name='__main__',
          debug=False,
          strip=None,
          upx=True,
          console=True , icon='icons/pdf.ico')
