import sqlite3

db = sqlite3.connect(r'E:\sg-acct\adaway.db')
cur = db.cursor()
have = {r[0] for r in cur.execute('SELECT host FROM hosts_lists')}
print('user rows:', cur.execute(
    'SELECT COUNT(*) FROM hosts_lists WHERE source_id=1').fetchone()[0])
for d in ['reddit.map.fastly.net']:
    if d in have:
        print(d, 'already present')
        continue
    cur.execute(
        'INSERT INTO hosts_lists(host, type, enabled, redirection, source_id)'
        ' VALUES(?, 0, 1, NULL, 1)', (d,))
    cur.execute(
        'INSERT OR IGNORE INTO host_entries(host, type, redirection)'
        ' VALUES(?, 0, NULL)', (d,))
    print('added', d)
db.commit()
db.close()
