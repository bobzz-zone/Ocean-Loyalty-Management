# -*- coding: utf-8 -*-
# Copyright (c) 2015, Myme and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class custom_method(Document):
	pass


@frappe.whitelist()
def get_item_point(item_code, point_list):
	
	array_temp = []

	get_item_point = frappe.db.sql("""
		SELECT
		di.`point_value`,
		di.`min_qty`
		FROM `tabItem Point` di
		WHERE di.`item_code` = "{}"
		AND di.`point_list` = "{}"

		""".format(item_code, point_list))

	if get_item_point :
		array_temp.append(str(get_item_point[0][0]))
		array_temp.append(str(get_item_point[0][1]))

	else :
		array_temp.append(str(0))
		array_temp.append(str(0))

	return array_temp


