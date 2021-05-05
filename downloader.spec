# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:\\Users\\owenw\\vscode\\projects\\Iproject\\src\\downloader.py'],
             pathex=['C:\\Users\\owenw\\vscode\\projects\\Iproject'],
             binaries=[],
             datas=[('C:\\Users\\owenw\\vscode\\projects\\Iproject\\data\\background1.png', '.'), ('C:\\Users\\owenw\\vscode\\projects\\Iproject\\data\\background2.jpg', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='downloader',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
