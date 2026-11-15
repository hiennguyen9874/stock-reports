import sys; sys.path.insert(0, "../../.pi/skills/stock/stock-analysis/scripts")
from sstock_lib import Work, price_frame
import pandas as pd
w=Work("."); px=price_frame(w.load("price"))
y=px.iloc[-250:]
print("hi",y.adjClose.idxmax(),y.adjClose.max(),"lo",y.adjClose.idxmin(),y.adjClose.min())
print(px[["close","adjClose","matchedValue","netForeignValue"]].iloc[-25:].assign(mv=lambda d:(d.matchedValue/1e9).round(1),nf=lambda d:(d.netForeignValue/1e9).round(1)).drop(columns=["matchedValue","netForeignValue"]))
print(px.loc["2026-02-01":"2026-02-28",["close","adjClose"]].assign(mv=px.matchedValue/1e9, nf=px.netForeignValue/1e9).round(1).to_string())
