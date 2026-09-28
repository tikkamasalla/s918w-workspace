import re
d = open(r'E:\s918w-port\ui.xml', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'text="([^"]*)"[^>]*bounds="([^"]+)"', d):
    t = m.group(1).strip()
    if t and len(t) < 60 and ('daw' in t.lower() or 'termux' in t.lower() or 'superuser' in t.lower()):
        print(repr(t), m.group(2))
