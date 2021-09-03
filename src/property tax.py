import datetime

def lease_period():
    d1_str = input('lease starting date in yr,mm,dd')
    yr_d1,mm_d1,dd_d1 = map(int, d1_str.split(','))
    d1 = datetime.date(yr_d1,mm_d1,dd_d1)
    d2_str = input('lease ending date in yr,mm,dd')
    yr_d2,mm_d2,dd_d2 = map(int, d2_str.split(','))
    d2 = datetime.date(yr_d2,mm_d2,dd_d2)
    lease_period = d2.month - d1.month + 12*(d2.year - d1.year)
    print('the lease period is ' ,int(lease_period), ' months.')
    #因為lease_period 係int, 必須要用逗號來連結 str and int in print()


def definition():
    x = str(input('If it a Land/Bldg/pier/whave? if yes, reply y, otherwise reply n'))
    if x == 'y' :
       print('Do the calculation')
       calculator()
    if x == 'n' :
        print('Use another application')
    else:
        print('incorrect command')
        start()

def database():
    rent = input('total rental income')
    pfr = input('any payments for the right of use of premises under licence')
    mgt_fee = input('service charge or management fee paid to owner')
    owner_exp = input('owner expenditure borne by the tenant ')
    return rent,pfr,mgt_fee,owner_exp

def database_special():
    month = int(input('lease period in month'))
    if month < 36:
        print('use month as the lump-sum fee calculation base')
        lumpsum_month()
    elif month > 36:
        print('use 3 years, i.e. 36 months as the lump-sum fee base')
        lumpsum_36()
    else:
        print('invaild input')
        start()
    return month

lease_period()

