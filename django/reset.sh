rm db.sqlite3
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

./manage.py makemigrations core && ./manage.py migrate core
#./manage.py makemigrations app_info && ./manage.py migrate app_info
#./manage.py makemigrations app_cooking && ./manage.py migrate app_cooking
#./manage.py makemigrations app_count && ./manage.py migrate app_count
#./manage.py makemigrations app_food && ./manage.py migrate app_food
#./manage.py makemigrations app_ingredient && ./manage.py migrate app_ingredient
./manage.py makemigrations && ./manage.py migrate
