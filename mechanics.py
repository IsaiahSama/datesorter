"""Handles all of the mechanics for the date manager"""

from ctypes import Union
from sqlite3 import Row, connect

DBNAME = "mydatedb.sqlite3"

class Database:

    """Class used to manage the connection to the database and related functions
    
    Attrs:
        None
        
    Methods:
        createDB(): Used to create the database if it does not exist with it's needed tables and fields
        getAllEntries(): Retrieves all entries from the database
        setEntry(date:int, event:str): stores a given event and date into the database"""
    
    def __init__(self):
        self.createDB()

    def createDB(self):
        """Method used to create the database."""
        with connect(DBNAME) as db:
            db.execute("""CREATE TABLE IF NOT EXISTS DATETABLE (
                ID INTEGER PRIMARY KEY UNIQUE AUTOINCREMENT,
                DATE INTEGER,
                EVENT TEXT)""")
            db.commit()

    def getAllEntries(self) -> Union[None | list[Row]]:
        """Used to retrieve all of the entires from the database.
        
        Returned format (if exists) is (ID, Date, event)
        Returns:
            None | list[Row]"""

        with connect(DBNAME) as db:
            cursor = db.execute("SELECT * FROM DATETABLE")
        return cursor.fetchall()

    def setEntry(self, date:int, event:str):
        """Method used to store the date and event into the database.
        
        Args:
            date (int): The date of the event
            event (str): The event that happened at date
            
        Returns:
            None"""
        with connect(DBNAME) as db:
            db.execute("INSERT INTO DATETABLE (DATE, EVENT) VALUES (?, ?)", (date, event))
            db.commit()

class InputValidation:
    """Class used to handle input validation.
    
    Attrs:
        None
        
    Methods:
        validateInt(prompt:str): Used to ensure that the user enters a 4 digit integer"""

    def __init__(self):
        pass 

    def validateInt(self, prompt:str) -> int:
        """Method that ensures the user enters a 4 digit integer.
        
        Args:
            prompt (str): The prompt to display the user
            
        Returns:
            int"""
            
        valid = 0
        while not valid:
            result = input(prompt + ": ")
            if not result.isnumeric(): print("Your response must be numeric, not", result)
            elif len(result != 4): print("Your response must be no more or less than 4 digits, not", len(result), "digits")
            else: valid = 1

        return int(result)
