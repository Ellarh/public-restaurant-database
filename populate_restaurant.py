import os

# Configure settings for project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant.settings')

import django
django.setup()

from faker import Faker
from home.models import Restaurant

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        # Create Fake Data for entry
        fake_restaurant_name = fakegen.company()
        fake_address = fakegen.address()
        fake_city = fakegen.city()
        fake_state = fakegen.state()
        fake_url = fakegen.url()
        # fake_phone_number = str(fakegen.phone_number())
        # fake_date = fakegen.date()
        # fake_image = fakegen.image()

        # Create new Entry
        user = Restaurant.objects.get_or_create(
            name=fake_restaurant_name, address=fake_address, city=fake_city, state=fake_state,
            website=fake_url
        )


if __name__ == '__main__':
    print('Populating database')
    populate(10)
    print('Populating Complete.')