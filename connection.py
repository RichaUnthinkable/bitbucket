

hostname = 'localhost'
username = 'hbstudent'
password = 'hbstudent'
database = 'contactsDB'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()
    str =  "insert into contacts(conatact_name,contact_number , contact_address , contact_email) values('richa' , '8765456789','iuyfgcvhbjkl' , 'richa@abc.com')"
    cur.execute(str)

print("Using mysql.connector…")
import mysql.connector
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
print(doQuery(myConnection))
print(myConnection)
myConnection.close()
