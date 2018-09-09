import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
# CREATE TABLE IF NOT EXISTS game_data (
#  id integer PRIMARY KEY,
#  player_id integer NOT NULL,
#  your_distance_to_end integer,
#  opp_distance integer,
#  walls_left integer,
#  diff_walls integer,
#  best_wall integer,
#  worst_wall integer,
#  move text,
#  block integer,
# );
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
def main():
    database = "C:\\sqlite\quoridor.db"
 
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS gamedata (
                                        id integer PRIMARY KEY,
                                        playerId integer NOT NULL,
                                        your_distance_to_end integer,
                                        opp_distance integer,
                                        walls_left integer,
                                        diff_walls integer,
                                        best_wall integer,
                                        worst_wall integer,
                                        move text,
                                        block integer
                                    ); """
 
    # sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS game_data (
    #                                         id integer PRIMARY KEY,
    #                                         player_id integer NOT NULL,
    #                                         your_distance_to_end integer,
    #                                         opp_distance integer,
    #                                         walls_left integer,
    #                                         diff_walls integer,
    #                                         best_wall integer,
    #                                         worst_wall integer,
    #                                         move text,
    #                                         block integer,
    #                                     ); """
 
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
       
    else:
        print("Error! cannot create the database connection.")
    database = "C:\\sqlite\quoridor2.db"
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
       
    else:
        print("Error! cannot create the database connection.")
    database = "C:\\sqlite\quoridor3.db"
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
       
    else:
        print("Error! cannot create the database connection.")
    database = "C:\\sqlite\quoridor4.db"
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
       
    else:
        print("Error! cannot create the database connection.")
    database = "C:\\sqlite\quoridor5.db"
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
       
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()