frappe.ui.form.on("Cash Coupon Tool", {
	refresh: function(frm) {
		frm.disable_save();
	},
	
	// update_clearance_date: function(frm) {
	// 	return frappe.call({
	// 		method: "update_details",
	// 		doc: frm.doc
	// 	});
	// },
	// create_sample_entry: function(frm){
	// 	return frappe.call({
	// 		method: "create_sample_entry",
	// 		doc: frm.doc,
	// 		callback: function(r, rt){
	// 			frm.refresh()
	// 		}
	// 	})
	// },
	// update_sample_entry: function(frm){
	// 	return frappe.call({
	// 		method: "update_sample_entry",
	// 		doc: frm.doc,
	// 		callback: function(r, rt){
	// 			frm.refresh()
	// 		}
	// 	})
	// },
	// get_relevant_entries: function(frm) {
	// 	return frappe.call({
	// 		method: "get_details",
	// 		doc: frm.doc,
	// 		callback: function(r, rt) {
	// 			frm.refresh()
	// 		}
	// 	});
	// },
	get_relevant_entries: function(frm) {
		return frappe.call({
			method: "get_details",
			doc: frm.doc,
			callback: function(r, rt) {
				frm.refresh()
			}
		});
	},
	create_coupons: function(frm) {
		return frappe.call({
			method: "create_coupons",
			doc: frm.doc,
			callback: function(r, rt) {
				frm.refresh()
			}
		});
	},
	// date_of_receipt: function(frm){
	// 	cur_frm.set_value("from_date", frm.doc.date_of_receipt);
	// 	cur_frm.set_value("to_date", frm.doc.date_of_receipt);
	// 	cur_frm.set_value("filter_based_on_date_of_receipt", 1);
		
	// },
	// to_date: function(frm){
	// 	cur_frm.set_value("filter_based_on_date_of_receipt", 1);
		
	// }
});