#!/bin/bash
touch LogFile
tail -n 1 /var/log/messages > LogFile
echo 'Logs collected' >> /var/log/messages