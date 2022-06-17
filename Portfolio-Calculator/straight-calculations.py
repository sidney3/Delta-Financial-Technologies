def calc_sharpe_ratio(risk_free_rate, port_return, stan_dev):
    return (port_return - risk_free_rate) / stan_dev


def calc_capital_asset_pricing_model(risk_free_rate, beta, mrkt_return):
    return risk_free_rate + (beta * (mrkt_return - risk_free_rate))


def calc_fama_french_models(risk_free_rate, b1, mrkt_return, b2, smb, b3, hml):
    return calc_capital_asset_pricing_model(risk_free_rate, b1, mrkt_return) \
        + (b2 * smb) + (b3 * hml)
