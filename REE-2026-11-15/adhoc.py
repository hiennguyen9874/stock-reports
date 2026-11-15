
import sys, json; sys.path.insert(0, "../../.pi/skills/stock/stock-analysis/scripts")
from sstock_lib import Work, price_frame, fa_frames, fa_series
import pandas as pd
pd.set_option("display.width",250); pd.set_option("display.max_columns",30)
w = Work(".")
fq = fa_frames(w.load("fa_q"))
keys=["financialProfit","otherProfit","operatingProfit","fixedAssets","constructionWip","finInvest","minorityInterest","debt","charterCapital","financing","investing","financialExpense","sellingExpense","adminExpense","depreciation","cogs","receivables","cashEndOfPeriod"]
rows={}
for k in keys:
    try:
        s=fa_series(fq,k); rows[k]=s.tail(8)
    except Exception as e: rows[k]=str(e)
for k,v in rows.items(): print(k, v.round(0).to_dict() if hasattr(v,"round") else v)
px = price_frame(w.load("price"))
print(px.columns.tolist())
print(px.tail(8))
m=json.load(open("metrics.json"))
print(json.dumps(m.get("elite"),ensure_ascii=False)[:1500])
print(json.dumps(m.get("price"),ensure_ascii=False)[:1500])
