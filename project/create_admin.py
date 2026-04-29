import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()

from django.contrib.auth.models import User

username = 'admin'
password = 'adminpassword123'
email = 'admin@example.com'

user = User.objects.filter(username=username).first()
if user:
    user.set_password(password)
    user.save()
    print("Admin password has been reset.")
else:
    User.objects.create_superuser(username, email, password)
    print("Admin superuser account has been created.")
