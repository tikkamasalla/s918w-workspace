import json

p = r'E:\s918w-port\Root-My-Galaxy-Payloads\support\targets-v3.json'
raw = open(p, 'rb').read().decode()
anchor = '    {\r\n      "payloadId": "a53x-A536EXXSNGZG3",'
assert raw.count(anchor) == 1, 'anchor not unique'
assert 'dm3q-S918WVLS6CYB3' not in raw, 'already present'
lines = [
    '    {',
    '      "payloadId": "dm3q-S918WVLS6CYB3",',
    '      "displayName": "Galaxy S23 Ultra (Canada) SM-S918W | Kernel 5.15.148 (S918WVLS6CYB3)",',
    '      "models": ["SM-S918W"],',
    '      "kernelVersions": ["5.15.148"],',
    '      "exploit": {',
    '        "url": "https://raw.githubusercontent.com/BuSung-dev/Root-My-Galaxy-Payloads/main/artifacts/dm3q-S918WVLS6CYB3/cve-2026-43499-app.so",',
    '        "size": 104128',
    '      },',
    '      "kernelsu": {',
    '        "url": "https://raw.githubusercontent.com/BuSung-dev/Root-My-Galaxy-Payloads/main/kernelsu/ksud-dm3q-S918WVLS6CYB3-kdp",',
    '        "size": 4629456',
    '      }',
    '    },',
]
block = '\r\n'.join(lines) + '\r\n'
open(p, 'w', newline='').write(raw.replace(anchor, block + anchor))
d = json.loads(open(p, encoding='utf-8-sig').read())
print('valid json; n =', len(d['payloads']))
print('ours present:', any(e.get('payloadId') == 'dm3q-S918WVLS6CYB3' for e in d['payloads']))
