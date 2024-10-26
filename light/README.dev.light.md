# Basic build guide

```bash
python3 -m venv venv
source venv/bin/activate
# pip install -r requirements.txt # ?
pip install Django Django-ninja chromadb openai
cd yoyj_feature_dev_insight
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
# yourname password
python manage.py runserver
```

Next, try visit {{your_ip}}:8000/admin/ to see if the server is running.
Then, you can visit {{your_ip}}:8000/api/docs/ to see the API documentation.
