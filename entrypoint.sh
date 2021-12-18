#!/usr/bin/env sh

echo "Starting"

#    export PATH=$PATH:$HOME/Downloads/redis-stable/src
#    redis-server --port 6379

#uWSGI:
#        sudo ln -s /home/maxim1106/HillelProjects/log_app/supervisor/production.conf /etc/supervisor/conf.d/log_app.conf
#        sudo supervisorctl update
#        sudo supervisorctl status
#
#        * sudo service supervisord stop
#        * sudo supervisord -c /etc/supervisor/supervisord.conf
#
#        * sudo service supervisord reload
#        * sudo supervisorctl restart all

#    Nginx:
#        sudo ln -s /home/maxim1106/HillelProjects/log_app/nginx/production.conf /etc/nginx/sites-enabled/log_app.conf
#        sudo nginx -t
#        sudo nginx -s reload
#
#        * ps -ef | grep nginx
#        * service nginx start