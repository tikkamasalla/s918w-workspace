import os
from collections import defaultdict
tot = defaultdict(int)
big = []
for root, dirs, files in os.walk(r'E:\s918w-port'):
    if '.git' in dirs:
        dirs.remove('.git')
    for f in files:
        p = os.path.join(root, f)
        try:
            s = os.path.getsize(p)
        except OSError:
            continue
        tot[os.path.splitext(f)[1].lower() or '(noext)'] += s
        if s > 100 * 1048576:
            big.append((s, p))
print('--- by extension:')
for ext, sz in sorted(tot.items(), key=lambda x: -x[1])[:12]:
    print('%s  %.0fMB' % (ext, sz / 1048576))
print('--- files over 100MB:')
for s, p in sorted(big, reverse=True)[:15]:
    print('%.0fMB  %s' % (s / 1048576, p))
