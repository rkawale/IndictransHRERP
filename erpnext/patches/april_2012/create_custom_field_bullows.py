field_list = [
['Customer', 'customer_code'],
['Customer', 'address_of_consignee'],
['Customer', 'tin_no'],
['Customer', 'cst_no'],
['Customer', 'consignee_ec_code'],
['Customer', 'consignee_sales_tax_no'],
['Customer', 'ecc_no'],
['Customer', 'location_detail'],
['Delivery Note', 'is_billable'],
['Delivery Note', 'pin_code'],
['Delivery Note', 'address_of_consignee'],
['Delivery Note', 'location_code'],
['Delivery Note', 'your_order_number'],
['Delivery Note', 'so_number'],
['Delivery Note', 'insurance'],
['Delivery Note', 'branch'],
['Delivery Note', 'freight'],
['Delivery Note', 'ecc_no'],
['Delivery Note', 'cst_no'],
['Delivery Note', 'tin_no'],
['Delivery Note', 'special_instructions'],
['Delivery Note', 'payment_terms'],
['Delivery Note', 'consignee_ec_code'],
['Delivery Note', 'consignee_sales_tax_no'],
['Delivery Note', 'excise_amount_in_words'],
['Delivery Note', 'consignee_name'],
['Delivery Note', 'vendor_code'],
['Delivery Note Detail', 'category'],
['Delivery Note Detail', 'sale_type'],
['Delivery Note Detail', 'rt_code'],
['DocType Mapper', 'sales_type'],
['Indent', 'estimated_miscellaneous_item_cost'],
['Indent', 'project_name'],
['Indent Detail', 'estimated_miscellaneous_item_cost'],
['Indent Detail', 'material'],
['Indent Detail', 'technical_specification'],
['Indent Detail', 'weight_per_unit'],
['Indent Detail', 'source_of_supply'],
['Indent Detail', 'drawing_size'],
['Indent Detail', 'total_surface_area_both_sides'],
['Indent Detail', 'remark'],
['Indent Detail', 'estimated_cost'],
['Indent Detail', 'prefered_make'],
['Indent Detail', 'presales_quotation_ref'],
['Indent Detail', 'presales_qutation_value'],
['Item', 'drawing_number'],
['Item', 'source_of_supply'],
['Item', 'chapter_id'],
['Item', 'matgrpcomm'],
['Item Group', 'show_in_catalogue'],
['Journal Voucher Detail', 'foxpro_ref'],
['Journal Voucher Detail', 'due_date'],
['Journal Voucher Detail', 'remark'],
['Leave Control Panel', 'date'],
['PO Detail', 'indent_number'],
['PO Detail', 'indent_date'],
['PO Detail', 'disc_per'],
['PO Detail', 'is_scrapped_item'],
['PO Detail', 'list_price'],
['PO Detail', 'excise_benifit_amount'],
['PO Detail', 'diff'],
['Project', 'completion_date_for_delivery'],
['Project', 'completion_date_for_ere_n_comm'],
['Project', 'offer_number'],
['Project', 'estimated_cost_bo'],
['Project', 'sales_person'],
['Project', 'total_estimated_cost'],
['Project', 'additional_excise_amt'],
['Project Milestone', 'start_date'],
['Project Milestone', 'end_date'],
['Project Milestone', 'milestone_start_date'],
['Project Milestone', 'milestone_end_date'],
['Purchase Order', 'transport'],
['Purchase Order', 'estimated_cost'],
['Purchase Order', 'test_certificate_required'],
['Purchase Order', 'vendor_reference'],
['Purchase Order', 'octroi'],
['Purchase Order', 'mode_of_dispatch'],
['Purchase Order', 'transportation_required'],
['Purchase Order', 'header_indent_no'],
['Purchase Order', 'header_indent_date'],
['Purchase Order', 'inspection'],
['Purchase Order', 'delivery_schedule'],
['Purchase Order', 'originated_by'],
['Purchase Order', 'insurance'],
['Purchase Receipt', 'incoming_qty_in_kgs'],
['Purchase Receipt', 'approved'],
['Purchase Receipt', 'against_rc_1'],
['Purchase Receipt', 'against_rc_2'],
['Purchase Receipt', 'against_rc_3'],
['Purchase Receipt', 'transaction_date'],
['Purchase Receipt Detail', 'list_price'],
['Purchase Receipt Detail', 'disc_per'],
['Receivable Voucher', 'category'],
['Receivable Voucher', 'is_billable'],
['Receivable Voucher', 'sale_type'],
['Receivable Voucher', 'so_number'],
['Receivable Voucher', 'address_of_consignee'],
['Receivable Voucher', 'your_order_number'],
['Receivable Voucher', 'name_of_excisable_goods'],
['Receivable Voucher', 'cst_no'],
['Receivable Voucher', 'tin_no'],
['Receivable Voucher', 'consignee_ec_code'],
['Receivable Voucher', 'ecc_no'],
['Receivable Voucher', 'excise_amount_in_words'],
['Receivable Voucher', 'payment_terms'],
['Receivable Voucher', 'consignee_sales_tax_no'],
['Receivable Voucher', 'consignee_name'],
['Receivable Voucher', 'excise_amount'],
['RV Detail', 'chapter_id'],
['RV Detail', 'sale_type'],
['RV Tax Detail', 'is_excise_account'],
['Sales Order', 'vendor_code'],
['Sales Order', 'estimated_cost'],
['Sales Order', 'is_billable'],
['Sales Order', 'against_form'],
['Sales Order', 'order_category'],
['Sales Order', 'pin_code'],
['Sales Order', 'offer_number'],
['Sales Order', 'inspection'],
['Sales Order', 'freight'],
['Sales Order', 'insurance'],
['Sales Order', 'special_instructions'],
['Sales Order', 'mode_of_dispatch'],
['Sales Order', 'branch'],
['Sales Order', 'address_of_consignee'],
['Sales Order', 'so_number'],
['Sales Order', 'payment_terms'],
['Sales Order', 'location_code'],
['Sales Order', 'your_order_number'],
['Sales Order', 'name_of_excisable_goods'],
['Sales Order', 'consignee_sales_tax_no'],
['Sales Order', 'tin_no'],
['Sales Order', 'consignee_ec_code'],
['Sales Order', 'cst_no'],
['Sales Order', 'ecc_no'],
['Sales Order', 'excise_amount_in_words'],
['Sales Order', 'authorised_signatory'],
['Sales Order', 'consignee_name'],
['Sales Order', 'c_form_applicable'],
['Sales Order Detail', 'billed_qty'],
['Sales Order Detail', 'category'],
['Sales Order Detail', 'sale_type'],
['Sales Order Detail', 'rt_code'],
['Stock Entry', 'supplier_code'],
['Stock Entry', 'po_number_and__date'],
['Stock Entry', 'memo_no_and_date'],
['Stock Entry', 'indent_no_and_date'],
['Stock Entry', 'mode_of_dispatch'],
['Stock Entry', 'special_instruction'],
['Stock Entry', 'invoice_ref_1'],
['Stock Entry', 'invoice_ref_2'],
['Stock Entry', 'invoice_ref_3'],
['Stock Entry', 'invoice_ref_4'],
['Stock Entry', 'invoice_ref_5'],
['Stock Entry', 'invoice_ref_date_1'],
['Stock Entry', 'invoice_ref_date_2'],
['Stock Entry', 'invoice_ref_date_3'],
['Stock Entry', 'invoice_ref_date_4'],
['Stock Entry', 'invoice_ref_date_5'],
['Stock Entry', 'approved'],
['Supplier', 'supplier_code'],
['Supplier', 'pan_no'],
['Ticket', 'reason'],
['Ticket', 'document_num'],
['Ticket', 'ticket_by'],
['Ticket', 'ticket_by_email'],
['Warehouse', 'country'],
]


import webnotes
from webnotes.model.code import get_obj
from webnotes.model.doc import Document

def execute():
	import webnotes.model.sync
	webnotes.model.sync.sync('core', 'custom_field')	
	for f in field_list:
		res = webnotes.conn.sql("""SELECT name FROM `tabCustom Field`
				WHERE dt=%s AND fieldname=%s""", (f[0], f[1]))
		if res: continue
		docfield = webnotes.conn.sql("""SELECT * FROM `tabDocField`
			WHERE parent=%s AND fieldname=%s""", (f[0], f[1]), as_dict=1)
		if not docfield: continue
		custom_field = docfield[0]

		# scrub custom field dict
		custom_field['dt'] = custom_field['parent']
		del custom_field['parent']
		
		d = Document('Custom Field', fielddata=custom_field)
		d.name = custom_field['dt'] + '-' + custom_field['fieldname']
		d.save(1, ignore_fields=1)