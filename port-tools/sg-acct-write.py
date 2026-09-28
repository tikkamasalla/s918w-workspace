import sqlite3

db = sqlite3.connect(r'E:\sg-acct\accounts_ce.db')
cur = db.cursor()
pw = cur.execute(
    "SELECT password FROM accounts WHERE _id=545").fetchone()[0]
assert pw and len(pw) == 32, 'unexpected source'
cur.execute("UPDATE accounts SET password=? WHERE _id=592", (pw,))
print('updated rows:', db.total_changes)
chk = cur.execute("SELECT length(password) FROM accounts WHERE _id=592"
                  ).fetchone()[0]
print('classic pw_len now:', chk)
db.commit()
db.close()
print('committed')
