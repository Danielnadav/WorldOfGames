# import json
# import requests
# # def api_url():
# #     resp = requests.get('https://api.exchangeratesapi.io/latest')
# #     if resp.status_code == 200:
# #         print("works")
# #     else: print("url issue")
# #     git_value = resp
# #     for git_value in resp.json():
# #         return json.load(resp.content.decode('utf-8'))
# #         print(json.load(resp.content.decode))
#
#
#
#
#
# # #get_money_interval =  GET https://data.fixer.io/api/latest
# # print(resp)
# #
# #
#
# #
# # GET
# # https: // api.exchangeratesapi.io / latest
# # HTTP / 1.1
# #
#
# def get_account_info():
#
#  #   api_url = requests.get('https://api.exchangeratesapi.io/latest').json()
#     return api_url
#     feth
#         return json.loads()
#     print(json.loads())
#
#     # response = requests.get(api_url, headers=headers)
#     # if response.status_code == 200:
#     #     return json.loads(response.content.decode('utf-8'))
#     #     print(json.loads(response.content.decode('utf-8')))
#     # else:
#     #     return None
#     # print(response)
#     # print(api_url)
#
def home_work():

    import requests

    import json

# Where USD is the base currency you want to use
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    d1 = """{"'BRL'":"}"""
# Making our request
    response = requests.get(url)
    list = []
    data = response.json()



    print(data)

#     json.loads(d)              # Produces a dictionary out of the given string
# d2 = json.dumps(d)              # Produces a string out of a given dict or string
# d3 = json.dumps(json.loads(d))  # 'dumps' gets the dict from 'loads' this time

    print(str(d1, url))
# print "d2:  " + d2
# print "d3:  " + d3

home_work()





