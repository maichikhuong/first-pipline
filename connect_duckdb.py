import duckdb

# initiate the MotherDuck connection through a service token through
con = duckdb.connect('md:?motherduck_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzZXNzaW9uIjoibWFpY2hpa2h1b25nOTguZ21haWwuY29tIiwiZW1haWwiOiJtYWljaGlraHVvbmc5OEBnbWFpbC5jb20iLCJ1c2VySWQiOiI0NDdjZTk5NC05N2ZjLTQ4YmMtOTA1Mi1jMDE4ZmU0OGY1MTgiLCJpYXQiOjE3MDEyMzA0OTIsImV4cCI6MTczMjc4ODA5Mn0.2mwUo_yTq_ygchdVwjMY-Xe4zciDJejgttfo0MLFCO8')


# con.sql(f""" CREATE TABLE IF NOT EXISTS mobile(
#     Pair_ID varchar(30),
#     Timestamp varchar(40) NOT NULL,
#     Open float,
#     High float,
#     Low float,
#     Close float,
#     Volume float);
# """)




def create_insert_table(value):
    try:
    
        create_script = """ CREATE TABLE IF NOT EXISTS mobile (
                                Pair_ID varchar(30),
                                Timestamp varchar(40),
                                Open float,
                                High float,
                                Low float,
                                Close float,
                                Volume float
        )
        """

        con.sql(create_script)

        for record in value:
            con.sql(f"""INSERT INTO mobile VALUES {record}""")

        
    except Exception as error:
        print(error)
