import sqlite3

EXTRA = [
    'redditblog.com', 'www.redditblog.com',
    'redditstatus.com', 'www.redditstatus.com',
    'redditmail.com',
    'sh.reddit.com', 'm.reddit.com',
]

db = sqlite3.connect(r'E:\sg-acct\adaway.db')
cur = db.cursor()
have = {r[0] for r in cur.execute('SELECT host FROM hosts_lists')}
added = 0
for d in EXTRA:
    if d in have:
        continue
    cur.execute(
        'INSERT INTO hosts_lists(host, type, enabled, redirection, source_id)'
        ' VALUES(?, 0, 1, NULL, 1)', (d,))
    cur.execute(
        'INSERT OR IGNORE INTO host_entries(host, type, redirection)'
        ' VALUES(?, 0, NULL)', (d,))
    added += 1
db.commit()
print('added:', added)
db.close()
