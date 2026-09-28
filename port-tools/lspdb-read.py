import shutil
import sqlite3

shutil.copy(r'E:\lspcfg\modules_config.db', r'E:\lspcfg\mc-read.db')
shutil.copy(r'E:\lspcfg\modules_config.db-wal', r'E:\lspcfg\mc-read.db-wal')
shutil.copy(r'E:\lspcfg\modules_config.db-shm', r'E:\lspcfg\mc-read.db-shm')
db = sqlite3.connect(r'E:\lspcfg\mc-read.db')
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
