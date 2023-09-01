from shortener.models import URL_Table
import uuid
import os
import random
import string

def generate_unique_id(length=5):
    characters = string.ascii_letters + string.digits
    unique_id = ''.join(random.choice(characters) for _ in range(length))
    return unique_id


def add_url(original_url,user_id):
    
    unique_id = generate_unique_id()
    return URL_Table.objects.create(original_url=original_url, shortened_url=unique_id,user=user_id)