import numpy as np

def read_params():
    principal = input('enter principal: ')
    rate = input('enter rate (as decimal): ')
    payment = input('enter payment: ')
    period = input('enter period (in months): ')
    print(principal, rate, payment, period)
    return principal, rate, payment, period

def calculate_period(principal, rate, payment):
    print('in method')
    period = np.math.log((payment/(payment-rate*principal)), 1+rate)
    print(period)
    return period

def calculate_payment(principal, rate, period):
    payment = principal*(rate*np.power((1+rate),period)/(np.power((1+rate),period)-1))
    print(payment)
    return payment

def graph_amort_table(principal, rate, payment, period):
    while period >= 0:
        print('table iteration goes here')
        period = period - 1

if __name__ == "__main__":
    principal, rate, payment, period = read_params()

    if period == '':
        print('calculating period...')
        period = calculate_period(float(principal), float(rate), float(payment))
    elif(payment == ''):
        print('calculating payment...')
        payment = calculate_payment(float(principal), float(rate), float(period))
    #TODO: calculate_principal, calculate_rate

#    graph_amort_table(float(principal), float(rate), float(payment),
#            float(period))
