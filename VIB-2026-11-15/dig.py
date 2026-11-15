
import sys, json; sys.path.insert(0, "../../.pi/skills/stock/stock-analysis/scripts")
from sstock_lib import Work, fa_frames
import pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
w=Work(".")
fq=fa_frames(w.load("fa_q"))
for k in ["capital","asset","costStructure"]:
    print(k); print(fq[k].tail(6).round(0).T)
v=w.load("valuation_1m")
print(json.dumps(v)[:1500])
