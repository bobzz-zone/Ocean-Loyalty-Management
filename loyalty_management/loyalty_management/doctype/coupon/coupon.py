# -*- coding: utf-8 -*-
# Copyright (c) 2015, sbk and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Coupon(Document):
	def on_submit(self):
		# cost_center = frappe.db.get_value("Company", ref_doc.company, "cost_center")
		if self.date_of_issue and self.company and self.is_bulk==0:
			company_abbr = frappe.db.get_value("Company", self.company, "abbr")
			doc_jv_creation=frappe.new_doc("Journal Entry")
			# doc_jv_creation.standards = r.get("standard")
			doc_jv_creation.posting_date=self.date_of_issue
			doc_jv_creation.append("accounts", {
			"account": "Cash Coupon Owe - "+company_abbr,
			"cost_center": self.cost_center,
			"credit_in_account_currency": self.coupon_value,
			})
			doc_jv_creation.append("accounts", {
			"account": "Cash Coupon - "+company_abbr,
			"cost_center": self.cost_center,
			"debit_in_account_currency": self.coupon_value,
			})
			doc_jv_creation.save()
			doc_jv_creation.user_remark=self.name
			doc_jv_creation.submit()
			frappe.msgprint(doc_jv_creation.name+" is Submited")

	# def get_payment_entry(ref_doc, args):
	# cost_center = frappe.db.get_value("Company", ref_doc.company, "cost_center")
	# exchange_rate = get_exchange_rate(args.get("party_account"), args.get("party_account_currency"),
	# 	ref_doc.company, ref_doc.doctype, ref_doc.name)

	# jv = frappe.new_doc("Journal Entry")
	# jv.update({
	# 	"voucher_type": "Bank Entry",
	# 	"company": ref_doc.company,
	# 	"remark": args.get("remarks")
	# })