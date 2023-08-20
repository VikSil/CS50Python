import requests
import sys
import json


def main():
    try:
        n = float(sys.argv[1])
    except:
        sys.exit("wrong command line argument")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("API request issue")

    dict = response.json()
    xrate = dict["bpi"]["USD"]["rate_float"]
    cost = float(xrate) * n
    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()
