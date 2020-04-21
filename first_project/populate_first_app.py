import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# fake script

import random
from first_app.models import Topic, AccessRecord, WebPage
from faker import Faker

fake_gen = Faker()
topics = ['search', 'social','news', 'games']


def add_topics():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        top = add_topics()  # getting the topic for the entry
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        # create new web page entry

        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create fake access record for that web page

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populated!')