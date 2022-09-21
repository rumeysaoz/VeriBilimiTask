import psycopg2


hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = 'root'
port_id = 5432
conn = None
cur = None

/*
Initially, I generated a postgres main class and put it in a conn variable.
The cursor() function of the main class was used to construct a cursor object,
 then the execute() method was used to drop the table name if it existed, 
 and then the script that generates the table was executed.
*/
try:
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id
            )

    cur = conn.cursor()

    cur.execute("Select * from flights_table")
    flights = cur.fetchall()
    for i in flights:
        print(i)
    cur.execute("Select * from gps_table")
    gps = cur.fetchall()
    for i in gps:
        print(i)

    cur.execute("Select * from angular_velocity_table")
    angular_velocity = cur.fetchall()
    for i in angular_velocity:
        print(i)




/*
Eventually, all of these programs are encased in a try/except block to catch and display any errors.
I stopped the connection in the finally block.
*/
except Exception as error:
    print(error)
finally:
    if cur is None:
        cur.close()



