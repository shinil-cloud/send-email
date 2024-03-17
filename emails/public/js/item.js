frappe.ui.form.on('Item',{

    refresh(frm)
    {
        frm.add_custom_button(__("Send Email"),function()
        {
            frappe.call({
                method: 'emails.email.send_email',
                args: {
                    item_code: frm.doc.name
                },
                
            });

        },"Actions")
    },
})