import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    # returns the connection and cursor to sparkifydb
    return cur, conn


def drop_tables(cur, conn):
    # drops each table in the 'drop_table_queries' list
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    #creates each table in the 'creat_table_queries' list
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    # establishes connection to the sparkify database and gets cursor to it
    cur, conn = create_database()
    
    # drops all the tables
    drop_tables(cur, conn)
    
    # creates all required tables
    create_tables(cur, conn)

    # closes the connection
    conn.close()

if __name__ == "__main__":
    main()