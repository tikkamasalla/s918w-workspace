import re
d = open(r'E:\s918w-port\ui.xml', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'<node[^>]*>', d):
    n = m.group(0)
    t = (re.search(r'text="([^"]*)"', n) or [None, ''])[1]
    b = re.search(r'bounds="([^"]+)"', n).group(1)
    if 'One UI X' in t or 'ne UI X' in t:
        print(repr(t), b)
