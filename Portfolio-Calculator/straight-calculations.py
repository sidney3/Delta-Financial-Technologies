def calc_sharpe_ratio(risk_free_rate, port_return, stan_dev):
    return (port_return - risk_free_rate) / stan_dev


def calc_capital_asset_pricing_model(risk_free_rate, beta, mrkt_return):
    return risk_free_rate + (beta * (mrkt_return - risk_free_rate))


def calc_fama_french_model(risk_free_rate, b1, mrkt_return, b2, smb, b3, hml):
    return calc_capital_asset_pricing_model(risk_free_rate, b1, mrkt_return) \
        + (b2 * smb) + (b3 * hml)


print("type ':quit' to end program")
prompts = ["Risk-Free Rate? ", "Portfolio Return? ",
           "Standard Deviation of portfolio's excess return? ",
           "Risk Ratio relative to the market? (where a ratio of 1 is matching the market) ",
           "Market Return? ",
           "SMB: Historic excess returns of small-cap companies over large-cap companies? ",
           "Beta coefficient for SMB? (previous entry) ",
           "HML: Historic excess returns of value stocks (high book-to-price ratio) over growth stocks (low book-to-price ratio)? ",
           "Beta coefficient for HML? (previous entry) "
           ]
responses = []

for prompt in prompts:
    user_input = input(prompt)
    if user_input == ":quit":  # break out of program when quit
        break
    else:
        responses.append(user_input)

print("Sharpe Ratio: " +
      str(calc_sharpe_ratio(responses[0], responses[1], responses[2])))
print("Capital Asset Pricing Model (CAPM): " +
      str(calc_capital_asset_pricing_model(responses[0], responses[3], responses[4])))
print("Fama French Model: " + str(calc_fama_french_model(
    responses[0], responses[3], responses[4], responses[6], responses[5], responses[8], responses[7])))
