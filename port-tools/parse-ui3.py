import re
d = open(r'E:\s918w-port\ui.xml', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'<node[^>]*>', d):
    n = m.group(0)
    t = re.search(r'text="([^"]*)"', n)
    c = re.search(r'content-desc="([^"]*)"', n)
    b = re.search(r'bounds="([^"]+)"', n)
    bb = b.group(1) if b else ''
    tt = t.group(1) if t else ''
    cc = c.group(1) if c else ''
    if 'uperuser' in tt or 'uperuser' in cc or 'oot' in tt:
        print(repr(tt), '|', repr(cc), '|', bb)
