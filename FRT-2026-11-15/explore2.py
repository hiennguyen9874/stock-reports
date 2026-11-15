
import sys; sys.path.insert(0, "../../.pi/skills/stock/stock-analysis/scripts")
from sstock_lib import Work, price_frame
w = Work(".")
px = price_frame(w.load("price"))
print(px.columns.tolist())
c = px["adjClose"] if "adjClose" in px else px["close"]
s = c["2026-09-01":]
print("since sep max", s.max(), s.idxmax(), "min", s.min(), s.idxmin())
s2 = c["2026-10-15":]; print("since oct15 max", s2.max(), s2.idxmax(), "min", s2.min(), s2.idxmin())
print(c["2026-09-01":"2026-09-05"])
print(c.tail(10))
