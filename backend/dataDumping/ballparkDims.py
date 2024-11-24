import sqlite3

# Create a connection to the database (it will create baseball-dump.db if it doesn't exist)
conn = sqlite3.connect("baseball-dump.db")
cursor = conn.cursor()

# Step 1: Create the ballpark_dimensions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS ballpark_dimensions (
    ballpark_name TEXT,
    team TEXT,
    start_date INTEGER,
    end_date INTEGER,
    league TEXT,
    left_field INTEGER,
    left_center INTEGER,
    center_field INTEGER,
    right_center INTEGER,
    right_field INTEGER,
    wall_height_notes TEXT,
    changes TEXT
);
""")

# Step 2: Insert the data into the table
data = [
    # Camden Yards (Baltimore Orioles)
    ('Camden Yards', 'Baltimore Orioles', 1992, 2021, 'AL', 333, 364, 400, 373, 318, None, None),
    ('Camden Yards', 'Baltimore Orioles', 2022, None, 'AL', 333, 384, 400, 373, 318, None, '2022: Left field pushed back to 384 ft; wall height increased to 13 ft.'),

    # Fenway Park (Boston Red Sox)
    ('Fenway Park', 'Boston Red Sox', 1912, None, 'AL', 310, 379, 390, 420, 302, 'Green Monster (37 ft tall)', None),

    # Guaranteed Rate Field (Chicago White Sox)
    ('Guaranteed Rate Field', 'Chicago White Sox', 1991, None, 'AL', 330, 375, 400, 375, 335, None, None),

    # Progressive Field (Cleveland Guardians)
    ('Progressive Field', 'Cleveland Guardians', 1994, None, 'AL', 325, 370, 400, 375, 325, None, None),

    # Comerica Park (Detroit Tigers)
    ('Comerica Park', 'Detroit Tigers', 2000, 2022, 'AL', 345, 370, 422, 365, 330, None, None),
    ('Comerica Park', 'Detroit Tigers', 2023, None, 'AL', 345, 370, 412, 365, 330, 'Center field wall reduced to 7 ft.', '2023: Center field reduced from 422 ft to 412 ft.'),

    # Minute Maid Park (Houston Astros)
    ('Minute Maid Park', 'Houston Astros', 2000, 2015, 'AL', 315, 362, 436, 373, 326, 'Included Tal\'s Hill.', None),
    ('Minute Maid Park', 'Houston Astros', 2016, None, 'AL', 315, 362, 409, 373, 326, None, '2016: Tal\'s Hill removed; center field reduced from 436 ft to 409 ft.'),

    # Kauffman Stadium (Kansas City Royals)
    ('Kauffman Stadium', 'Kansas City Royals', 1973, None, 'AL', 330, 387, 410, 387, 330, None, None),

    # Angel Stadium (Los Angeles Angels)
    ('Angel Stadium', 'Los Angeles Angels', 1966, None, 'AL', 347, 390, 396, 370, 350, None, None),

    # Target Field (Minnesota Twins)
    ('Target Field', 'Minnesota Twins', 2010, None, 'AL', 339, 377, 404, 367, 328, None, None),

    # Yankee Stadium (New York Yankees)
    ('Yankee Stadium', 'New York Yankees', 2009, None, 'AL', 318, 399, 408, 385, 314, None, None),

    # Oakland Coliseum (Oakland Athletics)
    ('Oakland Coliseum', 'Oakland Athletics', 1968, None, 'AL', 330, 388, 400, 388, 330, None, None),

    # T-Mobile Park (Seattle Mariners)
    ('T-Mobile Park', 'Seattle Mariners', 1999, 2016, 'AL', 331, 385, 405, 385, 326, None, None),
    ('T-Mobile Park', 'Seattle Mariners', 2017, None, 'AL', 331, 378, 401, 381, 326, None, '2017: Center field moved from 405 ft to 401 ft; right-center reduced from 385 ft to 381 ft.'),

    # Tropicana Field (Tampa Bay Rays)
    ('Tropicana Field', 'Tampa Bay Rays', 1998, None, 'AL', 315, 370, 404, 370, 322, None, None),

    # Globe Life Field (Texas Rangers)
    ('Globe Life Field', 'Texas Rangers', 2020, None, 'AL', 329, 372, 407, 374, 326, None, '2020: New stadium opened.'),

    # Rogers Centre (Toronto Blue Jays)
    ('Rogers Centre', 'Toronto Blue Jays', 1989, 2022, 'AL', 328, 375, 400, 375, 328, None, None),
    ('Rogers Centre', 'Toronto Blue Jays', 2023, None, 'AL', 320, 366, 400, 357, 328, 'Wall heights increased.', '2023: Left field reduced to 320 ft; right-center reduced to 357 ft.'),

    # Chase Field (Arizona Diamondbacks)
    ('Chase Field', 'Arizona Diamondbacks', 1998, None, 'NL', 330, 374, 407, 374, 334, None, None),

    # Truist Park (Atlanta Braves)
    ('Truist Park', 'Atlanta Braves', 2017, None, 'NL', 335, 375, 400, 375, 325, None, '2017: New stadium replaced Turner Field.'),

    # Wrigley Field (Chicago Cubs)
    ('Wrigley Field', 'Chicago Cubs', 1914, None, 'NL', 355, 368, 400, 368, 353, None, None),

    # Great American Ball Park (Cincinnati Reds)
    ('Great American Ball Park', 'Cincinnati Reds', 2003, None, 'NL', 328, 379, 404, 370, 325, None, None),

    # Coors Field (Colorado Rockies)
    ('Coors Field', 'Colorado Rockies', 1995, None, 'NL', 347, 390, 415, 375, 350, None, None),

    # Dodger Stadium (Los Angeles Dodgers)
    ('Dodger Stadium', 'Los Angeles Dodgers', 1962, None, 'NL', 330, 385, 400, 385, 330, None, None),

    # LoanDepot Park (Miami Marlins)
    ('LoanDepot Park', 'Miami Marlins', 2012, 2015, 'NL', 344, 386, 418, 392, 335, None, None),
    ('LoanDepot Park', 'Miami Marlins', 2016, None, 'NL', 344, 386, 407, 392, 335, None, '2016: Center field reduced from 418 ft to 407 ft; right-center reduced from 392 ft to 387 ft.'),

    # American Family Field (Milwaukee Brewers)
    ('American Family Field', 'Milwaukee Brewers', 2001, None, 'NL', 344, 370, 400, 374, 345, None, None),

    # Citi Field (New York Mets)
    ('Citi Field', 'New York Mets', 2009, 2014, 'NL', 335, 378, 408, 390, 330, 'Deep right-center.', None),
    ('Citi Field', 'New York Mets', 2015, None, 'NL', 335, 370, 408, 380, 330, 'Wall height reduced to 8 ft.', '2015: Right-center reduced to 380 ft.'),

    # Citizens Bank Park (Philadelphia Phillies)
    ('Citizens Bank Park', 'Philadelphia Phillies', 2004, None, 'NL', 329, 374, 401, 369, 330, None, None),

    # PNC Park (Pittsburgh Pirates)
    ('PNC Park', 'Pittsburgh Pirates', 2001, None, 'NL', 325, 383, 399, 375, 320, None, None),

    # Busch Stadium (St. Louis Cardinals)
    ('Busch Stadium', 'St. Louis Cardinals', 2006, None, 'NL', 336, 375, 400, 375, 335, None, None),

    # Petco Park (San Diego Padres)
    ('Petco Park', 'San Diego Padres', 2004, 2014, 'NL', 334, 400, 396, 402, 322, None, None),
    ('Petco Park', 'San Diego Padres', 2015, None, 'NL', 334, 382, 396, 391, 322, 'Right field wall lowered to 8 ft.', '2015: Right-center reduced from 402 ft to 391 ft.'),

    # Oracle Park (San Francisco Giants)
    ('Oracle Park', 'San Francisco Giants', 2000, 2019, 'NL', 339, 364, 399, 421, 309, None, None),
    ('Oracle Park', 'San Francisco Giants', 2020, None, 'NL', 339, 364, 391, 415, 309, None, '2020: Center field reduced to 391 ft; right-center reduced to 415 ft.')
]

# Step 3: Insert all data
cursor.executemany("""
INSERT INTO ballpark_dimensions (
    ballpark_name, team, start_date, end_date, league, left_field, left_center, center_field,
    right_center, right_field, wall_height_notes, changes
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", data)

# Step 4: Commit changes and close the connection
conn.commit()
conn.close()

print("Database 'baseball-dump.db' created successfully and populated with data.")
