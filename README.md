# EON Web Py  
Simple python web back-end  

    # adduser developer
    # usermod -aG sudo developer
    # visudo
    # sudo su - developer
    $ cat id_rsa.pub >> ~/.ssh/authorized_keys
    $ sudo apt-get install upstart
    $ reload(ssh)
    $ sudo apt-get update
    $ sudo apt-get upgrade --assume-no
    $ sudo apt-get upgrade --assume-yes
    $ sudo apt-get update
    $ sudo apt-get install python3-pip python3-dev nginx
    $ sudo pip3 install virtualenv
    $ mkdir ~/myproject
    $ cd ~/myproject
    $ virtualenv myprojectenv
    $ source myprojectenv/bin/activate
    (myprojectenv) $ pip install gunicorn flask
    (myprojectenv) $ vi ~/myproject/myproject.py
    (myprojectenv) $ sudo ufw allow 5000
    (myprojectenv) $ python myproject.py (CTRL + C)
    (myprojectenv) $ vi ~/myproject/wsgi.py
    (myprojectenv) $ cd ~/myproject/
    (myprojectenv) $ gunicorn --bind 0.0.0.0:5000 wsgi:app
    (myprojectenv) $ deactivate
    $ cd
    $ sudo vi /etc/systemd/system/myproject.service
    $ sudo systemctl start myproject
    $ sudo systemctl enable myproject
    $ sudo vi /etc/nginx/sites-available/myproject
    $ sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
    $ sudo nginx -t
    $ sudo systemctl restart nginx
    $ sudo ufw delete allow 5000
    $ sudo ufw allow 'Nginx Full'

## Restart after Python code changes  

    $ sudo systemctl restart myproject
