import frappe

@frappe.whitelist(allow_guest=True)
def get_all_doctype_fields(doctype):
    doctype_name = doctype
    fields = frappe.get_all('DocField', filters={'parent': doctype_name}, fields=["fieldname", "fieldtype", "label","options","idx","reqd","in_list_view","in_filter"])

    field_data = []
    for field in fields:
        field_data.append({
            "fieldname": field['fieldname'],
            "fieldtype": field['fieldtype'],
            "label": field['label'],
            "option": field['options'],
            "idx": field['idx'],
            "reqd": field['reqd'],
            "in_list_view": field['in_list_view'],
            "in_filter": field['in_filter']
        })

    frappe.local.response.update({
        "data": field_data
    })