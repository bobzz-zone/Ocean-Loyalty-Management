from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Coupon",
					"description": _("All Coupon"),
				},
				{
					"type": "doctype",
					"name": "Point List",
					"description": _("To Make Point List"),
				},
				{
					"type": "doctype",
					"name": "Item Point",
					"description": _("To Set Item Point"),
				},
			]
		},
		{
			"label": _("Tools"),
			"icon": "icon-star",
			"items": [
				
				{
					"type": "doctype",
					"name": "Adjust Point",
					"description": _("Adjust Point"),
				},
				{
					"type": "doctype",
					"name": "Cash Coupon Tool",
					"description": _("Create coupons in bulk"),
				},
			]
		},
                {
                       "label": _("Setup"),
                       "icon": "icon-star",
                       "items": [
                               {
                                         "type": "doctype",
                                         "name": "Master Promo",
                                         "description": _("Set Promo Code"),
                                },  
	                 ]
                 },         
         ]                                    
