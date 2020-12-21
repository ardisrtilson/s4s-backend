rm -rf s4sbackendapi/migrations
rm db.sqlite3
python manage.py makemigrations s4sbackendapi
python manage.py migrate
python manage.py loaddata Sexes
python manage.py loaddata User
python manage.py loaddata s4sUser
python manage.py loaddata Samples
python manage.py loaddata SampleRatings
python manage.py loaddata Comments
python manage.py loaddata SpectralData
python manage.py loaddata UserFavorites
python manage.py loaddata tokens