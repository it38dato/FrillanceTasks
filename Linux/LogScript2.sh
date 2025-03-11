#!/bin/bash
logger -p local1.debug "This is normal log -> debug"
echo 'local1.*                                                /var/log/mylog.debug' >> /etc/rsyslog.conf

logger -p local2.err "This is error -> error"
echo 'local2.*                                                                                          /var/log/mylog.error' >> /etc/rsyslog.conf

logger -p local3.crit "This is critical error -> crit"
echo 'local3.*                                                                                          /var/log/mylog.crit' >> /etc/rsyslog.conf

sudo systemctl restart rsyslog
#sudo touch /etc/logrotate.d/mylogdebug.conf
#sudo touch /etc/logrotate.d/mylogerror.conf
#sudo touch /etc/logrotate.d/mylogcrit.conf
echo '/var/log/mylog.debug
{
  dateext
  daily
  rotate 5
  compress
}' > /etc/logrotate.d/mylogdebug.conf
sudo logrotate -f /etc/logrotate.d/mylogdebug.conf

echo '/var/log/mylog.error
{
  dateext
  daily
  rotate 5
  delaycompress
}' > /etc/logrotate.d/mylogerror.conf
sudo logrotate -f /etc/logrotate.d/mylogerror.conf

echo '/var/log/mylog.crit
{
  dateext
  weekly
  rotate 5
}' > /etc/logrotate.d/mylogcrit.conf
sudo logrotate -f /etc/logrotate.d/mylogcrit.conf