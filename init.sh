# VSCODE Setting
mkdir .vscode logs media
cd .vscode
json='{"python.defaultInterpreterPath": "./.venv/bin/python"}'
echo "$json" > settings.json
cd ..

# Python Virtual ENV & install module
python3.11 -m venv .venv
cd .venv
. bin/activate
cd ..

cd django
pip install --upgrade pip
pip install wheel
pip install -r requirements.txt -U

# Setting Files
# db.ini : for PSQL
# settings.json : for Django 
cat << EOF > pyscript.py
# PSQL DB Setting
import configparser
config = configparser.ConfigParser()
config['mysqllocal'] = {
    'engine': 'django.db.backends.mysql',
    'name': 'DBNAME',
    'user': 'DBUSERNAME',
    'password':'DBPASSWORD',
    'host':'localhost',
    'port':'3306'
}

config['PSQL'] = {
    'engine': 'django.db.backends.postgresql',
    'name': 'DBNAME',
    'user': 'DBUSERNAME',
    'password':'DBPASSWORD',
    'host':'localhost',
    'port':'5432'}

config['mysql'] = {
    'engine': 'django.db.backends.mysql',
    'name': 'DBNAME',
    'user': 'DBUSERNAME',
    'password':'DBPASSWORD',
    'host':'localhost',
    'port':'3306'
}

with open('db.ini', 'w') as data:
    config.write(data)

# Django Setting
import json
from django.core.management.utils import get_random_secret_key
data =  {
    "LANGUAGE_CODE" : "en-us",
    "SECRET_KEY" : get_random_secret_key(),
}
file_path = 'settings.json'
# with open(file_path, 'w') as f:
#     json.dump(data, f)
EOF

./manage.py shell < ./pyscript.py
# python ./pyscript.py
rm ./pyscript.py
source reset.sh
cd ..

## FrontEnds
# yarn create vite react --template react-ts
cd react
yarn install
yarn build
# yarn add -D aos axios hamburger-react styled-normalize
# yarn add -D react-helmet-async react-icons react-router-dom
# yarn add -D @types/node @types/aos @types/react-router-dom
# yarn add -D styled-components @types/styled-components
# yarn add -D react-cookie
# yarn add -D tailwindcss postcss autoprefixer
# npx tailwindcss init
cd ..
# yarn install
# cd react
# yarn install


# Django Produce Build
cd django
source build.sh
cd ..
