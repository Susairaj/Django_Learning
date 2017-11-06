import odoorpc
class get_odoo_instance():
    odoo = odoorpc.ODOO('localhost', port=8069)
    odoo.login('atkg', 'admin', 'admin')
