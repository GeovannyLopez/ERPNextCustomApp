# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Custom App",
			"color": "#5DADE2",
			"icon": "octicon octicon-database",
			"type": "module",
			"label": _("Custom App")
		}
	]
