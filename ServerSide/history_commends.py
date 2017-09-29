 1002  sudo alsa force-reload
 1003  sudo add-apt-repository ppa:ubuntu-audio-dev
 1004  sudo apt-get update
 1005  sudo apt-get dist-upgrade
 1006  sudo gedit /etc/default/speech-dispatcher
 1007  sudo apt-get install indicator-sound
 1008  killall unity-panel-service
 1009  killall gnome-panel
 1010  sudo apt-get install indicator-sound
 1011  sudo apt-get install evolution-indicator
 1012  sudo add-apt-repository ppa:ubuntu-audio-dev/ppa; sudo apt-get update;sudo apt-get dist-upgrade; sudo apt-get install linux-sound-base alsa-base alsa-utils gdm ubuntu-desktop linux-image-`uname r` libasound2; sudo apt-get -y --reinstall install linux-sound-base alsa-base alsa-utils gdm ubuntu-desktop linux-image`uname -r` libasound2; killall pulseaudio; rm -r ~/.pulse*; sudo usermod -aG `cat /etc/group | grep -e '^pulse:' -e '^audio:' -e '^pulse-access:' -e '^pulse-rt:' -e '^video:' | awk -F: '{print $1}' | tr '\n' ',' | sed 's:,$::g'` `whoami`
 1013  sudo aplay -l
 1014  sudo setfacl -m u:susai:rw /dev/snd/*
 1015  gpasswd -a [susai] audio
 1016  gpasswd -a [user] audio
 1017  usermod -a -G audio <susai>
 1018  echo "Sound cards recognized by the system:"; lspci -nn | grep --color=none '\[04[80][13]\]'; echo "Sound cards recognized by ALSA:"; lspci -nn | grep '\[04[80][13]\]' | while read line; do lspci -nnk | grep -A 3 '\[04[80][13]\]' | grep -e 'Kernel modules: ..*' -e '\[04[80][13]\]' | grep --color=none -F "$line"; done; echo "Sound cards recognized by ALSA, and activated:"; lspci -nn | grep '\[04[80][13]\]' | while read line; do lspci -nnk | grep -A 3 '\[04[80][13]\]' | grep -e 'Kernel drivers in use: ..*' -e '\[04[80][13]\]' | grep --color=none -F "$line"; done
 1019  sudo alsa force-reload
 1020  ls -l /dev/snd
 1021  sudo alsa unload
 1022  sudo find / -name alsa
 1023  sudo alsa force-reload
 1024  $ sudo aptitude --purge reinstall linux-sound-base alsa-base alsa-utils linux-image-`uname -r` linux-ubuntu-modules-`uname -r` libasound2
 1025  $ sudo aptitude --purge reinstall linux-sound-base alsa-base alsa-utils linux-image-`susai -r` linux-ubuntu-modules-`susai -r` libasound2
 1026  $ sudo aptitude --purge reinstall linux-sound-base alsa-base alsa-utils linux-image-`uname -r` linux-ubuntu-modules-`uname -r` libasound2
 1027  $ sudo aptitude --purge reinstall linux-sound-base alsa-base alsa-utils
 1028  cd /tmp; wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.3-unstable/linux-headers-4.3.0-040300-generic_4.3.0-040300.201511020846_amd64.deb http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.3-unstable/linux-headers-4.3.0-040300_4.3.0-040300.201511020846_all.deb http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.3-unstable/linux-image-4.3.0-040300-generic_4.3.0-040300.201511020846_amd64.deb; sudo dpkg -i *.deb
 1029  history
 1030  d ~/
 1031  wget http://www.alsa-project.org/alsa-info.sh -O alsa-info.sh && bash alsa-info.sh
 1032  wget http://www.alsa-project.org/db/?f=ffb922d6246a2f791e7b5d22e150e9b5ab09b439
 1033  cat /proc/asound/card0/codec* | grep Codec
 1034  sudo nano
 1035  sudo alsa force-reload
 1036  lshw
 1037  $ sudo aptitude --purge reinstall linux-sound-base alsa-base alsa-utils linux-image-`uname -r` linux-ubuntu-modules-`uname -r` libasound2
 1038  sudo aptitude --purge reinstall linux-sound-base alsa-base alsa-utils linux-image-`uname -r` linux-ubuntu-modules-`uname -r` libasound2
 1039  sudo alsa force-reload
 1040  history
 1041  pavucontrol
 1042  sudo apt-get remove --purge alsa-base pulseaudio
 1043  sudo apt-get install alsa-base pulseaudio
 1044  sudo aptitude --purge reinstall linux-sound-base alsa-base alsa-utils linux-image-`uname -r` linux-ubuntu-modules-`uname -r` libasound2
 1045  sudo alsa force-reload
 1046  sudo apt-get update
 1047  inxi -Fx
 1048  inxi -A
 1049  sudo alsamixer
 1050  lspci
 1051  sudo update-grub
 1052  lshw -C sound
 1053  sudo su
 1054  sh screen_resolution_fix
 1055  lspci -nnk | grep VGA -A 12
 1056  xrandr
 1057  gksudo gedit /etc/modprobe.d/alsa-base.conf
 1058  sudo apt-get remove --purge alsa
 1059  sudo apt-get install pavucontrol
 1060  gksu pavucontrol
 1061  xrandr --newmode "1280x768_60.00"   79.50  1280 1344 1472 1664  768 771 781 798 -hsync +vsync
 1062  xrandr --addmode VGA1 1280x768_60.00
 1063  software-properties-gtk
 1064  sudo apt-get remove nvidia*
 1065  sudo apt install nvidia-361
 1066  sudo apt-get install gksu
 1067  arch
 1068  cd Downloads && tar xvzf ~/Downloads/sis64.tar.gz
 1069  sudo mv -v ~/Downloads/sisimedia_drv.* /usr/lib/xorg/modules/drivers
 1070  lspci | grep -i vga
 1071  sudo apt-get update
 1072  sudo apt-get upgrade
 1073  sudo apt-get install ubuntu-desktop
 1074  sudo apt-get install vnc4server
 1075  sh screen_resolution_fix
 1076  xrandr
 1077  xrandr --output VGA
 1078  xrandr --output default
 1079  xrandr --output VGA1 --rate 60 --mode 800x600 --fb 1280x1024 --panning 1280x1024
 1080  :
 1081  xrandr --output LVDS1 --off --output VGA1 --mode 1920x1200
 1082  chmod 777 out_source/
 1083  ce custom_product/
 1084  cd custom_product/
 1085  ls
 1086  sudo smbl __openerp__.py
 1087  sudo subl __openerp__.py
 1088  ssh bosco@192.168.1.159
 1089  cd ..
 1090  sudo cp custom_product /opt/Source/PycharmWorkspace/odoo-9.0c-20170301/out_source
 1091  sudo mv  custom_product /opt/Source/PycharmWorkspace/odoo-9.0c-20170301/out_source
 1092  apt-get install libjpeg-dev
 1093  rm /var/lib/dpkg/lock
 1094  sudo rm /var/lib/dpkg/lock
 1095  apt-get install libjpeg-dev
 1096  sudo su
 1097  aria2c John\ Wick-\ Chapter\ 2\ \(2017\)\ \[720p\]\ \[YTS.AG\].torrent
 1098  sudo python setup.py install
 1099  sudo pip install holovies
 1100  sudo pip install holoviews
 1101  sudo pip install geoviews
 1102  sudo pip install cartopy
 1103  ls -a
 1104  sudo rm .pr
 1105  sudo rm .project
 1106  python bar_chart.py
 1107  python color_data_map.py
 1108  python image.py
 1109  python
 1110  python --version
 1111  python 3.2
 1112  aria2c www.TamilRockers.lv\ -\ Inayathalam\ \(2017\)720p\ HD\ -\ AVC\ -\ MP4\ -\ 2.8GB\ -\ Tamil.mp4.torrent
 1113  python
 1114  aria2c www.TamilRockers.lv\ -\ Inayathalam\ \(2017\)
 1115  aria2c www.TamilRockers.lv - Inayathalam (2017)720p HD - AVC - MP4 - 2.8GB - Tamil.mp4.torrent
 1116  aria2c Inaya.torrent
 1117  ls
 1118  cd /opt/
 1119  cd Share/
 1120  ls
 1121  clear
 1122  ls
 1123  cd Personal/
 1124  ls
 1125  vi Important\ Notes.txt
 1126  clear
 1127  ls
 1128  cd Personal/
 1129  ls
 1130  vi Important\ Notes.txt
 1131  clear
 1132  cd ..
 1133  ls
 1134  cd Bujima/
 1135  ls
 1136  cd ..
 1137  ld
 1138  ls
 1139  cd Bosco/
 1140  ls
 1141  clear
 1142  ls
 1143  cd ..
 1144  ls
 1145  cd Downloads/
 1146  ls
 1147  cd ..
 1148  ;s
 1149  l
 1150  ls
 1151  cd Desktop\ Files/
 1152  ls
 1153  vi Links.txt
 1154  clear
 1155  exit
 1156  whereis .conf
 1157  ssh odoo@tendercuts.ifensys-demo.com
 1158  ll
 1159  sudo touch phpinfo.php
 1160  sudo mv magento-lts-1.9.2.4.zip /var/www/html/tendercuts.magento.com/public_html/Store
 1161  sudo mv Magento-CE-2.1.6-2017-03-29-01-08-05.tar.gz /var/www/html/tendercuts.magento.com/public_html/Store
 1162  sudo apt-get purge php*
 1163  ls
 1164  rm -rf php7.conf
 1165  sudo rm -rf php7.conf
 1166  cd /var/www/
 1167  ls
 1168  cd html/
 1169  ls
 1170  mkdir
 1171  mkdir tendercuts.magento.com
 1172  ls
 1173  ll
 1174  chown www-data:www-data tendercuts.magento.com/ -R
 1175  ll
 1176  cd tendercuts.magento.com/
 1177  ls
 1178  mkdir public_html
 1179  ls
 1180  cd public_html/
 1181  pw
 1182  pwd
 1183  cd ..
 1184  sudo mkdir logs
 1185  ls
 1186  cd public_html/
 1187  ls
 1188  cd Store/
 1189  ls
 1190  sudo unzip magento-lts-1.9.2.4.zip
 1191  sudo useradd magento
 1192  sudo usermod -g www-data magento
 1193  sudo find var vendor pub/static pub/media app/etc -type f -exec chmod g+w {} \;
 1194  sudo chown -R magento:www-data .
 1195  sudo chmod u+x bin/magento
 1196  cd magento-lts-1.9.2.4/
 1197  ls
 1198  cd mage
 1199  sudo systemctl restart apache2
 1200  sudo su magento
 1201  cd /etc/apache2/
 1202  ls
 1203  cd sites-available/
 1204  ls
 1205  vi 000-default.conf
 1206  ls
 1207  cd /var/www/
 1208  ls
 1209  cd html/
 1210  ls
 1211  vi test.php
 1212  cp tendercuts.magento.com/public_html/test.php .
 1213  ls
 1214  ll
 1215  cat test.php
 1216  cd /etc/apt
 1217  ls
 1218  cd sources.list.d/
 1219  ls
 1220  sudo rm -rf *
 1221  mysql -u root -p
 1222  apt install curl libcurl3
 1223  sudo apt install curl libcurl3
 1224  sudo subl /etc/php/7.0/fpm/php.ini
 1225  /etc/php/7.0
 1226  /etc/php/7.0/
 1227  cd /etc/php/7.0/
 1228  ld
 1229  ls
 1230  cd mods-available/
 1231  ls
 1232  cd ..
 1233  ls
 1234  cd cli
 1235  ls
 1236  sudo subl /etc/php/7.0/cli/php.ini
 1237  systemct restart php7.0-fpm
 1238  systemctl restart php7.0-fpm
 1239  apt-get install php7.0-fpm
 1240  sudo apt-get install php7.0-fpm
 1241  sudo subl /etc/php/7.0/fpm/php.ini
 1242  systemct restart php7.0-fpm
 1243  systemctl restart php7.0-fpm
 1244  mysql -u root -p
 1245  sudo apt-get install php-xml
 1246  sudo apt-get install php7.0-gd php7.0-mcrypt php7.0-curl php7.0-intl php7.0-xsl php7.0-mbstring php7.0-openssl php7.0-zip
 1247  sudo apt-get -y install php-fpm php-cli php-gd php-imagick php-mysql php-mcrypt php-pear php-curl php-intl php-xsl php-zip php-mbstring
 1248  ls
 1249  cd /var/www/html/
 1250  ls
 1251  cd tendercuts.magento.com/
 1252  ls
 1253  cd public_html/
 1254  ls
 1255  cd Store/
 1256  ls
 1257  sudo useradd magento
 1258  sudo usermod -g www-data magento
 1259  sudo find var vendor pub/static pub/media app/etc -type f -exec chmod g+w {} \;
 1260  sudo find var vendor pub/static pub/media app/etc -type d -exec chmod g+ws {} \;
 1261  sudo chown -R magento:www-data .
 1262  sudo chmod u+x bin/magento
 1263  sudo systemctl restart apache2
 1264  sudo su magento
 1265  cd ..
 1266  sudo tar -xvf Magento-CE-2.1.6-2017-03-29-01-08-05.tar.gz
 1267  sudo useradd magento
 1268  sudo find var vendor pub/static pub/media app/etc -type f -exec chmod g+w {} \;
 1269  sudo find var vendor pub/static pub/media app/etc -type d -exec chmod g+ws {} \;
 1270  sudo chown -R magento:www-data .
 1271  sudo chmod u+x bin/magento
 1272  sudo systemctl restart apache2
 1273  sudo su magento
 1274  sudo apt-get install lamp-server^
 1275  ls
 1276  cd ..
 1277  ls
 1278  php phpinfo.php
 1279  ll
 1280  cd Store/
 1281  ll
 1282  cd ..
 1283  ls
 1284  chown www-data:www-data phpinfo.php
 1285  sudo chown www-data:www-data phpinfo.php
 1286  ll
 1287  sudo chmod 755 phpinfo.php
 1288  ll
 1289  chmod 755 Store/ -R
 1290  suodo chmod 755 Store/ -R
 1291  sudo chmod 755 Store/ -R
 1292  lsof -i :80
 1293  sudo kill 13921
 1294  lsof -i :80
 1295  sudo kill 11429
 1296  lsof -i :80
 1297  systemctl status apache
 1298  sudo service apache2 status
 1299  sudo service apache2 stop
 1300  sudo service apache2 status
 1301  sudo systemctl status apache2
 1302  sudo systemctl start apache2
 1303  sudo systemctl status apache2
 1304  lsof -i :80
 1305  cd /etc/apache2/sites-available/
 1306  ls
 1307  vi tendercuts.magento.com.conf
 1308  cd /var/www/html/tendercuts.magento.com/
 1309  ls
 1310  cd public_html/
 1311  ls
 1312  vi test.php
 1313  ls
 1314  chmod 755 test.php
 1315  ll
 1316  chown www-data test.php
 1317  sudo chown www-data test.php
 1318  php test.php
 1319  sudo apt-get purge apache2
 1320  cd /etc/
 1321  ls
 1322  cd apache2/
 1323  ls
 1324  cd ..
 1325  sudo rm -rf apache2/
 1326  sudo apt-get install lamp-server^
 1327  sudo apt-get install phpmyadmin
 1328  sudo apt-get autoremove
 1329  cd apache2/mods-available/
 1330  ls
 1331  ll
 1332  sudo vi php7.conf
 1333  systemctl restart apache2
 1334  php -v
 1335  history | grep php
 1336  sudo su
 1337  sudo apt-get update && sudo apt-get upgrade
 1338  sudo apt-get -f install
 1339  sudo apt-get install php7.0-common php7.0-gd php7.0-mcrypt php7.0-curl php7.0-intl php7.0-xsl php7.0-mbstring php7.0-zip php7.0-iconv mysql-client
 1340  apache2 -v
 1341  sudo a2enmod rewrite
 1342  service apache2 status
 1343  vi /etc/apache2/sites-available/example.com.conf
 1344  sudo a2ensite example.com
 1345  vi /etc/apache2/sites-available/example.com.conf
 1346  subl /etc/apache2/sites-available/example.com.conf
 1347  sudo subl /etc/apache2/sites-available/example.com.conf
 1348  sudo a2ensite example.com
 1349  sudo systemctl restart apache2
 1350  service apache2 reload
 1351  sudo service apache2 stop
 1352  sudo service apache2 start
 1353  sudo service apache2 status
 1354  sudo a2dismod php7.0
 1355  sudo apache2 status
 1356  service apache2 restart
 1357  lsof -i :80
 1358  sudo kill -9 2907
 1359  lsof -i :80
 1360  lsof -i :11429
 1361  sudo service apache status
 1362  sudo service apache start
 1363  sudo service apache status
 1364  lsof -i :80
 1365  apache2 -v
 1366  sudo a2enmod rewrite
 1367  sudo apache2 status
 1368  /etc/init.d/apache2 restart
 1369  sudo systemctl start apache2.service
 1370  sudo systemctl stop apache2.service
 1371  sudo systemctl start apache2.service
 1372  journalctl -u apache2
 1373  sudo systemctl status apache2.service
 1374  sudo apache2ctl start
 1375  ping example.com
 1376  cd /etc/
 1377  sudo vim.tiny hosts
 1378  cd
 1379  ping tendercuts.magento.com
 1380  cd /etc/apache2/sites-available/
 1381  ls
 1382  mv example.com.conf tendercuts.magento.com.conf
 1383  sudo mv example.com.conf tendercuts.magento.com.conf
 1384  sudo vi tendercuts.magento.com.conf
 1385  ls
 1386  rm -rf ../sites-enabled/example.com.conf
 1387  sudo rm -rf ../sites-enabled/example.com.conf
 1388  sudo a2ensite tendercuts.magento.com.conf
 1389  sudo service apache2 reload
 1390  sudo a2dissite tendercuts.magento.com.conf
 1391  sudo service apache2 reload
 1392  sudo apache2 status
 1393  sudo service apache2 status
 1394  ls
 1395  sudo service apache2 status
 1396  sudo service apache2 start
 1397  sudo service apache2 status
 1398  sudo a2ensite tendercuts.magento.com.conf
 1399  sudo service apache2 reload
 1400  journalctl -xe
 1401  clear
 1402  history
 1403  sudo service apache2 start
 1404  sudo service apache2 status
 1405  sudo service apache2 restart
 1406  sudo touch /etc/apache2/envvars
 1407  sudo nano /etc/apache2/envvars
 1408  sudo service apache2 restart
 1409  systemctl status apache2.service
 1410  sudo a2enmod xxx.load
 1411  ls
 1412  sudo a2enmod tendercuts.magento.com.conf
 1413  cd a2enmod
 1414  sudo a2enmod xxx.load
 1415  sudo service apache2 restart
 1416  sudo apache2ctl configtest
 1417  sudo service apache2 restart
 1418  systemctl status apache2.service
 1419  sudo service apache2 reload
 1420  mysql -u root -p
 1421  sudo subl /etc/php/7.0/apache2/php.ini & /etc/php/7.0/cli/php.ini
 1422  sudo subl /etc/php/7.0/apache2/php.ini
 1423  sudo subl /etc/php/7.0/cli/php.ini
 1424  sudo subl /var/www/html/example.com/public_html/phpinfo.php
 1425  sudo subl /var/www/html/tendercuts.magento.com/public_html/phpinfo.php
 1426  apt update
 1427  sudo apt update
 1428  apt install nginx
 1429  sudo apt install nginx
 1430  sudo service apache2 stop
 1431  sudo apt install nginx
 1432  sudo apt install php7.0-mcrypt php7.0-fpm php7.0-curl php7.0-mysql php7.0-cli php7.0-xsl php7.0-json php7.0-intl php7.0-dev php-pear php7.0-mbstring php7.0-common php7.0-zip php7.0-gd php-soap
 1433  sudo apt install curl libcurl3
 1434  sudo smbl /etc/php/7.0/fpm/php.ini
 1435  sudo subl /etc/php/7.0/fpm/php.ini
 1436  curl -sS https://getcomposer.org/installer | php
 1437  mv composer.phar /usr/local/bin/composer
 1438  sudo mv composer.phar /usr/local/bin/composer
 1439  composer -v
 1440  composer create-project --repository-url=https://repo.magento.com/ magento/project-community-edition /var/www/magento2
 1441  EDITOR /etc/nginx/sites-available/magento
 1442  sudo subl /etc/nginx/sites-available/magento
 1443  ln -s /etc/nginx/sites-available/magento /etc/nginx/sites-enabled/
 1444  sudo ln -s /etc/nginx/sites-available/magento /etc/nginx/sites-enabled/
 1445  sudo systemctl restart nginx
 1446  /var/www/magento2/bin/magento setup:install --backend-frontname="admin" --key="cja8Jadsjwoqpgk93670Dfhu47m7rrIp"--db-host="localhost" --db-name="magento" --db-user="magento" --db-password="magento" --language="en_US" --currency="USD" --timezone="My/Timezone" --use-rewrites=1 --use-secure=0 --base-url="http://www.myecommerce.com" --base-url-secure="https://www.myecommerce.com" --admin-user=admin --admin-password=admin123 --admin-email=admin@myecommerce.com --admin-firstname=admin --admin-lastname=123 --cleanup-database
 1447  sudo /var/www/magento2/bin/magento setup:install --backend-frontname="admin" --key="cja8Jadsjwoqpgk93670Dfhu47m7rrIp"--db-host="localhost" --db-name="magento" --db-user="magento" --db-password="magento" --language="en_US" --currency="USD" --timezone="My/Timezone" --use-rewrites=1 --use-secure=0 --base-url="http://www.myecommerce.com" --base-url-secure="https://www.myecommerce.com" --admin-user=admin --admin-password=admin123 --admin-email=admin@myecommerce.com --admin-firstname=admin --admin-lastname=123 --cleanup-database
 1448  sudo /var/www/magento2/bin/magento setup:install
 1449  cd /var/www/magento2/bin
 1450  ls
 1451  execute magento
 1452  magento setup:install
 1453  sudo ./magento setup:install
 1454  sudo magento setup:install
 1455  sudo /var/www/magento2/bin/magento setup:install --backend-frontname="admin" --key="cja8Jadsjwoqpgk93670Dfhu47m7rrIp"--db-host="localhost" --db-name="magento_db" --db-user="magentousr" --db-password="usr_strong_password" --language="en_US" --currency="USD" --timezone="My/Timezone" --use-rewrites=1 --use-secure=0 --base-url="http://www.myecommerce.com" --base-url-secure="https://www.myecommerce.com" --admin-user=admin --admin-password=admin_password --admin-email=admin@myecommerce.com --admin-firstname=admin --admin-lastname=user --cleanup-database
 1456  ls
 1457  ll
 1458  chmod 755 magento
 1459  ll
 1460  sudo /var/www/magento2/bin/magento setup:install --backend-frontname="admin" --key="cja8Jadsjwoqpgk93670Dfhu47m7rrIp"--db-host="localhost" --db-name="magento" --db-user="magento" --db-password="magento" --language="en_US" --currency="USD" --timezone="My/Timezone" --use-rewrites=1 --use-secure=0 --base-url="http://www.myecommerce.com" --base-url-secure="https://www.myecommerce.com" --admin-user=admin --admin-password=admin123 --admin-email=admin@myecommerce.com --admin-firstname=admin --admin-lastname=123 --cleanup-database
 1461  sudo /var/www/magento2/bin/magento setup:install --backend-frontname="admin" --key="cja8Jadsjwoqpgk93670Dfhu47m7rrIp"--db-host="localhost" --db-name="magento" --db-user="magento" --db-password="magento" --language="en_US" --currency="USD" --timezone="Britain/United Kingdom" --use-rewrites=1 --use-secure=0 --base-url="http://www.myecommerce.com" --base-url-secure="https://www.myecommerce.com" --admin-user=admin --admin-password=admin123 --admin-email=admin@myecommerce.com --admin-firstname=admin --admin-lastname=123 --cleanup-database
 1462  sudo /var/www/magento2/bin/magento setup:install --backend-frontname="admin" --key="cja8Jadsjwoqpgk93670Dfhu47m7rrIp"--db-host="localhost" --db-name="magento" --db-user="magento" --db-password="magento" --language="en_US" --currency="USD" --use-rewrites=1 --use-secure=0 --base-url="http://www.myecommerce.com" --base-url-secure="https://www.myecommerce.com" --admin-user=admin --admin-password=admin123 --admin-email=admin@myecommerce.com --admin-firstname=admin --admin-lastname=123 --cleanup-database
 1463  service nginx status
 1464  sudo service nginx stop
 1465  history
 1466  systemctl status apache2
 1467  systemctl start apache2
 1468  systemctl status apache2
 1469  sh pycharm.sh
 1470  service apache2 status
 1471  service apache2 start
 1472  service apache2 status
 1473  service apache2 start
 1474  service apache2 status
 1475  sudo systemctl start apache2.service
 1476  service apache2 status
 1477  lsof -i :80
 1478  kill -9 9164
 1479  lsof -i :80
 1480  sudo systemctl start apache2.service
 1481  service apache2 status
 1482  sudo /etc/init.d/apache2 start
 1483  service apache2 status
 1484  sudo service nginx status
 1485  sudo service nginx stop
 1486  sudo /etc/init.d/apache2 start
 1487  service apache2 status
 1488  sudo apt-get install php7-xmlrpc
 1489  sudo apt-get install php7-xml-rpc
 1490  sudo apt-get install php-xml-rpc
 1491  sudo apt-get install php7.0-xml-rpc
 1492  php -v
 1493  sudo apt-get install -y php7.0 php7.0-fpm php7.0-cli php7.0-common php7.0-mbstring php7.0-gd php7.0-intl php7.0-xml php7.0-mysql php7.0-mcrypt php7.0-zip
 1494  sudo apt-get install php7.0-xmlrpc
 1495  service apache2 status
 1496  service apache2 restart
 1497  service apache2 status
 1498  service apache2 restart
 1499  service apache2 status
 1500  sudo service nginx status
 1501  sudo service nginx stop
 1502  service apache2 start
 1503  service apache2 status
 1504  sudo pip install odoorpc
 1505  /usr/bin/python -m pip install pylint
 1506  sudo /usr/bin/python -m pip install pylint
 1507  python /home/susai/Documents/webservice.py
 1508  ps -fA | grep python
 1509  ps -fA | greb python
 1510  ps -fA | grep python
 1511  ls
 1512  cd Downloads/
 1513  aria2c TheZookeepersWife.torrent
 1514  aria2c Lens\ \(2017\).torrent
 1515  aria2c vm.torrent
 1516  python
 1517  sudo pip install --upgrade --pre pylint-odoo
 1518  cd /home/susai/Downloads/The Zookeeper's Wife (2017) [YTS.AG]
 1519  ls
 1520  exit
 1521  cd /home/susai/Downloads/The\ Zookeeper\'s\ Wife\ \(2017\)\ \[YTS.AG\]/
 1522  ls
 1523  exit
 1524  ls -a
 1525  sudo rm .gitignore
 1526  cd git
 1527  npm install
 1528  xargs rm -rf < non-essential-files.osx.txt
 1529  rm src/app/*.spec*.ts
 1530  rm non-essential-files.osx.txt
 1531  wkhtmltopdf -V
 1532  sudo python setup.py intall
 1533  sudo pip install MySQLdb
 1534  sudo apt-get install python-msqldb
 1535  sudo apt-get install python-mysqldb
 1536  sudo pip install pyodbc
 1537  tar -x pyodbc-4.0.17.tar.gz
 1538  tar xvzf pyodbc-4.0.17.tar.gz
 1539  sudo python setup.py install
 1540  sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-imaging python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libssl-dev
 1541  sudo easy_install greenlet
 1542  sudo easy_install gevent
 1543  sudo python setup.py install
 1544  sudo apt-get install build-essential libssl-dev libffi-dev python-dev
 1545  sudo pip install pillow
 1546  pip install pycrypto
 1547  sudo pip install pyodbc
 1548  cd /tmp/
 1549  ls
 1550  yum install unixODBC-devel
 1551  sudo install unixODBC-devel
 1552  sudo apt-get install unixODBC-devel
 1553  sudo apt-get install unixodbc-dev
 1554  sudo pip install pyodbc
 1555  sudo pip install pymssql
 1556  mkdir app
 1557  cd app
 1558  touch app.component.ts
 1559  subl app.component.ts
 1560  touch main.ts
 1561  subl main.ts
 1562  cd ..
 1563  touch index.html
 1564  subl index.html
 1565  touch styles.css
 1566  subl styles.css
 1567  ping www.google.com
 1568  ls
 1569  cd Desktop/
 1570  ls
 1571  mkdir Angular2App
 1572  cd Angular2App/
 1573  node -v
 1574  npm -v
 1575  touch package.json
 1576  touch tsconfig.json
 1577  touch typings.json
 1578  touch systemjs.config.js
 1579  subl package.json
 1580  subl tsconfig.json
 1581  subl typings.json
 1582  subl systemjs.config.js
 1583  npm install
 1584  apt-get update
 1585  sudo apt-get update
 1586  sudo apt-get -f install
 1587  sudo service ngix status
 1588  sudo service ngix start
 1589  sudo service apache2 status
 1590  apt-get install nginx
 1591  sudo apt-get install nginx
 1592  ps –ef | grep nginx
 1593  sudo ps –ef | grep nginx
 1594  sudo service ngix status
 1595  sudo service nginx reload
 1596  sudo service nginx status
 1597  sudo chmod 777 /var/www/html
 1598  cp Desktop/Angular2Project/Demo /var/www/html
 1599  sudo cp Desktop/Angular2Project/Demo /var/www/html
 1600  sudo Desktop/Angular2Project/Demo cd /var/www/html
 1601  cp -r Desktop/Angular2Project/Demo /var/www/html
 1602  cd /var/www/html/
 1603  ls
 1604  npm install
 1605  npm start
 1606  ping www.google.com
 1607  sudo service nginx status
 1608  sudo service nginx stop
 1609  sudo service nginx start
 1610  npm install
 1611  npm start
 1612  npm start
 1613  mkdir angular2-demo
 1614  cd angular2-demo
 1615  touch tsconfig.json
 1616  subl tsconfig.json
 1617  touch typings.json
 1618  subl typings.json
 1619  touch package.json
 1620  subl package.json
 1621  npm install
 1622  git clone https://github.com/angular/quickstart Demo
 1623  sudo pip install --upgrade --pre pylint-odoo
 1624  cd ..
 1625  cd to\ test/
 1626  ls
 1627  touch /opt/Gnanam/BES/Odoo/Addons\ downloaded/Odoo\ 10/Untitled\ Folder/__init__.py
 1628  touch touch /opt/Gnanam/BES/Odoo/Addons\ downloaded/Odoo\ 10/Untitled\ Folder/__init__.py/__init__.py
 1629  touch show_chartsshow_chartsshow_chartsshow_charts/__init__.py
 1630  touch /home/susai/Desktop/to test/show_charts/__init__.py
 1631  touch /home/susai/Desktop/to
 1632  touch /home/susai/Desktop/to_test/show_charts/__init__.py
 1633  pylint --load-plugins=pylint_odoo -d all -e odoolint /home/susai/Desktop/to_test/
 1634  touch /home/susai/Desktop/to_test/show_charts/__init__.py
 1635  pylint --load-plugins=pylint_odoo -d all -e odoolint /home/susai/Desktop/to_test/
 1636  pylint --load-plugins=pylint_odoo -d all -e odoolint
 1637  pylint --load-plugins=pylint_odoo -d all -e odoolint /home/susai/Desktop/to_test
 1638  npm install
 1639  npm start
 1640  psql -U odoo
 1641  psql -U odoo database 'store'
 1642  psql -d  new_store -U odoo
 1643  pip uninstall Pillow
 1644  sudo pip uninstall Pillow
 1645  sudo pip uninstall PIL
 1646  sudo apt-get install libjpeg-dev
 1647  sudo pip install Pillow
 1648  sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
 1649  sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
 1650  sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
 1651  sudo apt-get install libjpeg-dev
 1652  sudo apt-get install libjpeg8-dev
 1653  pip install --no-cache-dir -I pillow
 1654  sudo pip install --no-cache-dir -I pillow
 1655  pylint --load-plugins=pylint_odoo -d all -e odoolint /home/susai/Desktop/to_test
 1656  ng serve
 1657  ng serve --host 192.168.1.124
 1658  node -v
 1659  ng -v
 1660  ng new contact
 1661  ls
 1662  cd contact/
 1663  ls
 1664  cd src/
 1665  ls
 1666  cd app/
 1667  ls
 1668  cd components/
 1669  ls
 1670  ng g component header
 1671  ng g component footer
 1672  ng g component navbar
 1673  ng g component login
 1674  ng g component register
 1675  ng g component home
 1676  ls
 1677  cd ..
 1678  ls
 1679  ng -v
 1680  node -v
 1681  sudo npm install -g n
 1682  sudo n latest
 1683  npm install -g @angular/cli
 1684  sudo npm install -g @angular/cli
 1685  npm start
 1686  history
 1687  pip freeze
 1688  pip uninstall Pillow
 1689  sudo pip uninstall Pillow
 1690  pip install Pillow==3.4.1
 1691  sudo pip install Pillow==3.4.1
 1692  sudo lshw
 1693  sudo dmidecode --type 17
 1694  aria2c http://download.welltorrent.com/Transformers%20The%20Last%20Knight%20(2017)%20720p%20CAMRip.torrent
 1695  aria2c Transformers\ The\ Last\ Knight\ \(2017\)\ 720p\ CAMRip.torrent
 1696  ng serve localhost:8080
 1697  ls
 1698  cd Desktop/
 1699  ls
 1700  ce Angular2Contact/
 1701  cd Angular2Contact/
 1702  ng new contact
 1703  cd contact/
 1704  serve localhost:192.168.1.124
 1705  ng serve localhost:192.168.1.124
 1706  ng serve
 1707  cd src
 1708  mkdir components
 1709  cd components/
 1710  ls
 1711  cd compan
 1712  ls
 1713  ng g conponent header
 1714  ng g component header
 1715  ng g component home
 1716  ng g component footer
 1717  ng g component login
 1718  ng g component navbar
 1719  ssh ifensys@erp.tendercuts.in
 1720  exit
 1721  ssh ifensys@erp.tendercuts.in
 1722  exit
 1723  sudo apt-get update
 1724  sudo apt-get -f install
 1725  sudo apt autoremove
 1726  sudo apt clean
 1727  ng serve
 1728  cd app
 1729  cd src
 1730  cd app
 1731  ng g component about
 1732  ng g component contact
 1733  sudo apt-get remove wine
 1734  sudo apt-get remove --auto-remove wine
 1735  sudo apt-get purge wine
 1736  sudo apt-get remove wine
 1737  rm -rf $HOME/.wine
 1738  rm -f $HOME/.config/menus/applications-merged/wine*
 1739  rm -rf $HOME/.local/share/applications/wine
 1740  rm -f $HOME/.local/share/desktop-directories/wine*
 1741  rm -f $HOME/.local/share/icons/????_*.xpm
 1742  sudo apt-get remove –purge wine
 1743  sudo apt-get update
 1744  sudo apt-get -f install
 1745  sudo apt-get autoclean
 1746  sudo apt-get clean
 1747  sudo apt-get autoremove
 1748  sudo apt-get install libxine2-all-plugins
 1749  sudo add-apt-repository ppa:ubuntu-audio-dev/ppa
 1750  sudo apt-get update
 1751  sudo apt-get install linux-alsa-driver-modules-$(uname -r)
 1752  sudo chmod 775 /home/susai/Desktop/product_product.csv
 1753  aria2c Gifted\ \(2017\)\ \[720p\]\ \[YTS.AG\].torrent
 1754  aria2c The\ Boss\ Baby\ \(2017\)\ \[720p\]\ \[YTS.AG\].torrent
 1755  aria2c Gifted\ \(2017\)\ \[720p\]\ \[YTS.AG\].torrent
 1756  ls
 1757  cd Desktop/
 1758  ls
 1759  virtualenv envtest
 1760  sudo apt-get install virtualenv
 1761  virtualenv envtest
 1762  pip feeze
 1763  pip freeze
 1764  clear
 1765  cd envtest/
 1766  cd bin
 1767  source activate
 1768  pip freeze
 1769  deactivate
 1770  cd ..
 1771  rm envtest/
 1772  sudo rm -r envtest/
 1773  ls
 1774  virtualenv env test
 1775  virtualenv env_test
 1776  cd env_test/
 1777  cd bin/
 1778  source activate
 1779  pip
 1780  deactivate
 1781  exit
 1782  aria2c The\ Lost\ City\ of\ Z\ \(2016\)\ \[720p\]\ \[YTS.AG\].torrent
 1783  aria2c The\ Boss\ Baby\ \(2017\)\ \[
 1784  aria2c The\ Boss\ Baby\ \(2017\)\ \[720p\]\ \[YTS.AG\].torrent
 1785  aria2c --max-uploadd-limit=0kb The\ Boss\ Baby\ \(2017\)\ \[720p\]\ \[YTS.AG\].torrent
 1786  aria2c The\ Boss\ Baby\ \(2017\)\ \[720p\]\ \[YTS.AG\].torrent
 1787  sudo service apache2 status
 1788  sudo service nginx status
 1789  sudo service nginx stop
 1790  sudo service apache2 start
 1791  aria2c Dhoom\ 3\ 2013.torrent
 1792  ls
 1793  sudo pip install jwt
 1794  sudo pip install pyjwt
 1795  ps -aux | grep python
 1796  kill -9 4915 5901 5925 17879 17936
 1797  ps -aux | grep python
 1798  sudo pip remove jwt
 1799  sudo pip uninstall jwt
 1800  sudo pip uninstall pyjwt
 1801  sudo pip install pyjwt
 1802  sudo pip install cryptography
 1803  sudo service nginx
 1804  sudo service nginx status
 1805  sudo service nginx stop
 1806  sudo service apache2 start
 1807  sudo service nginx stop
 1808  sudo service apache2 start
 1809  sudo service apache2 status
 1810  python webservice.py
 1811  git status
 1812  sudo touch .gitignore
 1813  subl .gitignore
 1814  git status
 1815  ls
 1816  ls -a
 1817  git add .gitignore
 1818  git status
 1819  git commit .gitignore
 1820  ls - a
 1821  ls -a
 1822  git status
 1823  git commit .gitignore
 1824  git push
 1825  find . -name "*.pyc" -exec git rm -f {} \;
 1826  sudo find . -name "*.pyc" -exec git rm -f {} \;
 1827  ssh ifensys@erp.tendercuts.in
 1828  exit
 1829  sudo apt-get install gpick
 1830  sudo service apache2 status
 1831  sudo service nginx status
 1832  sudo service nginx stop
 1833  sudo service apache2 start
 1834  aria2c Wonder\ Woman\ 2017\ 758\ MB.torrent
 1835  sudo umount /dev/sdd1
 1836  umount /dev/sdd1
 1837  fdisk -l
 1838  sudo fdisk -l
 1839  sudo gparted
 1840  lsblk -m
 1841  lsblk
 1842  sudo dd if=/dev/zero of=/dev/sdb bs=4k && sync
 1843  lsblk
 1844  sudo fdisk /dev/sdb
 1845  lsblk
 1846  lsblk
 1847  sudo fdisk /dev/sdc
 1848  lsblk
 1849  sudo fdisk /dev/sdc
 1850  lsblk
 1851  sudo mkfs.vfat /dev/sdc1
 1852  lsblk
 1853  sudo dd if=/dev/zero of=/dev/sdc1 bs=4k && sync
 1854  lsblk
 1855  sudo dd if=/dev/zero of=/dev/sdc bs=4k && sync
 1856  lsblk
 1857  sudo fdisk /dev/sdc
 1858  lsblk
 1859  sudo dd if=/dev/zero of=/dev/sdc4 bs=4k && sync
 1860  lsblk
 1861  sudo mkfs.vfat /dev/sdc4
 1862  lsblk
 1863  sudo eject /dev/sdc4
 1864  ls
 1865  ls -a
 1866  sudo pip install xlsxwriter
 1867  history
 1868  sudo service nginx status
 1869  sudo service nginx stop
 1870  sudo service apache2 status
 1871  sudo service apache2 start
 1872  aria2c www.TamilRockers.nu\ -\ Vikram\ Vedha\ \(2017\)HQ\ Real\ DVDScr\ -\ x264\ -\ 1.4GB\ -\ Tamil.mkv.torrent
 1873  sudo service apache2 status
 1874  sudo service nginx stop
 1875  sudo service apache2 start
 1876  sudo apt-get update
 1877  sudo service nginx stop
 1878  sudo service apache2 start
 1879  aria2c Boyka-\ Undisputed\ \(2016\)\ \[1080p\]\ \[YTS.AG\].torrent
 1880  aria2c
 1881  aria2c Alien-\ Covenant\ \(2017\)\ \[720p\]\ \[YTS.AG\].torrent
 1882  sudo apt-get install ntfs-3g
 1883  sudo apt-get install ntfs-config
 1884  run ntfs-config
 1885  sudo run ntfs-config
 1886  sudo apt-get -f install
 1887  sudo su -
 1888  aria2c Let\ Me\ In\ \(2010\)\ \[720p\]\ \[YTS.AG\].torrent
 1889  aria2c Super-Star-Special--Arunachalam--1997--DVD-Rip--Movies-Share.torrent
 1890  aria2c \[DVD-Rip\]-Arunachalam-\(1997\)-Xvid-1CD-AVI.torrent
 1891  aria2c aru.torrent
 1892  aria2c Let\ Me\ In\ \(201
 1893  aria2c Let\ Me\ In\ \(2010\)\ \[720p\]\ \[YTS.AG\].torrent
 1894  wget http://download.forge.ow2.org/spagobi/All-In-One-SpagoBI-5.0-01102014.zip
 1895  sudo wget http://download.forge.ow2.org/spagobi/All-In-One-SpagoBI-5.0-01102014.zip
 1896  sudo chmod 777 Test/
 1897  chmod 777 product_product.csv
 1898  sudo chmod 777 product_product.csv
 1899  sudo psql -d tendercuts_new -U admin
 1900  sudo psql -d tendercuts_new -U odoo
 1901  sudo chmod 777 o
 1902  sudo chmod 777 product_product.csv
 1903  aria2c Let\ Me\ In\ \(2010\)\ \[720p\]\ \[YTS.AG\].torrent
 1904  aria2c Alien-\ Covenant\ \(2017\)\ \[720p\]\ \[YTS.AG\].torrent
 1905  cd The\ Bourne/
 1906  ls
 1907  aria2c The\ Bourne\ Identity\ \(2002\)\ \[720p\]\ \[YTS.AG\].torrent
 1908  sudo service nginx stop
 1909  sudo service apache2 status
 1910  sudo service apache2 start
 1911  sudo service apache2 status
 1912  ssh odoo@ifensys-demo.com
 1913  aria2c The\ Bourne\ Supremacy\ \(2004\)\ \[720p\]\ \[YTS.AG\].torrent
 1914  aria2c The\ Bourne\ Ultimatum\ \(2007\)\ \[720p\]\ \[YTS.AG\].torrent
 1915  aria2c The\ Bourne\ Legacy\ \(2012\)\ \[720p\]\ \[YTS.AG\].torrent
 1916  aria2c https://yts.ag/torrent/download/A2E7EA58534C1769D50EAD2DA2778836E407084C
 1917  .com
 1918  sudo chmod 777 odoo
 1919  ./odoo scaffold test module /home/susai/snap
 1920  ./odoo-bin scaffold test module /home/susai/snap
 1921  ./odoo-bin scaffold test /home/susai/snap
 1922  ./odoo-bin scaffold test1 /home/susai/snap
 1923  ./odoo-bin scaffold test1
 1924  ./odoo saffold test_module
 1925  sudo ./odoo saffold test_module
 1926  sudo ./odoo-bin saffold test_module
 1927  sudo odoo-bin saffold test_module
 1928  sudo ./odoo.py saffold test_module
 1929  sudo ./odoo.py scaffold test_module
 1930  sudo ./odoo-bin.py scaffold test_module
 1931  ./odoo-bin.py scaffold test_module
 1932  ls
 1933  ./odoo-bin scaffold test_module
 1934  sudo ./odoo-bin scaffold test_module
 1935  sudo ./odoo-bin scaffold test_module /home/susai/snap
 1936  ./odoo-bin scaffold test_module /home/susai/snap
 1937  sudo chmod 777 odo-bin
 1938  sudo chmod 777 odoo-bin
 1939  sudo service nginx status
 1940  sudo service nginx stop
 1941  sudo service apache2 start
 1942  sudo ps aux | grep python
 1943  kill -9 4484
 1944  kill -9 8169
 1945  kill -9 19430
 1946  kill -9 20602
 1947  sudo ps aux | grep python
 1948  kill -9 20614
 1949  sudo dpkg -i skypeforlinux-64.deb
 1950  sudo fdisk -l
 1951  sudo service nginx stop
 1952  sudo service apache2 start
 1953  sudo service apache2 status
 1954  ls
 1955  sudo service apache2 status
 1956  sudo service nginx stop
 1957  sudo service apache2 start
 1958  sudo service apache2 status
 1959  sudo service nginx status
 1960  sudo service apache2 stop
 1961  sudo service apache2 start
 1962  sudo service apache2 stop
 1963  sudo service apache2 start
 1964  python
 1965  ssh erp.tendercuts.in
 1966  ssh ifensys@erp.tendercuts.in
 1967  exit
 1968  ssh odoo@ifensys-demo.com
 1969  pylint main.py
 1970  pylint
 1971  pylint /home/susai/Downloads/bokeh-master/
 1972  clear
 1973  history
 1974  pylint --load-plugins=pylint_odoo -d all -e odoolint /home/susai/Desktop/to_test/
 1975  sudo service nginx stop
 1976  sudo service apache2 start
 1977  sudo service apache2 status
 1978  cd ..
 1979  pylint
 1980  clear
 1981  pylint /opt/Source/Neon\ Workspace/odoo-10.0/test/__init__.py
 1982  pylint /opt/Source/Neon\ Workspace/odoo-10.0/test
 1983  ./odoo-bin1 scaffold test
 1984  ls
 1985  ls -a
 1986  ls -l
 1987  sudo chmod 755 odoo-bin1
 1988  ls
 1989  ./odoo-bin1 scaffold test
 1990  whereis .bash_history
 1991  python
 1992  aria2c http://62.138.0.84/downloads/Th3-D2-V1nc1-C0d3-2006-720p-hdp0pc0rns.mkv?st=VBXbIzPHp5Vh8XAI3lj48g&e=1503472435
 1993  aria2c The\ Da\ Vinci\ Code\ \(2006\)\ \[720p\]\ \[YTS.AG\].torrent
 1994  ssh bosco@192.168.1.159
 1995  ssh odoo@ifensys-demo.com
 1996  exit
 1997  pip freeze
 1998  ssh odoo@ifensys-demo.com
 1999  exit
 2000  python
 1931  apt­-get install curl
 1932  ap-get install curl
 1933  sudo apt-get install curl
 1934  curlhttp://archive.eclipse.org/technology/epp/downloads/release/oxygen/M2/eclipse-jee-oxygen-M2-linux-gtk-x86_64.tar.gz
 1935  curl http://archive.eclipse.org/technology/epp/downloads/release/oxygen/M2/eclipse-jee-oxygen-M2-linux-gtk-x86_64.tar.gz
 1936  sudo ps aux | grep vlc
 1937  sudo kill -9 13103
 1938  sudo kill -9 13117
 1939  sudo service nginx stop
 1940  sudo service apache2 start
 1941  sudo service apache2 status
 1942  ssh odoo@ifensys-demo.com
 1943  exit
 1944  ./odoo-bin scaffold /opt/Source/Neon Workspace/Odoo_10_theme/inherited_purchase_report
 1945  ./odoo-bin1 scaffold /opt/Source/Neon Workspace/Odoo_10_theme/inherited_purchase_report
 1946  ./odoo-bin1 scaffold inherited_purchase_report
 1947  pylint --load-plugins=pylint_odoo -d all -e odoolint /opt/Source/Neon Workspace/Odoo_10_theme/inherited_purchase_report
 1948  pylint --load-plugins=pylint_odoo -d all -e odoolint /opt/Source/Neon Workspace/Odoo_10_theme/inherited_purchase_report/__init__.py
 1949  touch /opt/Source/Neon Workspace/Odoo_10_theme/inherited_purchase_report/__init__.py
 1950  pylint --load-plugins=pylint_odoo -d all -e odoolint /opt/Source/Neon Workspace/Odoo_10_theme/inherited_purchase_report
 1951  ssh odoo@ifensys-demo.com
 1952  wkhtmltopdf
 1953  sudo apt-get uninstall wkhtmltopdf
 1954  sudo apt-get remove wkhtmltopdf
 1955  sudo apt-get remove --auto-remove wkhtmltopdf
 1956  sudo apt-get purge wkhtmltopdf
 1957  sudo apt-get purge --auto-remove wkhtmltopdf
 1958  sudo apt-get install wkhtmltopdf == 0.12.2.1
 1959  sudo apt-get install wkhtmltopdf==0.12.2.1
 1960  sudo apt-get install xvfb
 1961  wget http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-trusty-amd64.deb
 1962  sudo dpkg -i wkhtmltox-0.12.2.1_linux-trusty-amd64.deb
 1963  ls
 1964  cd Downloads/
 1965  ls
 1966  sudo dpkg -i wkhtmltox-0.12.2.1_linux-trusty-amd64.deb
 1967  sudo apt-get -f install
 1968  wkhtmltopdf
 1969  ssh odoo@ifensys-demo.com
 1970  sudo service nginx stop
 1971  sudo service apache2 start
 1972  sudo service apache2 status
 1973  cd Documents/
 1974  ls
 1975  unzip OpenUpgrade-10.0.zip
 1976  cd /opt/
 1977  ls
 1978  cd Source/
 1979  ls
 1980  cd Neon\ Workspace/
 1981  ls
 1982  cd Confic_Files/
 1983  ls
 1984  cat /opt/Source/Neon Workspace/Confic_Files/openerp-server_odoo_8.cfg
 1985  ls
 1986  cat "/opt/Source/Neon Workspace/Confic_Files/openerp-server_odoo_8.cfg"
 1987  cp openerp-server_odoo_8.cfg /tmp/odoo8.conf
 1988  sudo -i
 1989  ps -aux | grep python
 1990  kill -9 13945
 1991  cd /home/susai/Documents/OpenUpgrade-10.0/
 1992  ls
 1993  cd scripts/
 1994  ls
 1995  python migrate.py --config=/tmp/odoo8.conf --database=bodhih --run-migrations=8.0,10.0
 1996  ps -eaf | grep python
 1997  kill -9 15385
 1998  python migrate.py --config=/tmp/odoo8.conf --database=bodhih --run-migrations=8.0,10.0
 1999  ssh odoo@ifensys.com
 2000  ssh odoo@ifensys-demo.com
 2001  ps -eaf | grep python
 2002  kill -9 13930
 2003  kill -9 8089
 2004  kill -9 8015
 2005  kill -9 8061
 2006  history
sudo odoo /opt/Source/Neon Workspace/Confic_Files/openerp-server_common_theme.cfg
 2006  sudo /opt/Source/Neon Workspace/odoo-10.0-20170706/setup/odoo-bin
 2007  run /opt/Source/Neon Workspace/odoo-10.0-20170706/setup/odoo-bin
 2008  cd /opt/Source/Neon Workspace/odoo-10.0-20170706
 2009  cd /opt/Source/Neon\ Workspace/odoo9
 2010  ls
 2011  ./odoo.py
 2012  ./odoo.py -c "/opt/Source/Neon Workspace/Confic_Files/openerp-server_odoo_9.cfg"



 susai@621Bits-237:~$ sudo -i
[sudo] password for susai:
root@621Bits-237:~# ping odoo.mysite.co
^C
root@621Bits-237:~# subl /etc/hosts
root@621Bits-237:~# subl /etc/hosts
root@621Bits-237:~# ping odoo.mysite.co
PING odoo.mysite.co (127.0.1.1) 56(84) bytes of data.
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=1 ttl=64 time=0.015 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=2 ttl=64 time=0.019 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=3 ttl=64 time=0.020 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=4 ttl=64 time=0.024 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=5 ttl=64 time=0.117 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=6 ttl=64 time=0.019 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=7 ttl=64 time=0.021 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=8 ttl=64 time=0.016 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=9 ttl=64 time=0.017 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=10 ttl=64 time=0.018 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=11 ttl=64 time=0.017 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=12 ttl=64 time=0.015 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=13 ttl=64 time=0.016 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=14 ttl=64 time=0.017 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=15 ttl=64 time=0.020 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=16 ttl=64 time=0.018 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=17 ttl=64 time=0.074 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=18 ttl=64 time=0.019 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=19 ttl=64 time=0.019 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=20 ttl=64 time=0.018 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=21 ttl=64 time=0.022 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=22 ttl=64 time=0.018 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=23 ttl=64 time=0.019 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=24 ttl=64 time=0.024 ms
64 bytes from 621Bits-237 (127.0.1.1): icmp_seq=25 ttl=64 time=0.019 ms
^C
--- odoo.mysite.co ping statistics ---
25 packets transmitted, 25 received, 0% packet loss, time 24559ms
rtt min/avg/max/mdev = 0.015/0.024/0.117/0.022 ms
root@621Bits-237:~# system
system-config-printer           systemd-cat                     systemd-hwdb                    systemd-run
system-config-printer-applet    systemd-cgls                    systemd-inhibit                 systemd-stdio-bridge
systemctl                       systemd-cgtop                   systemd-machine-id-setup        systemd-tmpfiles
systemd                         systemd-delta                   systemd-notify                  systemd-tty-ask-password-agent
systemd-analyze                 systemd-detect-virt             systemd-path
systemd-ask-password            systemd-escape                  systemd-resolve
root@621Bits-237:~# systemctl stop apache2
root@621Bits-237:~# systemctl status apache2
● apache2.service - LSB: Apache2 web server
   Loaded: loaded (/etc/init.d/apache2; bad; vendor preset: enabled)
  Drop-In: /lib/systemd/system/apache2.service.d
           └─apache2-systemd.conf
   Active: inactive (dead) since Fri 2017-09-29 09:19:20 IST; 5h 47min ago
     Docs: man:systemd-sysv-generator(8)

Sep 29 09:19:20 621Bits-237 apache2[1720]: (98)Address already in use: AH00072: make_sock: could not bind to address 0.0.0.0:80
Sep 29 09:19:20 621Bits-237 apache2[1720]: no listening sockets available, shutting down
Sep 29 09:19:20 621Bits-237 apache2[1720]: AH00015: Unable to open logs
Sep 29 09:19:20 621Bits-237 apache2[1720]: Action 'start' failed.
Sep 29 09:19:20 621Bits-237 apache2[1720]: The Apache error log may have more information.
Sep 29 09:19:20 621Bits-237 apache2[1720]:  *
Sep 29 09:19:20 621Bits-237 apache2[1963]:  * Stopping Apache httpd web server apache2
Sep 29 09:19:20 621Bits-237 apache2[1963]:  *
Sep 29 09:19:20 621Bits-237 systemd[1]: Started LSB: Apache2 web server.
Sep 29 15:06:05 621Bits-237 systemd[1]: Stopped LSB: Apache2 web server.
root@621Bits-237:~# systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since Fri 2017-09-29 10:55:38 IST; 4h 10min ago
 Main PID: 9116 (nginx)
   CGroup: /system.slice/nginx.service
           ├─9116 nginx: master process /usr/sbin/nginx -g daemon on; master_process on
           ├─9117 nginx: worker process
           ├─9118 nginx: worker process
           ├─9119 nginx: worker process
           ├─9120 nginx: worker process
           ├─9121 nginx: worker process
           ├─9122 nginx: worker process
           ├─9123 nginx: worker process
           └─9124 nginx: worker process

Sep 29 10:55:38 621Bits-237 systemd[1]: Starting A high performance web server and a reverse proxy server...
Sep 29 10:55:38 621Bits-237 systemd[1]: Started A high performance web server and a reverse proxy server.
root@621Bits-237:~# systemctl restart nginx
root@621Bits-237:~# cd /etc/nginx/sites-available/
root@621Bits-237:/etc/nginx/sites-available# ls
default  magento  odoo
root@621Bits-237:/etc/nginx/sites-available# subl odoo
root@621Bits-237:/etc/nginx/sites-available# mv odoo odoo.mysite.co.conf
root@621Bits-237:/etc/nginx/sites-available# subl odoo odoo.mysite.co.conf
root@621Bits-237:/etc/nginx/sites-available# subl odoo.mysite.co.conf
root@621Bits-237:/etc/nginx/sites-available# subl odoo.mysite.co.conf
root@621Bits-237:/etc/nginx/sites-available# cd ../sites-enabled/
root@621Bits-237:/etc/nginx/sites-enabled# ls
default  magento  odoo
root@621Bits-237:/etc/nginx/sites-enabled# rm -rf odoo
root@621Bits-237:/etc/nginx/sites-enabled# cd ../s
sites-available/ sites-enabled/   snippets/        ssl/
root@621Bits-237:/etc/nginx/sites-enabled# cd ../sites-available/
root@621Bits-237:/etc/nginx/sites-available# ls
default  magento  odoo.mysite.co.conf
root@621Bits-237:/etc/nginx/sites-available# cat odoo.mysite.co.conf
#odoo server
upstream mysite {
 server 127.0.0.1:8069;
}

server {
 listen 80;
 server_name odoo.mysite.co www.odoo.mysite.co;
 proxy_read_timeout 720s;
 proxy_connect_timeout 720s;
 proxy_send_timeout 720s;

 # Add Headers for odoo proxy mode
 proxy_set_header X-Forwarded-Host $host;
 proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
 proxy_set_header X-Forwarded-Proto $scheme;
 proxy_set_header X-Real-IP $remote_addr;

 # log
 access_log /var/log/nginx/odoo.mysite.co.access.log;
 error_log /var/log/nginx/odoo.mysite.co.error.log;

 # Redirect requests to odoo backend server
 location / {
   proxy_redirect off;
   proxy_pass http://mysite;
 }

}
root@621Bits-237:/etc/nginx/sites-available#
root@621Bits-237:/etc/nginx/sites-available# ln -s /etc/nginx/sites-available/odoo.mysite.co.conf /etc/nginx/sites-available/
ln: failed to create symbolic link '/etc/nginx/sites-available/odoo.mysite.co.conf': File exists
root@621Bits-237:/etc/nginx/sites-available# ls
default  magento  odoo.mysite.co.conf
root@621Bits-237:/etc/nginx/sites-available# ln -s /etc/nginx/sites-available/odoo.mysite.co.conf /etc/nginx/sites-enabled/
root@621Bits-237:/etc/nginx/sites-available# nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
root@621Bits-237:/etc/nginx/sites-available# systemctl restart nginx
root@621Bits-237:/etc/nginx/sites-available#

































root@621Bits-237:/etc/nginx/sites-available# subl odoo.mysite.co.conf
root@621Bits-237:/etc/nginx/sites-available# history
    1  sudo su apt-get install python-dateutil python-docutils python-feedparser python-gdata python-jinja2 python-ldap python-libxslt1 python-lxml python-mako python-mock python-openid python-psycopg2 python-psutil python-pybabel python-pychart python-pydot python-pyparsing python-reportlab python-simplejson python-tz python-unittest2 python-vatnumber python-vobject python-webdav python-werkzeug python-xlwt python-yaml python-zsi python-pip python-decorator  wkhtmltopdf python-requests python-pypdf python-passlib
    2  apt-get install nodejs
    3  cp /opt/Source/Eclipse/Java/Java.sh .
    4  ls
    5  update vim
    6  apt-get update vim
    7  update vim
    8  ls
    9  cd /opt/Source/Eclipse/Java
   10  ls
   11  cp Java.sh .
   12  ls
   13  cd ..
   14  cd /etc/profile.d/
   15  ls
   16  cp /opt/Source/Eclipse/Java/Java.sh .
   17  ls
   18  . Java.sh
   19  java
   20  javac
   21  cd pg_hba.conf pg_hba_backup.conf
   22  cp pg_hba.conf pg_hba_backup.conf
   23  ls
   24  vi pg_hba.conf
   25  cd /etc/postgresql/9.5/
   26  ls
   27  cd main
   28  ls
   29  vi pg_hba.conf
   30  cd ..
   31  /etc/init.d/postgresql restart
   32  /etc/modprobe.d
   33  cd /etc/modprobe.d
   34  ls
   35  vi alsa-base.conf
   36  sudo apt-get install libgtk2.0-0
   37  sudo apt-get install autopoint
   38  apt-get dist-upgrade
   39  cd /etc/profile.d/
   40  ls
   41  vi Java.sh
   42  lshw -C sound
   43  cat /proc/asound/cards
   44  cat /proc/asound/cardswget http://www.alsa-project.org/alsa-info.sh -O alsa-info.sh && bash alsa-info.sh
   45  wget http://www.alsa-project.org/alsa-info.sh -O alsa-info.sh && bash alsa-info.sh
   46  sudo modprobe snd-hda-intel
   47  apt-get upgrade
   48  apt-get downgrade
   49  sudo apt-get install ubuntu-desktop ubuntu-standard
   50  sudo apt-get install xserver-xorg-input-all xserver-xorg-video-all nvidia-common
   51  sudo apt-get install ubuntu-restricted-extras
   52  sudo pavucontrol
   53  gstreamer properties
   54  gstreame- properties
   55  gstreamer-properties
   56  sudo pavucontrol
   57  apt-get install libjpeg-dev
   58  pip install -I PIL
   59  После успешной установки проверьте р
   60  sudo apt-get install libjpeg62 libjpeg62-dev zlib1g-dev libfreetype6 libfreetype6-dev
   61  history | grep php
   62  apt-get purge apache2 php*
   63  apt-get purge apache2
   64  su susai
   65  apt-get purge apache2
   66  apt-get purge php*
   67  sudo apt-get install -f
   68  sudo apt-get install --fix-missing
   69  sudo apt-get autoremove
   70  sudo apt-get intall -f
   71  sudo apt-get install -f
   72  php -v
   73  apt-get intsall lamp-server^
   74  apt-get install lamp-server^
   75  su susai
   76  df -Th
   77  unmount /media/susai/JAKE
   78  umount /media/susai/JAKE
   79  dosfsck
   80  dosfsck -a /dev/sdb
   81  df -Th
   82  umount /media/susai/JAKE
   83  df -Th
   84  dosfsck -a /dev/sdb
   85  su postgres
   86  vi /etc/postgresql/9.5/main/pg_hba.conf
   87  systemctl restart postgresql
   88  su postgres
   89  cd /etc/postgresql/9.5/main/
   90  ls
   91  vi pg_hba.conf
   92  systemctl status postgresql
   93  systemctl stop postgresql
   94  systemctl status postgresql
   95  systemctl start postgresql
   96  systemctl status postgresql
   97  ifconfig
   98  vi pg_hba
   99  vi pg_hba.conf
  100  service postgresql restart
  101  vi pg_hba.conf
  102  systemctl restrt postgresql
  103  systemctl restart postgresql
  104  systemctl status postgresql
  105  psql -U odoo
  106  psql -U odoo -c tcuts
  107  psql -U odoo -d tcuts
  108  psql -U odoo -d tcuts_16
  109  vi pg_hba.conf
  110  systemctl stop postgresql
  111  systemctl status postgresql
  112  systemctl start postgresql
  113  systemctl status postgresql
  114  vi pg_hba.conf
  115  systemctl stop postgresql
  116  systemctl status postgresql
  117  systemctl start postgresql
  118  systemctl status postgresql
  119  vi pg_hba.conf
  120  systemctl restart postgresql
  121  vi pg_hba.conf
  122  ufw status
  123  psql -U bucardo
  124  psql -U bucardo -h 192.168.1.169
  125  ifconfig
  126  vi pg_hba.conf
  127  systemctl restart postgresql
  128  vi pg_hba.conf
  129  systemctl restart postgresql
  130  lsof -p:5432
  131  lsof -i:5432
  132  vi pg_hba.conf
  133  systemctl stop postgresql
  134  systemctl status postgresql
  135  systemctl start postgresql
  136  systemctl status postgresql
  137  vi pg_hba.conf
  138  exit
  139  cd /etc/postgresql/9.5/main/
  140  ls
  141  vi pg_hba.conf
  142  systemctl restart postgresql
  143  psql -U odoo10 -h 23.254.42.66
  144  ls
  145  cp postgresql.conf postgresql.conf.bk
  146  vi postgresql.conf
  147  cat pg_hba.conf
  148  ping odoo.mysite.co
  149  subl /etc/hosts
  150  ping odoo.mysite.co
  151  systemctl stop apache2
  152  systemctl status apache2
  153  systemctl status nginx
  154  systemctl restart nginx
  155  cd /etc/nginx/sites-available/
  156  ls
  157  subl odoo
  158  mv odoo odoo.mysite.co.conf
  159  subl odoo odoo.mysite.co.conf
  160  subl odoo.mysite.co.conf
  161  cd ../sites-enabled/
  162  ls
  163  rm -rf odoo
  164  cd ../sites-available/
  165  ls
  166  cat odoo.mysite.co.conf
  167  ln -s /etc/nginx/sites-available/odoo.mysite.co.conf /etc/nginx/sites-available/
  168  ls
  169  ln -s /etc/nginx/sites-available/odoo.mysite.co.conf /etc/nginx/sites-enabled/
  170  nginx -t
  171  systemctl restart nginx
  172  subl odoo.mysite.co.conf
  173  history


