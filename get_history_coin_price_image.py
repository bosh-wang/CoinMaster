from finlab import crypto
import matplotlib.pyplot as plt
import datetime


def get_history_price_figure(coin, period):

    df = crypto.get_all_binance(coin, period)

    plt.plot(df.index, df['Open'])

    plt.annotate('max price: {p}'.format(p=max(df['Open'])),
                 xy=(df.index[df['Open'] == max(df['Open'])], max(df['Open'])),
                 xytext=(df.index[df['Open'] == max(df['Open'])],
                         0.7 * max(df['Open'])),
                 arrowprops=dict(facecolor='green'))
    plt.annotate('min price: {p}'.format(p=min(df['Open'])),
                 xy=(df.index[df['Open'] == min(df['Open'])], min(df['Open'])),
                 xytext=(df.index[df['Open'] == min(df['Open'])],
                         0.3 * max(df['Open'])),
                 arrowprops=dict(facecolor='red'))

    plt.title(f"Price of {coin}")
    plt.xlabel("Year")
    plt.ylabel("Price(USDT)")

    #     plt.show()
    currentTime = datetime.datetime.now()

    plt.savefig(f"./image/{currentTime}_{coin}_test.jpg")

    plt.clf()

    return str(currentTime)

# default period '1d'
def get_two_history_price_figure(coin1, coin2, period):
    df1 = crypto.get_all_binance(coin1, period)
    df2 = crypto.get_all_binance(coin2, period)
    
    plt.rcParams['font.family'] = 'Consolas'
    
    plt.plot(df1['Open'], label = coin1)
    
    plt.plot(df2['Open'], label = coin2)

    greater = max(max(df1['Open']), max(df2['Open']))
    
    plt.annotate('max price: {p}'.format(p=max(df1['Open'])), 
                 xy = (df1.index[df1['Open'] == max(df1['Open'])], max(df1['Open'])), 
                 xytext = (df1.index[df1['Open'] == max(df1['Open'])], 0.9*greater), 
                 arrowprops=dict(facecolor='green'))
    plt.annotate('min price: {p}'.format(p=min(df1['Open'])), 
                 xy = (df1.index[df1['Open'] == min(df1['Open'])], min(df1['Open'])), 
                 xytext = (df1.index[df1['Open'] == min(df1['Open'])], 0.2*greater), 
                 arrowprops=dict(facecolor='red'))
    
    plt.annotate('max price: {p}'.format(p=max(df2['Open'])), 
                 xy = (df2.index[df2['Open'] == max(df2['Open'])], max(df2['Open'])), 
                 xytext = (df2.index[df2['Open'] == max(df2['Open'])], 0.5*greater),
                 arrowprops=dict(facecolor='green'))
    plt.annotate('min price: {p}'.format(p=min(df2['Open'])), 
                 xy = (df2.index[df2['Open'] == min(df2['Open'])], min(df2['Open'])), 
                 xytext = (df2.index[df2['Open'] == min(df2['Open'])], 0.4*greater), 
                 arrowprops=dict(facecolor='red'))
    
    plt.xlabel("Year")
    plt.ylabel("Price(USD)")
    plt.legend()

    currentTime = datetime.datetime.now()
    
    plt.savefig(f"./image/{currentTime}_{coin1}_{coin2}_test.jpg")

    plt.clf()
    
    # plt.show()
    return currentTime
