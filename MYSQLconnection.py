import pymysql

# Open database connection
db = pymysql.connect("localhost","root","harunbaba","city" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("select * from CITY")

# Fetch a single row using fetchone() method.
for row in cursor:
    print(row)


# disconnect from server
db.close()