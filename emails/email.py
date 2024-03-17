

import frappe



@frappe.whitelist(allow_guest=True)

def send_email(item_code):
    sql_query = """
        SELECT si.name AS invoice_name, si.posting_date AS posting_date
        FROM `tabSales Invoice` AS si
        JOIN `tabSales Invoice Item` AS sii ON si.name = sii.parent
        WHERE sii.item_code = %s
        ORDER BY si.creation DESC
        LIMIT 5
    """
    sales_invoices = frappe.db.sql(sql_query, item_code, as_dict=True)

    # frappe.msgprint(str(sales_invoices))

    email_content = frappe.render_template('emails/templates/sales_invoices_email.html', {
        'item_name': item_code,
        'invoices': sales_invoices,
        
    })


    send_email_to = "shinilshinu97@gmail.com"  
    subject = f'Recent Invoices for Item: {item_code}'
    recipients = [send_email_to] 
    attachments = [frappe.attach_print('Sales Invoice', invoice['invoice_name']) for invoice in sales_invoices]

    try:
        frappe.sendmail(recipients=recipients, subject=subject, message=email_content, attachments=attachments)
        frappe.msgprint("Email sent successfully")
        return True
    except Exception as e:
        frappe.log_error(f"Failed to send email: {e}")
        return False




