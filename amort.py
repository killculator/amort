import numpy

def read_params():
    principal = input('enter principal: ')
    rate = input('enter rate: ')
    payment = input('enter payment: ')
    period = input('enter period: ')
    print(principal, rate, payment, period)
    return principal, rate, payment, period

def calculate_period(principal, rate, payment):
    period = numpy.log1p(rate)*(payment/(payment-rate*principal))
    print(period)

def calculate_payment(principal, rate, period):
    payment = principal*(rate*numpy.power((1+rate),period)/(numpy.power((1+rate),period)-1))
    print(payment)



if __name__ == "__main__":
    principal, rate, payment, period = read_params()

    if period == '':
        print('calculating period...')
        calculate_period(float(principal), float(rate), float(payment))
    elif(payment == ''):
        print('calculating payment...')
        calculate_payment(float(principal), float(rate), float(period))
