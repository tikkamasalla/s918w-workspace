import json

p = r'E:\s918w-port\Root-My-Galaxy-Payloads\support\targets-v3.json'
raw = open(p, 'rb').read().decode()
d = json.loads(raw)
ours = [e for e in d['payloads'] if e.get('payloadId') == 'dm3q-S918WVLS6CYB3']
assert len(ours) == 1, 'ours missing!'
d['payloads'] = ours
# Re-emit surgically: keep schemaVersion line, replace payloads array text.
# Simplest safe route: rebuild with the file's own style via targeted splice.
start = raw.find('"payloads"')
assert start > 0
head = raw[:start]
entry_lines = [
    '"payloads": [',
    '    {',
    '      "payloadId": "dm3q-S918WVLS6CYB3",',
    '      "displayName": "Galaxy S23 Ultra (Canada) SM-S918W | Kernel 5.15.148 (S918WVLS6CYB3)",',
    '      "models": ["SM-S918W"],',
    '      "kernelVersions": ["5.15.148"],',
    '      "exploit": {',
    '        "url": "https://raw.githubusercontent.com/tikkamasalla/Root-My-Galaxy-Payloads/main/artifacts/dm3q-S918WVLS6CYB3/cve-2026-43499-app.so",',
    '        "size": 104128',
    '      },',
    '      "rootHelper": {',
    '        "url": "https://raw.githubusercontent.com/tikkamasalla/Root-My-Galaxy-Payloads/main/artifacts/dm3q-S918WVLS6CYB3/cve-2026-43499-root",',
    '        "size": 27056',
    '      },',
    '      "kernelsu": {',
    '        "url": "https://raw.githubusercontent.com/tikkamasalla/Root-My-Galaxy-Payloads/main/kernelsu/ksud-dm3q-S918WVLS6CYB3-kdp",',
    '        "size": 4629456',
    '      },',
    '      "notes": "Device-tested SM-S918W S918WVLS6CYB3: uid=2000->0, KernelSU live, su_compat ENABLED. Temp root only.",',
    '      "slideSource": "tracefs"',
    '    }',
    '  ]',
    '}',
]
NL = '\r\n'
open(p, 'w', newline='').write(head + NL.join(entry_lines) + NL)
d2 = json.loads(open(p, encoding='utf-8-sig').read())
print('entries now:', len(d2['payloads']), '| id:', d2['payloads'][0]['payloadId'])
