import sqlite3

con = sqlite3.connect('game.db')

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS game
            (Title TEXT1, Director TEXT2, Year INT)''')
