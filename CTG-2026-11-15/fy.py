
import sys; sys.path.insert(0, "../../.pi/skills/stock/stock-analysis/scripts")
from sstock_lib import Work, fa_frames
import pandas as pd
pd.set_option("display.width",250)
fy=fa_frames(Work(".").load("fa_y"))
print(fy["costStructure"].T.round(0)); print(fy["profitStructure"].T.round(0))
