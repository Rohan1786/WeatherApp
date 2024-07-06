# forms.py
from django import forms
from .models import City

INDIAN_CITIES = [
     ('Belgaum', 'Belgaum'),
    ('Mumbai', 'Mumbai'),
    ('Delhi', 'Delhi'),
    ('Bengaluru', 'Bengaluru'),
    ('Hyderabad', 'Hyderabad'),
    ('Ahmedabad', 'Ahmedabad'),
    ('Chennai', 'Chennai'),
    ('Kolkata', 'Kolkata'),
    ('Surat', 'Surat'),
    ('Pune', 'Pune'),
    ('Jaipur', 'Jaipur'),
    ('Lucknow', 'Lucknow'),
    ('Kanpur', 'Kanpur'),
    ('Nagpur', 'Nagpur'),
    ('Indore', 'Indore'),
    ('Thane', 'Thane'),
    ('Bhopal', 'Bhopal'),
    ('Visakhapatnam', 'Visakhapatnam'),
    ('Pimpri-Chinchwad', 'Pimpri-Chinchwad'),
    ('Patna', 'Patna'),
    ('Vadodara', 'Vadodara'),
    ('Ghaziabad', 'Ghaziabad'),
    ('Ludhiana', 'Ludhiana'),
    ('Agra', 'Agra'),
    ('Nashik', 'Nashik'),
    ('Faridabad', 'Faridabad'),
    ('Meerut', 'Meerut'),
    ('Rajkot', 'Rajkot'),
    ('Kalyan-Dombivli', 'Kalyan-Dombivli'),
    ('Vasai-Virar', 'Vasai-Virar'),
    ('Varanasi', 'Varanasi'),
    ('Srinagar', 'Srinagar'),
    ('Aurangabad', 'Aurangabad'),
    ('Dhanbad', 'Dhanbad'),
    ('Amritsar', 'Amritsar'),
    ('Navi Mumbai', 'Navi Mumbai'),
    ('Allahabad', 'Allahabad'),
    ('Ranchi', 'Ranchi'),
    ('Howrah', 'Howrah'),
    ('Coimbatore', 'Coimbatore'),
    ('Jabalpur', 'Jabalpur'),
    ('Gwalior', 'Gwalior'),
    ('Vijayawada', 'Vijayawada'),
    ('Jodhpur', 'Jodhpur'),
    ('Madurai', 'Madurai'),
    ('Raipur', 'Raipur'),
    ('Kota', 'Kota'),
    ('Guwahati', 'Guwahati'),
    ('Chandigarh', 'Chandigarh'),
    ('Hubli-Dharwad', 'Hubli-Dharwad'),
    ('Mysore', 'Mysore')
   
]

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = forms.Select(choices=INDIAN_CITIES)
