import json

NL = '\r\n'
p = r'E:\s918w-port\Root-My-Galaxy-Payloads\support\targets-v3.json'
raw = open(p, 'rb').read().decode()
assert 'dm3q-S918WVLS6CYB3' not in raw, 'already present'
# append after the dm3q-S918B entry to keep dm3q together
anchor = '    {' + NL + '      "payloadId": "a53x-A536EXXSNGZG3",'
assert raw.count(anchor) == 1, 'anchor issue'
base = 'https://raw.githubusercontent.com/tikkamasalla/Root-My-Galaxy-Payloads/main'
lines = [
    '    {',
    '      "payloadId": "dm3q-S918WVLS6CYB3",',
    '      "displayName": "Galaxy S23 Ultra (Canada) SM-S918W | Kernel 5.15.148 (S918WVLS6CYB3)",',
    '      "models": ["SM-S918W"],',
    '      "kernelVersions": ["5.15.148"],',
    '      "exploit": {',
    '        "url": "' + base + '/artifacts/dm3q-S918WVLS6CYB3/cve-2026-43499-app.so",',
    '        "size": 104128',
    '      },',
    '      "rootHelper": {',
    '        "url": "' + base + '/artifacts/dm3q-S918WVLS6CYB3/cve-2026-43499-root",',
    '        "size": 27056',
    '      },',
    '      "kernelsu": {',
    '        "url": "' + base + '/kernelsu/ksud-dm3q-S918WVLS6CYB3-kdp",',
    '        "size": 4629456',
    '      },',
    '      "notes": "Device-tested SM-S918W S918WVLS6CYB3: uid=2000->0, KernelSU live, su_compat ENABLED. Temp root only.",',
    '      "slideSource": "tracefs"',
    '    },',
]
block = NL.join(lines) + NL
open(p, 'w', newline='').write(raw.replace(anchor, block + anchor))
d = json.loads(open(p, encoding='utf-8-sig').read())
print('valid json; n =', len(d['payloads']))
print('ours present:', any(e.get('payloadId') == 'dm3q-S918WVLS6CYB3' for e in d['payloads']))
