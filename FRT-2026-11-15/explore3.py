
import sys; sys.path.insert(0, "../../.pi/skills/stock/stock-analysis/scripts")
from sstock_lib import Work, fa_frames, fa_series
for wd in [".", "../HPG-2026-11-14", "../IDC-2026-11-14"]:
    try:
        w = Work(wd); fq = fa_frames(w.load("fa_q"))
    except Exception as e:
        print(wd, "skip", e); continue
    cb = fa_series(fq,"cashBank"); ce = fa_series(fq,"cashEndOfPeriod"); fi=fa_series(fq,"finInvest"); inv=fa_series(fq,"investing")
    print(wd); print((cb.tail(6).round()).tolist()); print(ce.tail(6).round().tolist()); print(fi.tail(6).round().tolist()); print(inv.tail(6).round().tolist())
