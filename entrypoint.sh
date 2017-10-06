#!/bin/bash
set -e

# Get the maximum upload file size for Nginx, default to 0: unlimited
USE_NGINX_MAX_UPLOAD=${NGINX_MAX_UPLOAD:-0}
# Generate Nginx config for maximum upload file size
echo "client_max_body_size $USE_NGINX_MAX_UPLOAD;" > /etc/nginx/conf.d/upload.conf

# mkdir /home/LogFiles
# touch /home/LogFiles/python_$WEBSITE_ROLE_INSTANCE_ID_out.log
# echo "$(date) Container started" >> /home/LogFiles/python_$WEBSITE_ROLE_INSTANCE_ID_out.log

exec "$@"

