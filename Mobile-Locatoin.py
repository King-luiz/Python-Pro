import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+254727638320")
phone_number2 = phonenumbers.parse("+254112876340")
phone_number3 = phonenumbers.parse("+254705776973")
phone_number4 = phonenumbers.parse("+254727638320")


print ("\nPhone Number Location\n")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
print(geocoder.description_for_number(phone_number3,"en"))
print(geocoder.description_for_number(phone_number4,"en"))

#LETS TRACK PHONE NUMBERS