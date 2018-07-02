import json
import pandas as pd
# da="item.json"
# test=json.loads(da,)
# # df = pd.read_json('items.json',typ='series')
# print(da)

# with open("items.json",'r') as load_f:
#      load_dict = json.load(load_f)
#      print(load_dict)

json_str = '{"country":"Netherlands"}'
data = pd.read_json(json_str,typ='series')
print(data)
p=pd.read_csv('items.csv')
print(p['content'])