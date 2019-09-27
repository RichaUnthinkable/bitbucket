import mysql.connector as mysql

class ConnectionDetails():
   HOST = 'localhost'
   USER = 'hbstudent'
   PASSWORD = 'hbstudent'
   DATABASE = 'contactsDB'


class DBConnection:
   __instance = None

   @classmethod
   def get_connection(cls):
      ins = DBConnection.get_instance()
      if(ins.connection.is_connected() != True):
         ins.connection = mysql.connect(host = ConnectionDetails.HOST, user=ConnectionDetails.USER, passwd=ConnectionDetails.PASSWORD, db=ConnectionDetails.DATABASE)
      return ins.connection

   @staticmethod 
   def get_instance():
      if DBConnection.__instance == None:
         DBConnection()
      return DBConnection.__instance

   def __init__(self):
      if DBConnection.__instance != None:
         raise Exception("This class is a singleton class!")
      else:
         self.connection = mysql.connect(host = ConnectionDetails.HOST, user=ConnectionDetails.USER, passwd=ConnectionDetails.PASSWORD, db=ConnectionDetails.DATABASE)
         DBConnection.__instance = self
   
DBConnection.get_connection()
