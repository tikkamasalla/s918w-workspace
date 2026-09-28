import os, shutil, glob

DST = r'E:\workspace-backup'
pairs = [
    (r'E:\s918w-port\tools', 'port-tools'),
    (r'E:\s918w-port\pytools', 'port-pytools'),
    (r'E:\s918w-port\src', 'port-src'),
    (r'E:\s918w-port\bin', 'port-bin'),
    (r'E:\s918w-port\dm3q-S918WVLS6CYB3', 'port-profile'),
]
n_files = 0
n_bytes = 0
for src, rel in pairs:
    if not os.path.isdir(src):
        print('SKIP (missing):', src)
        continue
    for root, dirs, files in os.walk(src):
        if '.git' in dirs:
            dirs.remove('.git')
        for f in files:
            s = os.path.join(root, f)
            d = os.path.join(DST, rel, os.path.relpath(s, src))
            os.makedirs(os.path.dirname(d), exist_ok=True)
            shutil.copy2(s, d)
            n_files += 1
            n_bytes += os.path.getsize(s)

singles = [
    ('port-docs', glob.glob(r'E:\s918w-port\*.md') + glob.glob(r'E:\s918w-port\*.json') + glob.glob(r'E:\s918w-port\feed-entry*')),
    ('port-evidence', glob.glob(r'E:\s918w-port\*.txt') + glob.glob(r'E:\s918w-port\*.png') + glob.glob(r'E:\s918w-port\*.log')),
    ('morphe-notes', glob.glob(r'E:\morphe\*.md') + glob.glob(r'E:\morphe\*.log') + glob.glob(r'E:\morphe\*.json')),
]
for rel, files in singles:
    for s in files:
        if os.path.isdir(s):
            continue
        if os.path.getsize(s) > 90 * 1048576:
            print('SKIP (too big):', s)
            continue
        d = os.path.join(DST, rel, os.path.basename(s))
        os.makedirs(os.path.dirname(d), exist_ok=True)
        shutil.copy2(s, d)
        n_files += 1
        n_bytes += os.path.getsize(s)

print('copied %d files, %.1fMB' % (n_files, n_bytes / 1048576))
