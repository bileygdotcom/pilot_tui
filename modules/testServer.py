# setUp.py

def url():
    from urllib.request import urlopen
    try:
        u = urlopen('http://localhost:5545').read()
    except:
        u = '............. no server'
    return u
