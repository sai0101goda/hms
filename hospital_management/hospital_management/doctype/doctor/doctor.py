# # Copyright (c) 2024, gopichand and contributors
# # For license information, please see license.txt


import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname  

class Doctor(Document):
    def autoname(self):
        self.name = make_autoname("DOC-.######")

    def before_save(self):
        self.create_user()

    def create_user(self):
        if not frappe.db.exists("User", self.email):
            user = frappe.get_doc({
                "doctype": "User",
                "email": self.email,
                "first_name": self.doctor_name,
                "mobile_no": self.mobile_no,
                "enabled": 1            })
            user.insert(ignore_permissions=True)
            frappe.msgprint(f"User {self.email} created successfully!")

            self.db_set("linked_user", user.name)
        else:
            frappe.msgprint(f"User with email {self.email} already exists.")

