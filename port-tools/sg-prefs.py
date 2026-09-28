import re
for label, path in [
    ('installed-2026.1.5', r'E:\SeriesGuide-classic-input\SeriesGuide-installed-2026.1.5.apk'),
    ('classic-build', r'E:\SeriesGuide-classic\app\build\outputs\apk\pure\release\app-pure-release.apk'),
]:
    data = open(path, 'rb').read()
    print('===', label)
    # find oauth/trakt prefs file name references
    for m in set(re.findall(rb'[A-Za-z0-9_\-]*trakt[A-Za-z0-9_\-\.]*', data)):
        s = m.decode()
        if len(s) > 4:
            print('  ', s)
