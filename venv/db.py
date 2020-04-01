# import psycopg2 to talk to the database, dont forget to install it!!!!
import psycopg2

# connection to the database
con = psycopg2.connect(
    host="localhost",
    database="pyex"
)

#cursor
cur = con.cursor()

# inserting a new employee, sanitized it with %s and put the values in a tuple
cur.execute("insert into employees (id, name) values (%s, %s)", (5, 'bob'))
# deleting an employee
cur.execute("delete from employees where name = 'jim'")
# updating an employee/s name
cur.execute("update employees set name = 'billy' where id = 4")
# getting all employee/s id/s and name/s
cur.execute("select id, name from employees")

# executes cursor? and fetches all 
rows = cur.fetchall()

# python/s version of console.log, will loop and print each result
for r in rows:
    print(f"id: {r[0]} name: {r[1]}")

# commit changes/connections
con.commit()

cur.close()

#close the database connection when youre done
con.close()