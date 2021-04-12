# setUp.py

def url(sli):
    from urllib.request import urlopen
    port = str(5544+sli)
    try:
        u = urlopen('http://localhost:'+port).read()
    except:
        u = '............. no server'
    return u
