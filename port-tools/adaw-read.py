import sqlite3

db = sqlite3.connect(r'E:\sg-acct\adaway.db')
cur = db.cursor()
tables = [r[0] for r in cur.execute(
    "SELECT name FROM sqlite_master WHERE type='table'")]
print('tables:', tables)
for t in tables:
    try:
        cols = [r[1] for r in cur.execute(f'PRAGMA table_info({t})')]
        n = cur.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]
        print(f'{t}: cols={cols} rows={n}')
    except Exception as e:
        print(t, 'ERR', str(e)[:80])
db.close()
