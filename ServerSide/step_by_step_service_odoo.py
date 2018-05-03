Copying the odoo server file into etc:

cp /opt/Source/Neon\ Workspace/Confic_Files/openerp-server_odoo_10.cfg /etc/odoo-server.cfg

vi /etc/odoo-server.cfg

AND PAST THIS
########################
[options]
; This is the password that allows database operations:
;admin_passwd = admin
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo
addons_path = /opt/Source/odoo-11.0/addons
logfile = /var/log/odoo/odoo11-server.log

xmlrpc_port = 8099
netrpc_port = 8070
########################

create service file:::
touch /lib/systemd/system/odoo-server.service

vi odoo-server.service

AND PAST THIS
########################
[Unit]
Description=Odoo Open Source ERP and CRM
Requires=postgresql.service
After=network.target postgresql.service

[Service]
Type=simple
PermissionsStartOnly=true
SyslogIdentifier=odoo11-server
User=odoo
Group=odoo
ExecStart=/opt/Source/odoo-11.0/odoo-bin --config /etc/odoo11-server.conf --logfile /var/log/odoo/odoo11-server.log
KillMode=mixed

[Install]
WantedBy=multi-user.target
##########################################
systemctl daemon-reload

sudo systemctl start odoo-server

sudo systemctl status odoo-server


Nginx mapping Step by step::

cd /etc/nginx/sites-available/
vim odoo-custom.co.conf
AND PAST THIS:
#############################
#odoo server
upstream mysite {
 server 127.0.0.1:8099;
}

server {
 listen 80;
 server_name odoo11.com www.odoo11.com;
 proxy_read_timeout 720s;
 proxy_connect_timeout 720s;
 proxy_send_timeout 720s;

 # Add Headers for odoo proxy mode
 proxy_set_header X-Forwarded-Host $host;
 proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
 proxy_set_header X-Forwarded-Proto $scheme;
 proxy_set_header X-Real-IP $remote_addr;

 # log
 access_log /var/log/nginx/odoo11.com.access.log;
 error_log /var/log/nginx/odoo11.com.error.log;

 # Redirect requests to odoo backend server
 location / {
   proxy_redirect off;
   proxy_pass http://mysite;
 }

}
#####################################

vi /etc/hosts

AND ADD THIS:
###############
127.0.1.1       odoo11.com
127.0.1.1       www.odoo11.com
################
sudo ln -s /etc/nginx/sites-available/odoo11.com.conf /etc/nginx/sites-enabled/

sudo nginx -t






