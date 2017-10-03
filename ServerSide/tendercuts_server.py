SSH Key Password : tendercutsodoo


/opt/odoo/v10/tendercuts/odoo10/odoo/addons,
/opt/odoo/v10/tendercuts/tendercuts-addons
	

/etc/odoo/v10/tendercuts-server.conf

/opt/odoo/v10/tendercuts/odoo10/odoo-bin

DB Password:TendercutsOdoo


host: erp.tendercuts.in
user: ifensys
pass: ifensys!@#$


for http://tendercuts.ifensys-demo.com/
db_pass = Demo10Admin
tail -f /var/log/odoo10-demo/odoo-server.log


for erp.tendercuts.in
sudo service tendercuts-server stop
ps aux | grep python
tail -f /var/log/odoo/tendercuts-server.log

ifensys@erp:/etc/odoo$ cd v10/
ifensys@erp:/etc/odoo/v10$ ls
tendercuts-server.conf
ifensys@erp:/etc/odoo/v10$ cat tendercuts-server.conf
[options]
; This is the password that allows database operations:
admin_passwd =TendercutsOdoo
db_host = False
db_port = False
db_user = tendercutsodoo
db_password = tendercutsodoo
addons_path = /opt/odoo/v10/tendercuts/odoo10/odoo/addons,/opt/odoo/v10/tendercuts/tendercuts-addons

 cat tendercuts-server.conf
  368  psql -d tendercuts0701 -U tendercutsodoo
  369  psql -d tendercuts0701 -U tendercutsodoo
  370  psql -d tendercuts0701 -U tendercutsodoo

  Export psql table in csv file:

  COPY product_product TO '/home/susai/Desktop/product_product.csv' CSV HEADER;

  COPY product_product TO '/home/susai/Desktop/product_product.csv' DELIMITER ',' CSV HEADER;

  COPY (SELECT id,product_tmpl_id FROM product_product) TO '/home/susai/Desktop/Test/product_product1.csv' DELIMITER ',' CSV HEADER;
  
 Credentials::
 Uname = varun
 Password = +Zv)PU=j93PAwm9o

https://tendercuts.in/console



New Server:::

Please find the FTP details for the new server.

FTP:
Host: ifensys-demo.com
ip : 23.254.42.66
Port: 22
Username: odoo
Password: Odoo@iFS
Addons Path: /home/odoo

Note:
1) Custom Module: You can find respective folder for each project. Please upload only custom addons to the project folder.

2) Community Module: If there is any community module (downloaded from odoo apps, etc.,) to be used for any project, upload it to /home/odoo/community-addons/9.0 or /10.0


This is the password that allows database operations:admin_passwd = Demo10Admin
# Database configuration
db_host = localhostdb_port = False
db_user = odoo10
db_password = odoo10
# Logging
logfile = /var/log/odoo10/odoo-server.log
# Ports to use
xmlrpc_port = 3069
netrpc_port = 3070# 
Custom Addonsaddons_path = /opt/odoo10/addons,/home/odoo/odoo-addons,/home/odoo/pharmsol-addons,/home/odoo/shc-addons,/home/odoo/tendercuts-addons,/home/odoo/vishoes-addons,/home/odoo/zone-addons,/home/odoo/metro-addons,/home/odoo/community-addons/10.0# DB filtering for multi-site instancesdbfilter=^%d


#SMI
http://test.smart-inventory.co.uk
Username : admin
Password : powster33