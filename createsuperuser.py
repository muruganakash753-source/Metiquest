import os
import django

# 1. Point this to your project's settings file
# IMPORTANT: Change 'metiquest' to your actual project folder name if it's different!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metiquest.settings') 

# 2. Initialize Django
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

# 3. Pull credentials from Render's Environment Variables
# (It falls back to these default strings if you forget to add them in Render)
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

# 4. Safely create the user
if not User.objects.filter(username=username).exists():
    print(f"Creating superuser: {username}")
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created successfully!")
else:
    print(f"Superuser '{username}' already exists. Skipping creation.")