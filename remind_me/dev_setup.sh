sudo apt-get update
sudo apt-get install build-essential python3.4 python3.4-dev libpq-dev python-virtualenv g++ vim
sudo apt-get install flex bison gperf perl libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev
sudo apt-get install libpng-dev libjpeg-dev libx11-dev libxext-dev npm nodejs-legacy ruby
sudo apt-get install -y software-properties-common python-software-properties python-pip

# Setting up virtual environment
sudo pip install virtualenvwrapper
export WORKON_HOME=$HOME/Env
source /usr/local/bin/virtualenvwrapper.sh

# Setting up application
mkvirtualenv -p /usr/bin/python3.4 remind_me
export DJANGO_SETTINGS_MODULE=remind_me.settings
cd /vagrant

pip install -r requirements.txt

touch remind_me.db
chmod 776 remind_me.db
python manage.py migrate

# Setting up application settings at the time of vagrant login
echo 'export WORKON_HOME=$HOME/Env' >> /home/vagrant/.bashrc
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> /home/vagrant/.bashrc
echo 'workon remind_me && cd /vagrant' >> /home/vagrant/.bashrc
echo 'export DJANGO_SETTINGS_MODULE=remind_me.settings' >> /home/vagrant/.bashrc
echo 'python manage.py runserver 0.0.0.0:8000' >> /home/vagrant/.bashrc
