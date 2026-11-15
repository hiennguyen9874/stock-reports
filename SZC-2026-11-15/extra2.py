import sys; sys.path.insert(0, "../../.pi/skills/stock/stock-analysis/scripts")
from sstock_lib import Work, fa_frames, fa_series, price_frame
import pandas as pd, json
pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
w = Work(".")
fq = fa_frames(w.load("fa_q"))
rows={n:fa_series(fq,n) for n in ["charterCapital","debt","surplusRetainedFunds","financing","operating","investing","cashBank","cashEndOfPeriod","appropriatedDebt","buyerAdvancesShort","depreciation","cogs","grossProfit","adminExpense","sellingExpense"]}
print(pd.DataFrame(rows).round(0).T.iloc[:, :9])
px = price_frame(w.load("price"))
print(px.columns.tolist())
print(px.loc["2024-01-02":"2024-01-10"])
print(px.loc["2026-09-08":"2026-09-15"])
print(px.loc["2026-05-20":"2026-06-05"][[c for c in px.columns if c in ("close","adjClose","matchedValue","putThroughValue")]])
