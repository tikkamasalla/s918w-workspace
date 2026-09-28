import json

def load_lines(path):
    with open(path) as f:
        return [ln.strip() for ln in f if ln.strip()]

mine = set()
for fn in ['combined_all-import-01.txt', 'combined_all-import-02.txt', 'ftc.txt']:
    try:
        mine.update(load_lines(
            r'C:\Users\Aows\Downloads\CallShield-blocklists\\' + fn))
    except FileNotFoundError:
        print('missing:', fn)
print('mine total:', len(mine))

d = json.load(open(
    r'C:\Users\Aows\Downloads\callshield-port\CallShield\data\spam_numbers.json'))
ups = set()
for e in d['numbers']:
    n = str(e.get('number', ''))
    digits = ''.join(c for c in n if c.isdigit())
    ups.add(digits)

def norm(s):
    dd = ''.join(c for c in s if c.isdigit())
    return dd.lstrip('1') if len(dd) == 11 and dd.startswith('1') else dd

mine_n = {norm(x) for x in mine}
ups_n = {norm(x) for x in ups}
both = mine_n & ups_n
print('upstream total:', len(ups_n))
print('overlap:', len(both))
print('mine only (NEW):', len(mine_n - ups_n))
