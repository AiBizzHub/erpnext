# Copyright (c) 2020, AiBizzHub LLC. and contributors
# For license information, please see license.txt


# import frappe
from frappe.model.document import Document


class IncomingCallHandlingSchedule(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		agent_group: DF.Link
		day_of_week: DF.Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
		from_time: DF.Time
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		to_time: DF.Time
	# end: auto-generated types

	pass