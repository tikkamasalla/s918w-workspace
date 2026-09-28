import sqlite3
db = sqlite3.connect(r'E:\lspcfg\mc.db')
mods = [r[0] for r in db.execute('SELECT module_pkg_name FROM modules ORDER BY 1')]
states = {r[0]: (r[1], r[2]) for r in db.execute('SELECT module_pkg_name, user_id, enabled FROM modules_state')}
print('modules:', len(mods), 'states:', len(states))
for m in mods:
    s = states.get(m, 'NO-STATE-ROW')
    print(('EN' if s != 'NO-STATE-ROW' and s[1] else ('dis' if s != 'NO-STATE-ROW' else '???')), m, s)
print('--- scope user_ids:')
print(db.execute('SELECT DISTINCT user_id FROM scope').fetchall())
print('--- scope count per module:')
for r in db.execute('SELECT module_pkg_name, COUNT(*) FROM scope GROUP BY 1 ORDER BY 2 DESC'):
    print(r)
db.close()
