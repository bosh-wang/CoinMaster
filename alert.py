import get_current_coin_price

def alert():
  COIN = ['BTCUSDT', 'ETHUSDT', 'DOGEUSDT', 'LUNAUSDT']
  
  pre_price = {}
  curr_price = {'BTCUSDT':0, 'ETHUSDT':0, 'DOGEUSDT':0, 'LUNAUSDT':0}
  
  for coin in COIN:
    pre_price[coin] = curr_price[coin]
    curr_price[coin] = get_current_coin_price(coin)
    price_change_ratio = (curr_price[coin] - pre_price[coin])/curr_price
    if price_change_ratio > 0.001 or price_change_ratio < 0.001:
      return True
    else :
      return False
    