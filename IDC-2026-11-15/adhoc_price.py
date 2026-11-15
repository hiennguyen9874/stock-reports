import sys
sys.path.insert(0,'../../.pi/skills/stock/stock-analysis/scripts')
from sstock_lib import Work, price_frame
w=Work('.')
p=price_frame(w.load("price"))
print(p.columns.tolist())
t=p.tail(45)
print(t.to_string())
v=p.filter(regex='val|Val|gtgd|value',axis=1)
print(p.sort_values(p.columns[-1]).tail(3) if v.empty else v.squeeze().nlargest(5))
