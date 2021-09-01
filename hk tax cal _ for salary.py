UI = '''
1. tax calculator for salary tax
2. tax deduction items
3. total tax
'''

def tax_cal_sal():
    joint = input('joint-assessment or not? if so, press y; otherwise press n')
    if joint == y:
        tax_cal_sal_j()
    elif joint == n:
        tax_cal_sal_i()
    else:
        print('invaild input')

    