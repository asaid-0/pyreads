from math import floor

def calc_rate(rates):
    rates_number = len(rates) or 1
    avg = 0
    for rate in rates:
        avg += rate.rate
    rate = {}
    rate['actual'] = avg/rates_number
    rate['base'] = floor(rate['actual'])
    return rate


def calc_donations(donations):
    amount_of_donations = 0
    for donation in donations:
        amount_of_donations += donation.amount
    return amount_of_donations