import phonenumbers
from phonenumbers import geocoder
number =+60108873726
num = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(num,"en"))
from phonenumbers import carrier
s_num = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(s_num,"en"))
