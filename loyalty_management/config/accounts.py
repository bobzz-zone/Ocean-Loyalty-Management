from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Tools"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Adjust Point Value",
					"description": _("Adjust Point Value"),
				},
			]
		},
	]
