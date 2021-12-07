import phonenumbers
from num import number

from phonenumbers import geocoder
Loc_num = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(Loc_num,"en"))

from phonenumbers import carrier
service_num = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_num,"en"))