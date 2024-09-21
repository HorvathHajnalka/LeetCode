
    response_json = response.json()
    print('fact: ' + response_json['fact'])
    print('length: ' + str(response_json['length']))
else:
    print(response.status_code)

