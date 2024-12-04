# Copyright (c) 2018, AiBizzHub LLC. and contributors
# For license information, please see license.txt


from frappe.model.document import Document


class AllowedToTransactWith(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		company: DF.Link
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types

	pass