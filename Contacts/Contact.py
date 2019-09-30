
class Contact():
    def __init__(self):
        self._id = None
        self._name = None
        self._contactNumber = None
        self._address = None
        self._email = None
    
    def __str__(self):
        return "NAME : {}, MOBILE/PHONE : {}, ADDRESS : {}, EMAIL : {}".format(self._name,self._contactNumber,self._address,self._email)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, d):
        if not d: raise Exception("description cannot be empty")
        self._name = d

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, d):
        if not d: raise Exception("Id Cannot be Empty!")
        self._id = d

    @property
    def contactNumber(self):
        return self._contactNumber

    @contactNumber.setter
    def contactNumber(self, d):
        if not d: raise Exception("Contact Number Cannot be Empty!")
        self._contactNumber = d

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, d):
        if not d: raise Exception("Address Cannot Be Empty!")
        self._address = d

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, d):
        if not d: raise Exception("Email Cannot be Empty!")
        self._email = d

