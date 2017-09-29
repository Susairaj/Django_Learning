For enableing the sites:


ln -s /etc/nginx/sites-available/odoo.mysite.co.conf /etc/nginx/sites-enabled/
  170  nginx -t

systemctl restart nginx