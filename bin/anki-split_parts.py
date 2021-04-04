import csv
from pathlib import Path
anki_import_Dir = Path(
    r'C:\Users\14049\WordAndStudy\Projects\anki-导入')

testFile = anki_import_Dir / 'unit7-测一测.txt'

with open(testFile, 'r', newline='', encoding='utf-8') as f:
    for i in range(10):
        line = f.readline()
        for w in line:
            if not (w >= u'\u4E00' and w <= u'\u9FA5'):
                print(hex(ord(w)), w)
