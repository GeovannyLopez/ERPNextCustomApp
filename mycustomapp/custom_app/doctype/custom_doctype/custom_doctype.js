// Copyright (c) 2019, Oscar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Custom DocType', {
	refresh: function(frm) {
		frappe.show_alert({
			indicator: 'red',
			message: __('HOLA MUNDO!')
		});
	}
});
