#!/usr/bin/env python3

from requests_tor import RequestsTor

requests = RequestsTor(tor_ports=(9050,),tor_cport=9051)

url =  "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/"
r = requests.get(url)

print(r.text)


