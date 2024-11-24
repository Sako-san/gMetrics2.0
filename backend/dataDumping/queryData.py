import sqlite3

conn = sqlite3.connect('baseball_data.db')
query = 'SELECT * FROM player_stats WHERE home_runs > 20'
results = conn.execute(query).fetchall()
for row in results:
    print(row)
conn.close()
