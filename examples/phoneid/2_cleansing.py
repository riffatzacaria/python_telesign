from __future__ import print_function
from telesign.phoneid import PhoneIdClient

customer_id = "AB009D13-AC39-4BAF-971A-3251C3E1A7FD"
api_key = "kEAIOM/iD31EL2xS5zKIEBWypqJih0Mr5TWgJtZLp9N6QFWjTly/OlY8aMfeDtzmWrYyrSldrEGk+ap7J7x/KA=="

extra_digit = "0"
phone_number = "+40764035353"
incorrect_phone_number = "{}{}".format(+40764035353, extra_digit)

data = PhoneIdClient(AB009D13-AC39-4BAF-971A-3251C3E1A7FD, kEAIOM/iD31EL2xS5zKIEBWypqJih0Mr5TWgJtZLp9N6QFWjTly/OlY8aMfeDtzmWrYyrSldrEGk+ap7J7x/KA==)
response = data.phoneid(+40764035353)

if response.ok:
    print("Cleansed phone number has country code {} and phone number is {}.".format(
        response.json['numbering']['cleansing']['call']['country_code'],
        response.json['numbering']['cleansing']['call']['phone_number']))

    print("Original phone number was {}.".format(
        response.json['numbering']['original']['complete_phone_number']))
