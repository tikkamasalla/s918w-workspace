import sqlite3

db = sqlite3.connect(r'E:\sg-acct\adaway.db')
cur = db.cursor()
print('types:', cur.execute(
    'SELECT DISTINCT type FROM hosts_lists').fetchall())
print('sources:', cur.execute(
    'SELECT id, label, enabled FROM hosts_sources').fetchall())
print('sample black:', cur.execute(
    "SELECT id, host, type, enabled, redirection, source_id FROM hosts_lists "
    "WHERE type LIKE '%LACK%' LIMIT 3").fetchall())
db.close()
