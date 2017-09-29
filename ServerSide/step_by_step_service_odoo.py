Copying the odoo server file into etc:

cp /opt/Source/Neon\ Workspace/Confic_Files/openerp-server_odoo_10.cfg /etc/odoo-server.cfg

vi /etc/odoo-server.cfg

create service file:::
touch /lib/systemd/system/odoo-server.service

vi odoo-server.service

systemctl daemon-reload

sudo systemctl start odoo-server

sudo systemctl status odoo-server


Nginx mapping Step by step::

cd /etc/nginx/sites-available/
vim odoo-custom.co.conf

vi /etc/hosts


