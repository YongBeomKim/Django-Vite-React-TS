cd ../react
rm -rf dist
yarn build
cd ../django
deactivate
source ../.venv/bin/activate
rm -rf staticfiles
./manage.py collectstatic
./manage.py build
