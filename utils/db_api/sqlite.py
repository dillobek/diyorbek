import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            username varchar(255),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)


    def create_table_courses(self):
        sql = """
        CREATE TABLE Courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            name varchar (255) NOT NULL,
            description text NOT NULL,
            video varchar (255) NOT NULL
            );
"""
        self.execute(sql, commit=True)

    def create_table_social(self):
        sql="""
        CREATE TABLE Books (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        name varchar(255) NOT NULL,
        description varchar (255) NOT NULL,
        pdf varchar (255) NOT NULL
        );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self,id:int, name: str, username: str):

        sql = """
        INSERT INTO Users(id, Name, username) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, username), commit=True)

    def add_course(self, name:str, description:str, video:str):
        sql = """
            INSERT INTO Courses (name, description, video) VALUES (?, ?, ?)
        """
        self.execute(sql, parameters=(name, description, video), commit=True)


    def add_books (self, name:str, description:str, pdf:str):
        sql = """
        INSERT INTO Books (name, description, pdf) VALUES (?, ?, ?)
        """
        self.execute(sql, parameters=(name, description, pdf), commit=True)


    def get_all_course(self):
        sql = """
            SELECT * FROM Courses
            """
        return self.execute(sql, fetchall=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)


    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)



    def get_videos(self):
        return self.execute("SELECT * FROM Courses WHERE TRUE", fetchall=True)

    def get_video(self, id):
        return self.execute("SELECT * FROM Courses WHERE id=?", (id,), fetchone=True)

    def delete_course(self, id):
        return self.execute("DELETE FROM Courses WHERE id=?", (id,), commit=True)

    def get_pdfs(self):
        return self.execute("SELECT * FROM Books WHERE TRUE", fetchall=True)

    def get_pdf(self, id):
        return self.execute("SELECT * FROM Books WHERE id=?", (id,), fetchone=True)

    def delete_pdf(self, id):
        return self.execute("DELETE FROM Books WHERE id=?", (id,), commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
