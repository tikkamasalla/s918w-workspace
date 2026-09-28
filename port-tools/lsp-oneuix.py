import sqlite3
db = sqlite3.connect(r'E:\lspcfg\mc.db')
for r in db.execute('SELECT module_pkg_name, apk_path FROM modules'):
    if 'oneuix' in r[0] or 'soclear' in r[0]:
        print(r)
db.close()
