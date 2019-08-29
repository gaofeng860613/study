import json


class bank_json:

    def json_write(self, card_id, password):
        dict_json = {'card_id': card_id, 'password': password}
        res = json.dumps(dict_json)
        with open('bank_json.txt', 'a+') as f:
            f.write(res)

    def json_read(self):
        with open('bank_json.txt', 'r+') as f:
            res = f.readline()
            return res
