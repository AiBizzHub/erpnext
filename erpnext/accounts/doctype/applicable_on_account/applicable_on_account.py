# Copyright (c) 2020, AiBizzHub LLC. and contributors
# For license information, please see license.txt


# import frappe
from frappe.model.document import Document


class ApplicableOnAccount(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		applicable_on_account: DF.Link
		is_mandatory: DF.Check
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types

	pass
