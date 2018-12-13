# Byte-Flipping

Perform byte flipping attack against vulnerable cookies.

```python
$./byte-flip.py -h
usage: byte-flip.py [-h] -u URL -n COOKIENAME -v COOKIEVALUE -e ENCODING -s
                    STRING

Process some integers.

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     URl to request (https://web.com/path.php)
  -n COOKIENAME, --cookiename COOKIENAME
                        Cookie to play with (cookie of "bdmin")
  -v COOKIEVALUE, --cookievalue COOKIEVALUE
                        Cookie to play with (cookie of "bdmin")
  -e ENCODING, --encoding ENCODING
                        Encoding used: hex_low, hex_upp, base64,
                        base64_urlsafe
  -s STRING, --string STRING
                        String to search for in the response of the server


python3 byte-flip.py -u <URL> -n <cookie_name> -v <cookie_value> -e <hex_low or hex_upp or base64 or base64_urlsafe> -s <String_to_search_in_response>
python3 byte-flip.py -u http://web.com/index.php -n auth -v aET7FNm19aieDs2pPyAqSQ== -e base64 -s admin
```

All the parameters are required
