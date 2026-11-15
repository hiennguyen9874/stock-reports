
import json, pandas as pd
d=json.load(open("raw/valuation_1m.json")); d=d.get("data",d)
pb=d["charts"]["pb"]; s=pd.Series(pb["pb"] if isinstance(pb,dict) and "pb" in pb else pb.get("series",{}).get("pb"), index=pd.to_datetime(d["dates"]))
print(s.groupby(s.index.year).mean().round(2).to_dict())
