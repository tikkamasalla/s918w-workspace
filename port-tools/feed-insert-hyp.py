import json

NL = '\r\n'
p = r'E:\rmg-hyp\support\targets-v3.json'
raw = open(p, 'rb').read().decode()
assert 'dm3q-S918WVLS6CYB3' not in raw, 'already present'
anchor = NL + '  ]' + NL + '}'
assert raw.endswith(anchor), 'unexpected tail: %r' % raw[-20:]
base = 'https://raw.githubusercontent.com/HyperRamzey/Root-My-Galaxy-Payloads/main'
lines = [
    '    {',
    '      "payloadId": "dm3q-S918WVLS6CYB3",',
    '      "displayName": "Galaxy S23 Ultra (Canada) SM-S918W | Kernel 5.15.148 (S918WVLS6CYB3)",',
    '      "models": [',
    '        "SM-S918W"',
    '      ],',
    '      "kernelVersions": [',
    '        "5.15.148"',
    '      ],',
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
    '      "notes": "Device-tested on physical SM-S918W (S918WVLS6CYB3): uid=2000->0, KernelSU live, Manager Working <LKM>, Termux su uid=0, su_compat ENABLED. Temp root only; run via Shizuku close to boot.",',
    '      "slideSource": "tracefs"',
    '    }',
]
new_tail = ',' + NL + NL.join(lines) + NL + '  ]' + NL + '}'
open(p, 'w', newline='').write(raw[: -len(anchor)] + new_tail)
d = json.loads(open(p, encoding='utf-8-sig').read())
print('valid json; n =', len(d['payloads']))
print('ours present:', any(e.get('payloadId') == 'dm3q-S918WVLS6CYB3' for e in d['payloads']))
