
import sys, json; sys.path.insert(0, "../../.pi/skills/stock/stock-analysis/scripts")
from sstock_lib import Work, fa_frames, price_frame
w = Work(".")
fq = fa_frames(w.load("fa_q"))
import pandas as pd
pd.set_option("display.width",250); pd.set_option("display.max_columns",30)
for cid in ["capital","asset","costStructure"]:
    print(cid); print(fq[cid].tail(5).round(1).T)
px = price_frame(w.load("price"))
print(px.tail(25)[["close","adjClose","matchedValue","putThroughValue"]] if "adjClose" in px else px.tail(25))
print(px.columns.tolist())
