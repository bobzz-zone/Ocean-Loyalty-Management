# -*- coding: utf-8 -*-
# Copyright (c) 2015, sbk and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, getdate, nowdate, now_datetime
from frappe import msgprint, _
from frappe.utils import flt, getdate, nowdate
from datetime import date

class AdjustPoint(Document):
	
	def get_point(self):

		if self.customer :
			customer = frappe.get_doc("Customer", self.customer)
			get_point = customer.total_point

			self.set('total_point', get_point)

		else :
			frappe.throw("Silahkan pilih customer terlebih dahulu")


	def validate(self):
		self.check_claim_point()

	def on_submit(self):
		self.reduce_point_from_customer()

	def on_cancel(self):
		self.add_point_to_customer()


	def check_claim_point(self):
		if self.claim_point :
			if self.claim_point > self.total_point :
				frappe.throw("Claim Point lebih besar daripada Total Point yang dimiliki oleh Customer "+str(self.customer))
		else :
			frappe.throw("Claim Point belum diisi")

	def reduce_point_from_customer(self):
		customer = frappe.get_doc("Customer",self.customer)
		current_point = customer.total_point
		point_after_reduce = 0
		
			
		point_after_reduce = current_point - self.claim_point
		customer.update({
			"total_point": point_after_reduce	
		})
		customer.flags.ignore_permissions = 1
		customer.save()

		logg=frappe.new_doc("Customer Point Log")
		logg.customer=self.customer
		logg.point=self.claim_point * -1
		logg.balance_after = point_after_reduce
		logg.reference_doc = "Adjust Point"
		logg.reference = self.name
		logg.save()

	def add_point_to_customer(self):
		customer = frappe.get_doc("Customer",self.customer)
		current_point = customer.total_point
		point_after_reduce = 0
		
		point_after_reduce = current_point + self.claim_point
		customer.update({
			"total_point": point_after_reduce	
		})
		customer.flags.ignore_permissions = 1
		customer.save()
		logg=frappe.new_doc("Customer Point Log")
		logg.customer=self.customer
		logg.point=self.claim_point
		logg.balance_after = point_after_reduce
		logg.reference_doc = "Adjust Point"
		logg.reference = self.name
		logg.save()

		

