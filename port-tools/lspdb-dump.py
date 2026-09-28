import shutil
import sqlite3

shutil.copy(r'E:\lspcfg\modules_config.db', r'E:\lspcfg\mc-read.db')
shutil.copy(r'E:\lspcfg\modules_config.db-wal', r'E:\lspcfg\mc-read.db-wal')
shutil.copy(r'E:\lspcfg\modules_config.db-shm', r'E:\lspcfg\mc-read.db-shm')
db = sqlite3.connect(r'E:\lspcfg\mc-read.db')
cur = db.cursor()
print('=== modules ===')
for r in cur.execute('SELECT * FROM modules'):
    print('  ', r)
print('=== modules_state ===')
for r in cur.execute('SELECT * FROM modules_state'):
    print('  ', r)
print('=== scope ===')
for r in cur.execute('SELECT * FROM scope'):
    print('  ', r)
db.close()
