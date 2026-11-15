
import sys, json; sys.path.insert(0, "../../.pi/skills/stock/stock-analysis/scripts")
from sstock_lib import Work, price_frame, fa_frames, fa_series
import pandas as pd
pd.set_option("display.width",250); pd.set_option("display.max_columns",30)
w = Work(".")
fq = fa_frames(w.load("fa_q"))
for k in ["asset","capital","costStructure","loanStructure"]:
    print(k); print(fq[k].tail(6).T.round(1))
fy = fa_frames(w.load("fa_y"))
print(fy["profitability"].T.round(2))
print(fy["loanStructureBySector"].tail(3).T.round(0))
m = json.load(open("metrics.json"))
print(json.dumps(m.get("valuation",{}), ensure_ascii=False)[:3000])
