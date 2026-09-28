import json

d = json.load(open(r'E:\sg-acct\upstream-spam.json'))
ups = {str(e.get('number', '')) for e in d['numbers']}

def load_lines(path):
    with open(path) as f:
        return [ln.strip() for ln in f if ln.strip()]

mine = set()
for fn in ['combined_all-import-01.txt', 'combined_all-import-02.txt']:
    mine.update(load_lines(
        r'C:\Users\Aows\Downloads\CallShield-blocklists\\' + fn))

both = mine & ups
print('mine:', len(mine), '| ups v49:', len(ups))
print('exact overlap vs v49:', len(both))
print('mine only:', len(mine - ups))
