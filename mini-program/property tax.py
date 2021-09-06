import datetime

def definition():
    x = str(input('If it a Land/Bldg/pier/whave? if yes, reply y, otherwise reply n'))
    if x == 'y' :
       print('Do the calculation')
       start()
    if x == 'n' :
        print('That isnt peoperty tax.')
        start()
    else:
        print('incorrect command')
        start()

def database(rent = 0, pfr = 0, mgt_fee = 0, owner_exp = 0):
    rent = input('total rental income')
    pfr = input('any payments for the right of use of premises under licence')
    mgt_fee = input('service charge or management fee paid to owner')
    owner_exp = input('owner expenditure borne by the tenant ')
    database_result = rent + pfr + mgt_fee + owner_exp
    return database_result

def database_special():
    global premium_month
    premium_month = int(input('lease period in month'))
    if premium_month < 36:
        print('use month as the lump-sum fee calculation base')
        lumpsum_month()
    elif premium_month >= 36:
        print('use 3 years, i.e. 36 months as the lump-sum fee base')
        lumpsum_36()
    else:
        print('invaild input')
        start()

def lumpsum_month():
    global taxable_premium
    total_premium = int(input('Total premium value is:'))
    x = round(total_premium // premium_month)
    print('monthly premium is ', x, ' .')
    y = int(input('leasing period from the str of the f.y. till yr end'))
    taxable_premium = x*y
    print('taxable premium is ',taxable_premium, ' .')
    start()
    return taxable_premium


def lumpsum_36():
    global taxable_premium_36
    total_premium = int(input('Total premium value is:'))
    x = round(total_premium // 36)
    print('monthly premium is ', x, ' .')
    y = int(input('leasing period from the str of the f.y. till yr end'))
    taxable_premium_36 = x*y
    print('taxable premium is ',taxable_premium_36, ' .')
    start()
    return taxable_premium_36

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
    start()

def consideration_payable():
    global recovered_bad_debt,irrecoverable_rent,rates,consider_payable
    recovered_bad_debt = int(input('recovered_bad_debt'))
    irrecoverable_rent = int(input('irrecoverable_rent'))
    rates = int(input('rates paid by owner'))
    consider_payable = recovered_bad_debt + irrecoverable_rent + rates
    start()

def calculator():
    database_result = database()
    print('total normal income' + database_result)
    print('Taxable premium in lease period base: ' + taxable_premium)
    print('Taxable_premium in 36 months base: ' + taxable_premium_36)
    print('total considered payable is' + consider_payable)
    accessable_income = database_result + taxable_premium + taxable_premium_36 + consider_payable
    print('accessable income before rate is' + accessable_income)
    print('rates paid by owner: ' + rates)
    print('accessable income after rate is ', accessable_income)
    statutory_deduction = round(accessable_income * 0.2)
    print('0.2 stationary deduction value:', statutory_deduction)
    net_accessable_value = accessable_income - statutory_deduction
    print('net accessable value is: ', net_accessable_value )
    start()

def start():
    UI = '''
        1. Whether your item is property tax
        2. input rental income, payment for the right-of-use, mgt fee and owner expense
        3. calculate property premium
        4. calculate your lease period for reference
        5. input recovered bad debt, irrecoverable rent and rates paid by owner
        6. do the calculation
    '''
    print(UI)
    x = int(input('run which program? input a number.'))
    if x == 1:
        definition()
    elif x == 2:
        database()
    elif x == 3:
        database_special()
    elif x == 4:
        lease_period()
    elif x == 5:
        consideration_payable()
    elif x == 6:
        calculator()
    else:
        print('Wrong command')
        start()


start()
