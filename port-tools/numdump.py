import json

d = json.load(open(
    r'C:\Users\Aows\Downloads\callshield-port\CallShield\data\spam_numbers.json'))
seen = set()
out = []
for e in d['numbers']:
    n = str(e.get('number', '')).strip()
    if n and n not in seen:
        seen.add(n)
        out.append(n)
out.sort()
with open(r'C:\Users\Aows\Desktop\callshield-blocklist.txt', 'w') as f:
    f.write('\n'.join(out) + '\n')
print('wrote:', len(out))
