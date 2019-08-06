import numpy as np

def read_params():
    principal = input('enter principal: ')
    rate = input('enter annual rate (as decimal): ')
    payment = input('enter payment: ')
    period = input('enter period (in months): ')
    print('[', principal, rate, payment, period, ']')
    return principal, rate, payment, period

def calculate_period(principal, rate, payment):
    period = np.math.log((payment/(payment-rate*principal)), 1+rate)
    print('[', '%.2f' % period, ']')
    return period

def calculate_payment(principal, rate, period):
    payment = principal*(rate*np.power((1+rate),period)/(np.power((1+rate),period)-1))
    print('[', '%.2f' % payment, ']')
    return payment

def calculate_principal(rate, payment, period):
    principal = (payment/rate)*(1-np.power(1+rate, -1*period))
    print('[', '%.2f' % principal, ']')
    return principal

def graph_amort_table(principal, rate, payment, period):
    total_interest = 0
    rate = rate/12
    print('--period--+principal-+-interest-+-tot-int--')
    print('----------+----------+----------+----------')
    while (period >= 0) and (principal > 0):
        principal, interest = calc_graph_iteration(principal, rate, payment)
        total_interest = total_interest + interest
        print(int(period), ' | ', '%.2f' % principal, ' | ', '%.2f' %
                interest,' | ', '%.2f' % total_interest)
        print('----------+----------+----------+----------')
        period = period - 1

def calc_graph_iteration(principal, rate, payment):
   principal = principal - payment
   interest = principal * rate
   principal = principal + interest
   return principal, interest

if __name__ == "__main__":
    principal, rate, payment, period = read_params()

    if period == '':
        print('calculating period...')
        period = calculate_period(float(principal), float(rate), float(payment))
    elif(payment == ''):
        print('calculating payment...')
        payment = calculate_payment(float(principal), float(rate), float(period))
    elif(principal == ''):
        print('calculating principal...')
        #fix this
        principal = calculate_principal(float(rate), float(period),
                float(period))
    elif(rate == ''):
        while rate == '':
            print('rates are arbitrarily set by the fed, so i can\'t " \
                    "determine these, please enter in your own')
            rate = input('enter rate (as decimal): ')

    graph_amort_table(float(principal), float(rate), float(payment),
            float(period))
