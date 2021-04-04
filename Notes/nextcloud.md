## install
sudo apt update
sudo apt install apache2 mariadb-server libapache2-mod-php7.4  -y
sudo apt install php7.4-gd php7.4-mysql php7.4-curl php7.4-mbstring php7.4-intl -y
sudo apt install php7.4-gmp php7.4-bcmath php-imagick php7.4-xml php7.4-zip -y




CREATE USER 'gl'@'localhost' IDENTIFIED BY 'glin';
CREATE DATABASE IF NOT EXISTS nextcloud CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
GRANT ALL PRIVILEGES ON nextcloud.* TO 'gl'@'localhost';
FLUSH PRIVILEGES;


cd /var/www
wget https://download.nextcloud.com/server/releases/nextcloud-21.0.0.zip
unzip nextcloud-21.0.0.zip



Alias /nextcloud "/var/www/nextcloud/"

<Directory /var/www/nextcloud/>
  Require all granted
  AllowOverride All
  Options FollowSymLinks MultiViews

  <IfModule mod_dav.c>
    Dav off
  </IfModule>
</Directory>


sudo -u www-data php occ  maintenance:install --database \
"mysql" --database-name "nextcloud"  --database-user "gl" --database-pass \
"glin" --admin-user "admin" --admin-pass "password"


see https://curl.haxx.se/libcurl/c/libcurl-errors.html) for https://github.com/nextcloud/calendar/releases/download/v2.2.0/calendar.tar.gz

Carnet
Powerful note taking app available on android

## extension

## 使用


## 备份,迁移
