#
# import requests
# import json
#
# def RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key):
#     # importing required libraries
#     import requests, json
#
#     # base_url variable store base url
#     base_url = "https://api.exchangerate-api.com/v4/latest/USD"
#
#     # main_url variable store complete url
#     main_url = base_url + "&from_currency =" + from_currency + "&to_currency =" + to_currency + "&apikey =" + api_key
#
#     # get method of requests module
#
#
# # return response object
# req_ob = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
#
# # json method return json format
# # data into python dictionary data type.
#
# # result contains list of nested dictionaries
# result = req_ob.json()
# print(result)
# print(" Result before parsing the json data :\n", result)
#
# print("\n After parsing : \n Realtime Currency Exchange Rate for",
#       result["'BRL':"]
#       ["2. From_Currency Name"], "TO",
#       result["Realtime Currency Exchange Rate"]
#       ["4. To_Currency Name"], "is",
#       result["Realtime Currency Exchange Rate"]
#       ['5. Exchange Rate'], to_currency)
#
# # Driver code
# if __name__ == "__main__":
#     # currency code
#     from_currency = "USD"
#     to_currency = "NIS"
#
#     # enter your api key here
#     api_key = "https://api.exchangerate-api.com/v4/latest/USD"
#
#     # function calling
#     RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key)

import json
import requests


    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url).json()
    json_data = json.loads(response.text)
    result = json_data['data']['BRL']
    print (result)