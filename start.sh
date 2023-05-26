#!/bin/bash
#
# metadata_begin
# recipe: Hestia Control Panel
# tags: debian9,debian10,ubuntu1804,ubuntu2004
# revision: 1.0
# description_ru: Установка панели управления Hestia. Данные для подключения и пароль можно найти в файле /root/hestiacp_info.txt на виртуальном сервере.
# description_en: Installing Hestia Control Panel. Connection information and password can be found in the file /root/hestiacp_info.txt on virtual server.
# metadata_end
#

set -x
RNAME="Hestia Control Panel"

set -x

LOG_PIPE=/tmp/log.pipe.$$                                                                                                                                                                                                                    
mkfifo ${LOG_PIPE}
LOG_FILE=/root/hestia.log
touch ${LOG_FILE}
chmod 600 ${LOG_FILE}

tee < ${LOG_PIPE} ${LOG_FILE} &

exec > ${LOG_PIPE}
exec 2> ${LOG_PIPE}

killjobs() {
	jops="$(jobs -p)"
	test -n "${jops}" && kill ${jops} || :
}
trap killjobs INT TERM EXIT

echo
echo "=== Recipe ${RNAME} started at $(date) ==="
echo

HOME=/root
export HOME

# Detect Total Memory
memt=$(grep MemTotal /proc/meminfo | awk '{print $2}')

# Change system limits
echo "fs.file-max=512000" >> /etc/sysctl.conf
sysctl -w fs.file-max=512000
echo "*                soft    nproc           65536" >> /etc/security/limits.conf
echo "*                hard    nproc           65536" >> /etc/security/limits.conf
echo "*                hard    nofile          65536" >> /etc/security/limits.conf
echo "*                soft    nofile          65536" >> /etc/security/limits.conf
echo "*                hard    memlock         65536" >> /etc/security/limits.conf
echo "*                soft    memlock         65536" >> /etc/security/limits.conf

# Upgrade OS
apt update
apt --yes -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" upgrade

# Instal Hestia Control Panel
wget https://raw.githubusercontent.com/hestiacp/hestiacp/release/install/hst-install.sh
chmod +x hst-install.sh

bash hst-install.sh --interactive no --email ($EMAIL) --password ($PASS) --hostname ($HOSTNAME) -f

rm hst-install.sh
rm hst-install-ubuntu.sh

echo "Connect information to Hestia Control Panel" >> /root/hestiacp_info.txt
echo "Admin address: https://"($IPv4)":8083" >> /root/hestiacp_info.txt
echo "Login: admin" >> /root/hestiacp_info.txt
echo "Password: "($PASS) >> /root/hestiacp_info.txt

exit 0
