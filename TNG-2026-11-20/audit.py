from pathlib import Path
import json

W = Path(__file__).resolve().parent

def raw(key):
    return json.loads((W / 'raw' / f'{key}.json').read_text())['data']

q = raw('fa_q')['charts']
y = raw('fa_y')['charts']
cf = q['cashFlow']
# Đọc bản PDF BCTC riêng của TNG, trang PDF 5 ở cả bốn báo cáo. Đơn vị tỷ đồng.
# Mã 20: LCTT hoạt động kinh doanh; mã 30: LCTT đầu tư; mã 21: chi mua/xây TSCĐ và TS dài hạn khác.
cf_official = {
    'FY25': {'cfo': -259.486278787, 'invest': -90.591275408, 'capex21': 79.565962252},
    '9M25': {'cfo': -344.256176692, 'invest': -88.837068581, 'capex21': 77.811755425},
    '6M25': {'cfo': -937.259654491, 'invest': -69.897874576, 'capex21': 58.872561420},
    '9M26': {'cfo': -695.529280522, 'invest': -204.332225400, 'capex21': 66.852225400},
    '6M26': {'cfo': -870.323271350, 'invest': -199.511148544, 'capex21': 62.031148544},
}
a,b,c,d,e = (cf_official[k] for k in ('FY25','9M25','6M25','9M26','6M26'))
bridge = lambda f,g,h=None: {key:f[key]-g[key]+(h[key] if h else 0) for key in f}
ttm = bridge(a,b,d)
lnst_ttm = 391.968936388 - 280.378820648 + 361.637277658
cap = 128731266 * 16.8 / 1e6
p = {r['date']:r for r in raw('price')['rows']}
v = raw('valuation_1d')['charts']
bv_i = v['pb']['dates'].index('2026-11-19') if 'dates' in v['pb'] else raw('valuation_1d')['dates'].index('2026-11-19')
out = {
    'sstock': {'CFO_FY25_annual':y['cashFlow']['operating'][-1], 'CFO_FY25_sum_Q':sum(cf['operating'][-7:-3]), 'CFO_9M26_sum_Q':sum(cf['operating'][-3:]),'CFO_TTM':sum(cf['operating'][-4:]), 'CFO_TTM_prior':sum(cf['operating'][-8:-4]),'CFO_Q3_26':cf['operating'][-1], 'BVPS_at_close_dong':v['pb']['bvps'][bv_i], 'adjusted_ret_1Y_pct': (p['2026-11-19']['adjClose']/p['2025-11-13']['adjClose']-1)*100},
    'BCTC_riêng_TNG': cf_official,
    'Q3_25': bridge(b,c), 'Q4_25': bridge(a,b), 'Q3_26':bridge(d,e), '2026Q3_TTM':ttm,
    'LNST_TTM_bctc':lnst_ttm,'CFO_LNST_TTM':ttm['cfo']/lnst_ttm,'CFO_plus_CFI_TTM':ttm['cfo']+ttm['invest'], 'CFO_less_capex21_TTM':ttm['cfo']-ttm['capex21'],
    'BVPS_bctc_2026Q3_dong':2035.275102163e9/128731266,'PB_priceOverQ3book':cap/2035.275102163,
    'cashAndDeposits_bctc':158.162847681+492.766260829,'interestBorrowingPctYoY_Q3':(87.384844339/71.293006201-1)*100,
    'ESOP_2025':{'new_shares':6130060,'issue_price_thousand':10.0,'proceeds_bil':61.3006,'end_date':'2025-10-15'},
}
(W/'audit.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(out, ensure_ascii=False, indent=2))
