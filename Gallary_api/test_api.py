import os
import django
import json
import sys

# Setup Django
sys.path.append('e:/Practice(Python)/DRF/Gallary_API/Gallary_api')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Gallary_api.settings')
django.setup()

from django.conf import settings
# Fix DisallowedHost error
if 'testserver' not in settings.ALLOWED_HOSTS:
    settings.ALLOWED_HOSTS.append('testserver')

from rest_framework.test import APIRequestFactory, force_authenticate
from gallary.views import PhotoViewSet
from django.contrib.auth import get_user_model

User = get_user_model()
user = User.objects.first()
factory = APIRequestFactory()
view = PhotoViewSet.as_view({'get': 'list'})

# Make API request
request = factory.get('/gallary/photos/', {'album': '1'})
force_authenticate(request, user=user)
response = view(request)

print(f"Status Code: {response.status_code}")
try:
    print(json.dumps(response.data, indent=2, default=str))
except Exception as e:
    print(f"Error printing JSON: {e}")
    print(response.data)
