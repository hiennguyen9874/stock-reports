import sys; sys.path.insert(0, "../../.pi/skills/stock/stock-analysis/scripts")
from sstock_lib import Work, price_frame, fa_frames, fa_series
import pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
w = Work(".")
fq = fa_frames(w.load("fa_q"))
for k,df in fq.items():
    print("==",k, list(df.columns))
names=["charterCapital","appropriatedDebt","buyerAdvancesShort","financialProfit","otherProfit","minorityInterest","otherAssets","fixedAssets","financialExpense","equity","totalAssets","netProfit","netProfitParent","shortTermDebt","longTermDebt","unearnedRevenue"]
rows={}
for n in names:
    try:
        s=fa_series(fq,n); rows[n]=s
    except Exception as e: print("miss",n,e)
print(pd.DataFrame(rows).tail(10).round(1).T)
fy = fa_frames(w.load("fa_y"))
rows={}
for n in ["charterCapital","appropriatedDebt","financialProfit","investing","operating","netProfitParent","constructionWip","inventory","cashBank"]:
    try: rows[n]=fa_series(fy,n)
    except Exception as e: print("missy",n,e)
print(pd.DataFrame(rows).round(0).T)
