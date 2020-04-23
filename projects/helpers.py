def calc_rate(rates):
    rates_number = len(rates) or 1
    avg = 0
    for rate in rates:
        avg += rate.rate
    return avg/rates_number