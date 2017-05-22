from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

@frappe.whitelist(allow_guest=True)
def point_updator(self, method):
	customer_doc=frappe.get_doc("Customer",self.customer)
	customer_doc.current_point_collected = 0 if not customer_doc.current_point_collected else customer_doc.current_point_collected
	customer_doc.current_point_collected = customer_doc.current_point_collected + self.grand_total_item_point
	customer_doc.save()
	logg=frappe.new_doc("Customer Point Log")
	logg.customer=self.customer
	logg.point=self.grand_total_item_point
	logg.balance_after = customer_doc.current_point_collected
	logg.reference_doc = self.doctype
	logg.reference = self.name
	logg.save()
	# if self.sample_id and (self.docstatus==0):
	# 	# frappe.msgprint("in save"+self.sample_id)
	# 	sample_entry_doc=frappe.get_doc("Sample Entry Register",self.sample_id)
	# 	sample_entry_doc.job_card_status = "Created"
	# 	sample_entry_doc.job_card=self.name
	# 	sample_entry_doc.save()
	# if self.sample_id and (self.docstatus==1):
	# 	# frappe.msgprint("in submit"+self.sample_id)
	# 	sample_entry_doc=frappe.get_doc("Sample Entry Register",self.sample_id)
	# 	sample_entry_doc.job_card_status = "Submitted"
	# 	sample_entry_doc.job_card=self.name
	# 	sample_entry_doc.save()
	# if self.sample_id and (self.docstatus==2):
	# 	# frappe.msgprint("in submit"+self.sample_id)
	# 	sample_entry_doc=frappe.get_doc("Sample Entry Register",self.sample_id)
	# 	sample_entry_doc.job_card_status = "Cancelled			raise Exception			raise Exception			raise Exception"
	# 	sample_entry_doc.job_card=self.name
	# 	sample_entry_doc.save()
	# 	# bill_list = frappe.db.sql("""select name from `tabPurchase Invoice` where bill_no=%s and docstatus =1 and is_recurring='0'""",
	# 		# self.bill_no)

