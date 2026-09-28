import re

tags = ['iuUqAks9', 'dd1GzL6Y', 'o1hdUbe6', 'yUCWQPIx', 'PuNmEjUo',
        'swpe0-ntx', 'Mju9dIBv', 'FV0bGlhs', 'n_DZ9yG4',
        'EwKXnqjv', 'ukrLropw', 'bvXKQxXf', 'Iid_6P6K']
lines = open(r'E:\s918w-port\pkglist.txt', encoding='utf-8',
             errors='replace').read().splitlines()
for ln in lines:
    if any(t in ln for t in tags):
        m = re.match(r'package:(.*\.apk)=(.*)', ln)
        if m:
            print(m.group(2), '<-', m.group(1)[:90])
