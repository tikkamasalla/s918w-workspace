import sqlite3

DOMAINS = [
    'reddit.com', 'www.reddit.com', 'old.reddit.com', 'new.reddit.com',
    'np.reddit.com', 'mod.reddit.com', 'redd.it', 'i.redd.it',
    'preview.redd.it', 'v.redd.it', 'redditstatic.com',
    'www.redditstatic.com', 'redditmedia.com', 'redditinc.com',
    'events.reddit.com', 'auth.reddit.com', 'gateway.reddit.com',
    'out.reddit.com', 'g.reddit.com', 'album.reddit.com',
]

db = sqlite3.connect(r'E:\sg-acct\adaway.db')
cur = db.cursor()
have = {r[0] for r in cur.execute('SELECT host FROM hosts_lists')}
added = 0
for d in DOMAINS:
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
print('user rows now:', cur.execute(
    'SELECT COUNT(*) FROM hosts_lists WHERE source_id=1').fetchone()[0])
db.close()
