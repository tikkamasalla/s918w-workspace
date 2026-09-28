import json
from collections import Counter

def load_lines(path):
    with open(path) as f:
        return [ln.strip() for ln in f if ln.strip()]

mine = set()
for fn in ['combined_all-import-01.txt', 'combined_all-import-02.txt']:
    mine.update(load_lines(
        r'C:\Users\Aows\Downloads\CallShield-blocklists\\' + fn))

d = json.load(open(
    r'C:\Users\Aows\Downloads\callshield-port\CallShield\data\spam_numbers.json'))
ups = {str(e.get('number', '')) for e in d['numbers']}

def npa(s):
    dd = ''.join(c for c in s if c.isdigit())
    if len(dd) == 11 and dd.startswith('1'):
        dd = dd[1:]
    return dd[:6] if len(dd) >= 6 else dd

mine_npa = Counter(npa(x) for x in mine)
ups_npa = Counter(npa(x) for x in ups)
common = set(mine_npa) & set(ups_npa)
print('mine NPA groups:', len(mine_npa), '| ups NPA groups:', len(ups_npa))
print('shared NPA-NXX groups:', len(common))
print('mine top:', mine_npa.most_common(5))
print('ups top:', ups_npa.most_common(5))
