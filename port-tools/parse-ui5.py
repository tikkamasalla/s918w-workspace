import re
d = open(r'E:\s918w-port\ui.xml', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'<node[^>]*>', d):
    n = m.group(0)
    t = (re.search(r'text="([^"]*)"', n) or [None, ''])[1]
    c = (re.search(r'content-desc="([^"]*)"', n) or [None, ''])[1]
    b = re.search(r'bounds="([^"]+)"', n).group(1)
    tt = (t + ' ' + c).strip()
    if tt in ('Modules', 'Repository', 'Settings', 'Overview'):
        print(repr(tt), b)
