from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, getdate, nowdate, now_datetime
from frappe import msgprint, _
from frappe.utils import flt, getdate, nowdate
from datetime import date

class AdjustPointValue(Document):
	def get_details(self):
		dl = frappe.db.sql("""select name,transaction_date,grand_total_item_point,claim_status,claimed_item_point,customer from `tabSales Order` where customer=%s and docstatus=1 and claim_status NOT IN ('Claimed','Expired'); """,(self.customer),as_dict=1, debug=1)

		self.set('adjust_point_value_detail', [])

		for d in dl:
			nl = self.append('adjust_point_value_detail', {})
			nl.sales_order = d.name
			nl.sales_order_date = d.transaction_date
			nl.grand_total_item_point = d.grand_total_item_point
			nl.claim_status = d.claim_status
			nl.allready_claimed_item_point=d.claimed_item_point
			nl.customer = d.customer

	def update_point_value(self):
		sales_order_list = []
		total_claimed_item_point=0
		for d in self.get('adjust_point_value_detail'):
			customer_doc=frappe.get_doc("Customer", d.customer)
			sales_order_doc=frappe.get_doc("Sales Order", d.sales_order)
			if not sales_order_doc.claimed_item_point:
					return
			if (d.grand_total_item_point-sales_order_doc.claimed_item_point) < d.claimed_item_point:
				frappe.throw("Claimed Item Point can not be greator than Grand Total Item Point")
			if d.claim_status=='Claimed' or d.claim_status=='Expired':
				# claimed_point= sales_order_doc.claimed_item_point+d.claimed_item_point
				frappe.db.sql("""update `tabSales Order` set claim_status = %s, claimed_item_point= %s,modified = %s where name=%s and docstatus=1""", (d.claim_status, d.grand_total_item_point, now_datetime(), d.sales_order))
				sales_order_list.append(d.sales_order)
				customer_doc.current_point_collected = customer_doc.current_point_collected-(d.grand_total_item_point-sales_order_doc.claimed_item_point)
				sales_order_doc.claimed_item_point = sales_order_doc.claimed_item_point+d.grand_total_item_point
				customer_doc.save()
			if d.claim_status=='Partial Claimed':
				claimed_point= sales_order_doc.claimed_item_point+d.claimed_item_point
				frappe.db.sql("""update `tabSales Order` set claim_status = %s, claimed_item_point= %s,modified = %s where name=%s and docstatus=1""", (d.claim_status, claimed_point, now_datetime(), d.sales_order))
				sales_order_list.append(d.sales_order)
				if d.claim_status=="Partial Claimed":
					customer_doc.current_point_collected = customer_doc.current_point_collected-d.claimed_item_point
					customer_doc.save()
				if sales_order_doc.grand_total_item_point==sales_order_doc.claimed_item_point:
					sales_order_doc.claim_status="Claimed"
					sales_order_doc.save()
		self.set('adjust_point_value_detail', [])

		if sales_order_list:
			msgprint("Claim Status updated in: {0}".format(", ".join(sales_order_list)))
			msgprint("Remember to create journal entry for point claim")
