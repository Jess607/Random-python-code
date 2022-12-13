import re
def filepath():
    doc=input('Enter path:')
    with open(doc, 'r') as file:
        abs=file.read()
    list_abs=len(list(abs))
    total=[]
    match=re.findall(r'\w+', abs)
    for mat in match:
        total.append(mat)
    return 'your file has', list_abs, 'characters and', len(total), 'words'






print(filepath())



