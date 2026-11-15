
import sys, json; sys.path.insert(0, "../../.pi/skills/stock/stock-analysis/scripts")
from sstock_lib import Work, price_frame
w=Work("."); px=price_frame(w.load("price"))
print(px.columns.tolist())
c=px["adjClose"]
l=px.get("adjLow", c); h=px.get("adjHigh", c)
last=px.tail(260)
print("52w low date", last["adjClose"].idxmin(), last["adjClose"].min(), "high date", last["adjClose"].idxmax(), last["adjClose"].max())
r=px.loc["2026-08-15":]
print("since 15/8: min", r["adjClose"].min(), r["adjClose"].idxmin(), "max", r["adjClose"].max(), r["adjClose"].idxmax())
r=px.tail(20); print("20d min/max", r["adjClose"].min(), r["adjClose"].max())
print(px.tail(8)[["close","adjClose","matchedValue"]] if "matchedValue" in px else px.tail(8))
m=json.load(open("metrics.json")); print(json.dumps(m["price"], ensure_ascii=False)[:1500])
print(json.dumps(m.get("elite",{}), ensure_ascii=False)[:1200])
