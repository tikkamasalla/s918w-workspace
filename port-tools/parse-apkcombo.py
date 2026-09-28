import re
t = open(r'E:\s918w-port\apkcombo-xapk.html', encoding='utf-8', errors='replace').read()
pats = [r'<form[^>]{0,250}', r'checkin[^ "<>]{0,80}',
        r'onclick="[^"]{0,150}',
        r'data-[a-z-]*="[^"]{5,150}"']
for pat in pats:
    hits = sorted(set(re.findall(pat, t)))[:12]
    if hits:
        print('---', pat[:40])
        for h in hits:
            print('   ', h[:220].replace('\n', ' '))
