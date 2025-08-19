import requests
import sys
try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=7b1f8f06b7503db545bf53a8cbfad50b8e6a37cc55f3830c803eeaced4e70036")
    response.raise_for_status()
    
except requests.RequestException:
    sys.exit("Server issue")


r = response.json()
k = r['data']
price = float(k['priceUsd'])
def main():
    if len(sys.argv) == 2:
        s = float_check(sys.argv[1])
        result = price * s
        print(f"${result:,.4f}")
    else:
        sys.exit("Missing command-line argument")

def float_check(s):
    try:
        n = float(s)
        return n
    except ValueError:
        sys.exit("Command-line argument is not a number")


main()
