
import sys, json; sys.path.insert(0, "../../.pi/skills/stock/stock-analysis/scripts")
from sstock_lib import Work, fa_frames, fa_series
w = Work(".")
fq = fa_frames(w.load("fa_q"))
print(list(fq.keys()))
for k in ["minorityInterest","finInvest","fixedAssets","cashBank","receivables","appropriatedDebt","buyerAdvancesShort","financialProfit","otherProfit","operatingProfit","financialExpense","sellingExpense","adminExpense","surplusRetainedFunds","charterCapital","totalCapital","depreciation"]:
    try:
        s = fa_series(fq, k); print(k, [round(x) if x==x else None for x in s.tail(8).values], list(s.tail(8).index))
    except Exception as e: print(k, "ERR", e)
