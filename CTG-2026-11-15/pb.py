
import json
d=json.load(open("raw/valuation_1m.json"))["data"]
dates=d["dates"]; pb=d["charts"]["pb"]["pb"] if isinstance(d["charts"]["pb"],dict) and "pb" in d["charts"]["pb"] else None
if pb is None: print(d["charts"]["pb"].keys() if isinstance(d["charts"]["pb"],dict) else d["charts"]["pb"][:2])
else:
  for i,x in enumerate(dates):
    if x[5:7]=="12" or i==len(dates)-1: print(x, pb[i])
