from poll import Poll
import mlab
import string
from random import choice

#1.Connect to DB
mlab.connect()

#2.Prepare Data
q = "Hackathon an gi?"
opts = [
    "Pizza",
    "Banh mi Hoi An",
    "Pho xao",
]
alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
c = ""
for _ in range(6):
    c += choice(alphabet)

#3.Create Document
p = Poll(question = q, options = opts, code = c)

#4.Save
p.save()
