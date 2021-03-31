from fastapi import FastAPI
import random
import string

app = FastAPI()


def rand(a, b):
    return random.randrange(a, b + 1)


@app.get('/encode/{text}')
def encode(text):
    key = ''.join(random.choice(string.ascii_letters) for i in range(rand(5, 10)))
    encoded = ''
    last_key = key

    for sign in text:
        key_sum = sum([ord(el) for el in list(last_key)])
        s = sum([int(el) for el in list(str(key_sum))])
        last_digit = int(str(key_sum)[-1]) + 1
        temp_key = str(chr(ord(sign) + s))
        temp_key += ''.join(random.choice(string.ascii_letters) for i in range(last_digit-1))
        last_key = temp_key
        encoded += temp_key
    return {'encoded': encoded, 'key': key}


@app.get('/decode/{text}/{key}')
def decode(text, key):
    decoded = ''
    while len(text) > 0:
        key_sum = sum([ord(el) for el in list(key)])
        last_digit = int(str(key_sum)[-1]) + 1
        s = sum([int(el) for el in list(str(key_sum))])
        decoded += chr(ord(text[0]) - s)
        key = text[:last_digit]
        text = text[last_digit:]
    return {'decoded': decoded}


@app.get('/')
def home():
    return {'key': 'Encoding/Decoding'}

