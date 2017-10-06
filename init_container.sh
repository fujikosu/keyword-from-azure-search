#!/bin/bash
service ssh start
mkdir /home/LogFiles
touch /home/LogFiles/python_$WEBSITE_ROLE_INSTANCE_ID_out.log
echo "$(date) Container started" >> /home/LogFiles/python_$WEBSITE_ROLE_INSTANCE_ID_out.log
python /code/app.py
