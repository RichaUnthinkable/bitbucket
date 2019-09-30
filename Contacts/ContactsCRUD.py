from Singleton import DBConnection
import mysql.connector as mysql

from Queries import Queries
from Contact import Contact


class ContactCRUD():
    """
        This is ContactCRUD class. This is DAO Class.
        This class handles all CRUD operations.
    """
    @staticmethod
    def getAllContacts():
        '''
            getAllContacts() method tom fetch All contacts from DB.
            Returns Contacts as list of Objects(Contact)
        '''
        contactList = []
        try:
            con = DBConnection.get_connection() #Getting DB connection 
            cur = con.cursor(dictionary=True)
            if cur != None :
                cur.execute(Queries.ALL)
                for contct in cur:
                    c = Contact()
                    c.id = contct['contact_id']
                    c.name = contct['contact_name']
                    c.address = contct['contact_address']
                    c.contactNumber = contct['contact_number']
                    c.email = contct['contact_email']
                    contactList.append(c)
        except (mysql.Error, mysql.Warning) as e:
            print("error in operation")
            print(e)
        finally:
            con.close()
            return contactList

    @staticmethod
    def search(str):
        query = Queries.SEARCH
        contactList = []
        try:
            con = DBConnection.get_connection()
            cur = con.cursor(dictionary=True)
            data = (str,str,str,str)
            if cur != None :
                cur.execute(query,data)
                for contct in cur:
                    c = Contact()
                    c.id = contct['contact_id']
                    c.name = contct['contact_name']
                    c.address = contct['contact_address']
                    c.contactNumber = contct['contact_number']
                    c.email = contct['contact_email']
                    contactList.append(c)
        except (mysql.Error, mysql.Warning) as e:
            print("error in operation")
            print(e)
        finally:
            con.close()
            return contactList

    @staticmethod
    def insert_contact(contact):
        result = 0
        try:
            con = DBConnection.get_connection()
            cur = con.cursor()
            val = (contact.name,contact.contactNumber,contact.address,contact.email)
            if cur != None :
                cur.execute(Queries.INSERT , val)
                con.commit()
                result = cur.rowcount
        except (mysql.Error, mysql.Warning) as e:
            print("error in operation")
            print(e)
        finally:
            con.close()
            return result
    
    @staticmethod
    def update(contact):
        result = 0
        try:
            con = DBConnection.get_connection()
            cur = con.cursor()
            val = (contact.name,contact.contactNumber,contact.address,contact.email,contact.id)
            if cur != None :
                cur.execute(Queries.UPDATE, val)
                con.commit()
                result = cur.rowcount
        except (mysql.Error, mysql.Warning) as e:
            print("error in operation")
            print(e)
        finally:
            con.close()
            return result

    @staticmethod
    def delete(contact_id):
        result = 0
        try:
            con = DBConnection.get_connection()
            cur = con.cursor()
            if cur != None :
                cur.execute(Queries.DELETE,(int(contact_id),))
                con.commit()
                result = cur.rowcount
        except (mysql.Error, mysql.Warning) as e:
            print("error in operation")
            print(e)
        finally:
            con.close()
            return result
