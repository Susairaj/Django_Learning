import odoorpc
class get_odoo_instance():
    odoo = odoorpc.ODOO('tendercuts.ifensys-demo.com', port=80)
    odoo.login('tendercuts_pos', 'admin', 'tendercuts123')
