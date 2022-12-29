import sqlite3

lst = []
con = sqlite3.connect("music_db.sqlite")
cur = con.cursor()
ans = cur.execute(f"""SELECT DISTINCT
  a.name
FROM 
  genre g,
  track t,
  album al,
  artist a
WHERE
  t.genreid = g.genreid 
AND
  t.albumid = al.albumid
AND
  al.artistid = a.artistid
AND
  g.name = '{input()}'
ORDER BY a.name;""")

for i in ans:
    if i[0] in lst:
        continue
    if i[0] not in lst:
        lst.append(i[0])
for k in lst:
    print(*k)

con.close()
