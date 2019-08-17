import numpy as np


def read_params():
    principal = convert_param_to_float(input('enter principal: '))
    rate = convert_param_to_float(input('enter annual rate: '))
    payment = convert_param_to_float(input('enter payment: '))
    period = convert_param_to_float(input('enter period (in months): '))
    print('[', principal, rate, payment, period, ']')
    rate = format_rate(rate)
    return principal, rate, payment, period


def convert_param_to_float(param):
    if isinstance(param, float):
        return param
    elif param != '':
        return float(param)
    else:
        return param


def format_rate(rate):
    if rate > 1.0:
        rate = rate/100
    return rate/12


def calculate_period(principal, rate, payment):
    period = np.math.log((payment/(payment-rate*principal)), 1+rate)
    print('[', '%.2f' % period, ']')
    return period


def calculate_payment(principal, rate, period):
    payment = principal*(rate*np.power((1+rate), period)/(np.power((1+rate),
                                                          period)-1))
    print('[', '%.2f' % payment, ']')
    return payment


def calculate_principal(rate, payment, period):
    principal = (payment/rate)*(1-np.power(1+rate, -1*period))
    print('[', '%.2f' % principal, ']')
    return principal


def graph_amort_table(principal, rate, payment, period):
    total_interest = 0
    print('--period--+principal-+-interest-+-tot-int--')
    print('----------+----------+----------+----------')
    while (period >= 0) and (principal - payment > 0):
        principal, interest = calc_graph_iteration(principal, rate, payment)
        total_interest = total_interest + interest
        print(int(period), '      | ', '%.2f' % principal, ' | ', '%.2f' %
              interest, ' | ', '%.2f' % total_interest)
        print('----------+----------+----------+----------')
        period = period - 1


def calc_graph_iteration(principal, rate, payment):
    interest = principal * rate
    principal = principal - payment
    principal = principal + interest
    return principal, interest

if __name__ == "__main__":
    principal, rate, payment, period = read_params()

    if period == '':
        print('calculating period...')
        period = calculate_period(float(principal), float(rate),
                                  float(payment))
    elif(payment == ''):
        print('calculating payment...')
        payment = calculate_payment(float(principal), float(rate),
                                    float(period))
    elif(principal == ''):
        print('calculating principal...')
        # fix this
        principal = calculate_principal(float(rate), float(period),
                                        float(period))
    elif(rate == ''):
        while rate == '':
            print('rates are arbitrarily set by the fed, so i can\'t " \
                    "determine these, please enter in your own')
            rate = input('enter rate (as decimal): ')

    graph_amort_table(principal, rate, payment, period)
