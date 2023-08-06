def capitalization_ratio(interest, periods):
    return (1 + interest) ** -periods


def amortization_fee(capital, interest, periods):
    """
       interest: should be provided in numeric
    """

    cap_rat = capitalization_ratio(interest, periods)
    return capital * interest / (1 - cap_rat)


def calculate_period_summary(capital, interest, fee):
    interest_fee = capital * interest
    amortization = fee - interest_fee
    live_capital = capital - amortization

    dictio = {
        'capital': capital,
        'interest_fee': interest_fee,
        'amortization': amortization,
        'fee': fee,
        'live_capital': live_capital
    }
    return dictio


def amortization_table(capital, interest, periods):
    initial_capital = capital
    fee = amortization_fee(capital, interest, periods)

    amortization_list = []

    for period in range(periods):
        summary = calculate_period_summary(initial_capital, interest, fee)
        initial_capital = summary['live_capital']
        amortization_list.append(summary)

    return amortization_list


if __main__ == '__name__':
    print(amortization_table(1000, 0.01, 10))
