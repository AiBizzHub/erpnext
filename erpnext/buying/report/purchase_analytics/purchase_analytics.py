# Copyright (c) 2013, AiBizzHub LLC. and contributors
# For license information, please see license.txt


from erpnext.selling.report.sales_analytics.sales_analytics import Analytics


def execute(filters=None):
	return Analytics(filters).run()
