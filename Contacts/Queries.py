class Queries():
    INSERT = "insert into contacts(contact_name,contact_number , contact_address , contact_email) values(%s,%s,%s,%s)"
    SEARCH = """select * from contacts 
                where contact_name LIKE CONCAT('%', %s ,'%') 
                or contact_number LIKE CONCAT('%', %s ,'%') 
                or contact_address LIKE CONCAT('%', %s ,'%') 
                or contact_email LIKE CONCAT('%', %s ,'%')"""
    UPDATE = "update contacts set contact_name = %s , contact_number = %s ,contact_address = %s , contact_email = %s where contact_id = %s"
    DELETE = "delete from contacts where contact_id = %s"
    ALL = "select * from contacts"
    