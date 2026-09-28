import sqlite3, shutil, sys
src = r'E:\lspcfg\mc.db'
dst = r'E:\lspcfg\mc-off.db'
shutil.copy(src, dst)
db = sqlite3.connect(dst)
n = db.execute('UPDATE modules_state SET enabled = 0').rowcount
db.commit()
print('disabled rows:', n)
print('still enabled:', db.execute('SELECT COUNT(*) FROM modules_state WHERE enabled != 0').fetchone()[0])
db.execute('PRAGMA journal_mode = DELETE')
db.commit()
db.close()
print('built', dst)
