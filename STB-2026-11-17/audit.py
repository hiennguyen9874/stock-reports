import sys,json
from pathlib import Path
sys.path.insert(0,sys.argv[2])
from sstock_lib import Work,fa_frames,price_frame
w=Work(sys.argv[1]); fq=fa_frames(w.load('fa_q')); fy=fa_frames(w.load('fa_y'))
q=fq['loanStructureByQuality']; asset=fq['asset']; cap=fq['capital']; r=fq['rateBadDebt']; ps=fq['profitStructure']; cr=fq['costStructure']; px=price_frame(w.load('price'))
result={'quality':[]}
for p in q.index[-5:]:
 row=q.loc[p]; bad=sum(row[k] for k in ['lossLoans','doubtfulLoans','substandardLoans']); classified=sum(row[k] for k in ['lossLoans','doubtfulLoans','substandardLoans','watchLoans','standardLoans']); gross=asset.loc[p,'customerLoans']+row['loanLossProvision']
 result['quality'].append({'period':str(p),'grossLoans':gross,'netCustomerLoans':asset.loc[p,'customerLoans'],'classified':classified,'group2':row['watchLoans'],'group3':row['substandardLoans'],'group4':row['doubtfulLoans'],'group5':row['lossLoans'],'nplAmount':bad,'provisionBalance':row['loanLossProvision'],'nplRecalc':100*bad/gross,'group2PctRecalc':100*row['watchLoans']/gross,'group2to5PctRecalc':100*(bad+row['watchLoans'])/gross,'npl2Source':r.loc[p,'npl2Pct'],'llrRecalc':100*row['loanLossProvision']/bad,'llrSource':r.loc[p,'llrPct'],'vamc':row['vamcBonds']})
result['funding']=[]
for p in cap.index[-5:]:
 result['funding'].append({'period':str(p),**{k:cap.loc[p,k] for k in ['customerDeposits','interbankFunding','valuablePapers','govAndSbvDebt','charterCapital','surplusRetainedFunds','otherCapital']},'interbankAssets':asset.loc[p,'depositsLoansToOtherCIs'],'netInterbank':cap.loc[p,'interbankFunding']-asset.loc[p,'depositsLoansToOtherCIs'],'totalAssets':asset.loc[p,'totalAssets'],'otherAssets':asset.loc[p,'otherAssets']})
result['serviceShares']=[{'period':str(p),'serviceShare':100*ps.loc[p,'serviceIncome']/sum(ps.loc[p,k] for k in ['netInterestIncome','serviceIncome','securitiesTradingIncome','fxGoldIncome','otherIncome'])} for p in ps.index[-5:]]
result['profit9T']={k:{'2025':sum(ps.loc[[p for p in ps.index if str(p).startswith('2025') and not str(p).endswith('Q4')],k]),'2026':sum(ps.loc[[p for p in ps.index if str(p).startswith('2026')],k])} for k in ['netInterestIncome','serviceIncome','profitBeforeProvision','netProfitParent']}
result['annualLoanSector']=fy['loanStructureBySector'].tail(1).to_dict(orient='index')
result['annualLoanType']=fy['loanStructureByType'].tail(1).to_dict(orient='index')
result['recentPrices']=px.tail(25).reset_index().to_dict(orient='records')
result['extra'] = {'nii9Tyoy': -17.846821825835658, 'service9Tyoy': 253.69474051694039, 'q3ProvisionBridgeResidual': -15015.650000000001, 'q3NPLGrowth': 7.109313763616609, 'q3GrossLoansGrowth': 10.112372252267154, 'q3Group2Growth': 5.2523667742337965, 'q3TotalAssetGrowth': 18.53590438466821, 'q3DepositIncrease': 127482.33000000007, 'q3BondsIncrease': 46269.86000000001, 'q3InterbankAssetIncrease': 78329.49, 'q4InterbankAssetIncrease': 55355.07000000001, 'q4NetInterbankChange': 18208.24, 'atrK': 2.11608, 'valueBreakout': 255.99239999999998, 'bvpsK': 32.46167718665465}
result['extra']['q3ProvisionBridgeResidual']=q.iloc[-1]['loanLossProvision']-q.iloc[-2]['loanLossProvision']-cr.iloc[-1]['creditProvisionExpense']
import math
def sanitize(v):
    if isinstance(v,dict): return {str(k):sanitize(x) for k,x in v.items()}
    if isinstance(v,list): return [sanitize(x) for x in v]
    if isinstance(v,float) and not math.isfinite(v): return None
    return v
result=sanitize(result)
Path(sys.argv[1],'audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str))
print(json.dumps({k:v for k,v in result.items() if k!='recentPrices'},ensure_ascii=False,indent=2,default=str))
