# blog/templatetags/custom_tags.py
from datetime import date
import requests
from django import template

register = template.Library()

@register.simple_tag
def get_age():
    birth_date = date(2005, 7, 13)
    today = date.today()
    age = (today - birth_date).days // 365
    return age

@register.simple_tag
def get_geolocation():
    try:
        response = requests.get('http://ip-api.com/json/', timeout=5)
        data = response.json()
        if data['status'] == 'success':
            return f"📍{data['country']}, {data['city']}, {data['regionName']}"
        return "📍Location not available"
    except:
        return "📍Location not available"