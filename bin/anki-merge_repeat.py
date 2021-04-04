import csv
from pathlib import Path 
anki_import_Dir = Path(r'C:\Users\14049\WordAndStudy\Projects\anki-导入')

mergedDir = anki_import_Dir / 'merged'
if not mergedDir.exists():
    mergedDir.mkdir()


for child in anki_import_Dir.glob('*.txt'):
    dic = {}
    with open(child,'r' ,newline='',encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|')
        for row in spamreader:
            if row[0] in dic:
                dic[row[0]]+='\n' # this?
                dic[row[0]]+=row[1]
            else:
                dic[row[0]] = row[1]

    # for l,r in dic.items():
    #     print(l,r)
    
    with open(mergedDir/ child.name,'w',newline='',encoding='utf-8') as f:
        spamwriter = csv.writer(f, delimiter='|', quoting=csv.QUOTE_MINIMAL)
        for l,r in dic.items():
            spamwriter.writerow([l,r])
