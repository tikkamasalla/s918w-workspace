import sqlite3

db = sqlite3.connect(r'E:\sg-acct\accounts_ce.db')
cur = db.cursor()
tables = [r[0] for r in cur.execute(
    "SELECT name FROM sqlite_master WHERE type='table'")]
print('tables:', tables)
cols = [r[1] for r in cur.execute('PRAGMA table_info(accounts)')]
print('accounts cols:', cols)
rows = cur.execute(
    "SELECT _id, name, type, length(password) FROM accounts "
    "WHERE type LIKE '%seriesguide%'").fetchall()
for r in rows:
    print('row:', r[0], '|', r[1], '|', r[2], '| pw_len:', r[3])
db.close()
