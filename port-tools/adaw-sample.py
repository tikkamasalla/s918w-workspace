import sqlite3

db = sqlite3.connect(r'E:\sg-acct\adaway.db')
cur = db.cursor()
print('source_ids:', cur.execute(
    'SELECT DISTINCT source_id FROM hosts_lists').fetchall())
print('redirections:', cur.execute(
    'SELECT DISTINCT redirection FROM hosts_lists').fetchall())
print('enabled vals:', cur.execute(
    'SELECT DISTINCT enabled FROM hosts_lists').fetchall())
print('sample:', cur.execute(
    'SELECT id, host, enabled, redirection, source_id FROM hosts_lists '
    'LIMIT 3').fetchall())
print('max id:', cur.execute('SELECT MAX(id) FROM hosts_lists').fetchone())
db.close()
