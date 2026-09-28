import re
for label, path in [
    ('installed-2026.1.5', r'E:\SeriesGuide-classic-input\SeriesGuide-installed-2026.1.5.apk'),
    ('classic-build', r'E:\SeriesGuide-classic\app\build\outputs\apk\pure\release\app-pure-release.apk'),
]:
    data = open(path, 'rb').read()
    print('===', label)
    found = set()
    for m in set(re.findall(rb'[A-Za-z0-9_\-\.]{4,80}', data)):
        s = m.decode()
        sl = s.lower()
        if ('oauth' in sl or 'credential' in sl or 'refresh_token' in sl or 'access_token' in sl) and ('xml' not in sl or 'setting' in sl or 'pref' in sl or 'oauth' in sl):
            if not any(x in sl for x in ('fragment_', 'dialog_', 'activity_', 'ic_', 'menu_', 'layout', '.png', '.jpg')):
                found.add(s)
    for s in sorted(found)[:40]:
        print('  ', s)
