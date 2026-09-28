import re
d = open(r'E:\s918w-port\ui.xml', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'text="([^"]*)"[^>]*bounds="([^"]+)"', d):
    t, b = m.group(1), m.group(2)
    if 'oot based' in t or t.strip().lower() in ('allow', 'grant', 'permit', 'ok'):
        print(repr(t[:50]), b)
