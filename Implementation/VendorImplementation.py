from Abstractions.Vendor import Vendor
from Models.VendorModel import VendorModel
from Models.VendorSessionModel import VendorSessionModel


class VendorImplementation(Vendor):

    def __init__(self):
        self.vendor_model = VendorModel()
        self.vendor_session = VendorSessionModel()

    def login(self, username, password):
        # Add you code here after verifying the vendor data exists in the dictionary 
        if username in self.vendor_model.login_data:
            if(self.vendor_model.login_data[username] == password):
                self.vendor_session.login(username)
        else:
            return False

    def logout(self, username):
        # Add your code here to log out the current vendor
        if (self.vendor_session.check_login(username)):
            self.vendor_session.logout(username)

        else:
            return False
