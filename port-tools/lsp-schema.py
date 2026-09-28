import sqlite3, shutil
shutil.copy(r'E:\lspcfg\mc.db', r'E:\lspcfg\mc-live-backup.db')
db = sqlite3.connect(r'E:\lspcfg\mc.db')
print('integrity:', db.execute('PRAGMA integrity_check').fetchone()[0])
tables = [r[0] for r in db.execute('SELECT name FROM sqlite_master WHERE type = \'table\'')]
print('tables:', tables)
for t in tables:
    cols = db.execute('PRAGMA table_info(' + t + ')').fetchall()
    n = db.execute('SELECT COUNT(*) FROM ' + t).fetchone()[0]
    print('---', t, 'rows=', n)
    for c in cols:
        print('   ', c)
db.close()
