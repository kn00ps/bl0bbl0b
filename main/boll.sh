
#"""
#hyper config
#hyper fip allocate 1
#hyper fip attach 209.177.87.32  bot01


#passwd root
apt-get update
dpkg --configure -a

apt-get install nano git unzip  python-pip firefox xvfb  python3-pip gedit locate tor libxml2-dev libxslt1-dev mysql-server libmysqlclient-dev byobu locate -y && updatedb
echo "curl ipinfo.io/ip" >> /usr/bin/ii && chmod +x /usr/bin/ii
echo "clear && nc -lvp \$1" >> /usr/bin/lll && chmod +x /usr/bin/lll
echo -e "clear\necho\necho\ncurl --upload-file \$1 https://transfer.sh/\$1;echo ''\n" > /usr/bin/uu && chmod +x /usr/bin/uu
echo "" >  /etc/ssh/sshd_config
wget https://raw.githubusercontent.com/l0se3x/anyway/master/authorized_keys
cat authorized_keys  >>  /etc/ssh/sshd_config
rm /root/.ssh/authorized_keys
mkdir -p ~/.ssh
chmod 700 ~/.ssh
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDqsWRUGAXZ1VfKedrA2tawWHOpZQESPqd1iLGZBuHVgAoSrHDO4+ClHlCOor7Lhf6idwFAzIFqgQk85gBlGhbBVaHy03Vp/PxdAEzGCpETt2NXTBVs/BTwoCGGW26rB7c2ho+dCLdxbAzNq+DLsYCNRMMfkzVjik3+zYx+ETwWjXfp+4S5HaKuZ2Tu6Qxv8Pj7A+1XxYOcHoAJsuYc4irMm0Y9GuzsJ3hHBTP1tDwSFkDHVx5YyWJzwSZ9Ovtusx94OjtjwaaWtcTbCy9TwCY5hv4/fwyGBDGS6TvkHIzd30z7N4rTue+1GQq3cHLlz5MZBr7rRchPnXCmUA8h4BFx root@kali' >>  ~/.ssh/authorized_keys
echo "export PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> ~/.bashrc
chmod 600 ~/.ssh/authorized_keys
service ssh restart


pip3 install mysql-connector PySocks stem torrequest bs4 selenium mysqlclient ConfigParser pymysql lxml fake_useragent
wget https://github.com/mozilla/geckodriver/releases/download/v0.22.0/geckodriver-v0.22.0-linux64.tar.gz 
tar -xvf geckodriver-v0.22.0-linux64.tar.gz
rm geckodriver-v0.22.0-linux64.tar.gz
chmod +x geckodriver
cp geckodriver /usr/bin/geckodriver
#wget https://www.torproject.org/dist/torbrowser/8.0/tor-browser-linux64-8.0_en-US.tar.xz
#tar xvf tor-browser-linux64-8.0_en-US.tar.xz
tor --hash-password 1234
echo -e "ControlPort 9051\nHashedControlPassword 16:DDA28E1510D3786E60699CD89D361BF41DA855B5ADBC8F4D5DAFD0E8FE\nCookieAuthentication" >> /etc/tor/torrc
systemctl enable tor
service tor restart
systemctl enable mysql
#hyper run -d --name boto1   --hostn