def capitalization_ratio(interest, periods):
    return (1 + interest) ** -periods


def french_amortization_fee(capital, interest, periods):
    """
       interest: should be provided in numeric
    """

    cap_rat = capitalization_ratio(interest, periods)
    return capital * interest / (1 - cap_rat)


capital = input("")
