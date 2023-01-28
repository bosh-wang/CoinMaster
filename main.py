import discord
import os
import emoji

import get_current_coin_price as get
# import get_history_coin_price_image as get_figure
from keep_alive import keep_alive

token = os.environ['TOKEN']

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    # start messages
    if msg.startswith("!hello"):
        await message.channel.send(
            "Hello this is Coin Master :heavy_dollar_sign::heavy_dollar_sign: \nType !command to see more commands :smile: "
        )

    if msg.startswith("!command"):
        await message.channel.send('''
                               :red_circle:  Type !priceCoinName to see current price of this coin(bitcoin, ethercoin, dogecoin, lunacoin)\nEg: !pricebitcoin\n:red_circle:  Type !figureCoinName to see history price figure of this coin(bitcoin, ethercoin, dogecoin, lunacoin)\nEg: !figurebitcoin\n:red_circle:  Type !twofigureCoin1NameCoin2Name to see history price two figure of this coin(bitcoin, ethercoin, dogecoin, lunacoin)\nEg: !twofigurebitcoinlunacoin\n:red_circle:  Type !newsCoinName to see latest news of this coin(bitcoin, ethercoin, dogecoin, lunacoin)\nEg: !newsbitcoin\n:red_circle:  Type !author to see the authors\nEg: !author'''
                                   )

# get the current price
    if msg.startswith("!price"):

        await message.channel.send("Loading data ...\nAlmost done ... ")

        coin_type = msg.split('!price', 1)[1]
        official_coin = ''

        if coin_type == 'bitcoin':
            official_coin = 'BTC_USDT'
        elif coin_type == 'ethercoin':
            official_coin = 'ETH_USDT'
        elif coin_type == 'dogecoin':
            official_coin = 'DOGE_USDT'
        elif coin_type == 'lunacoin':
            official_coin = 'LUNA_USDT'
        else:
            await message.channel.send(
                'Sorry :worried:, we currently do not support this type of coin : ( '
            )

        try:
            response = "The current price of " + coin_type + " is " + str(
                get.get_current_coin_price(
                    official_coin)) + " USDT :dollar: :dollar:"
            await message.channel.send(response)
        except:
            await message.channel.send(
                "Network error, please try again later...")

# about author
    if msg.startswith("!author"):
        await message.channel.send(
            ''':red_circle:  Type !shadowslayer to see the profile of shadowslayer\nEg: !shadowslayer\n:red_circle:  Type !bosh to see the profile of bosh\nEg: !bosh\n:red_circle:  Type !surprise to see the surprise\nEg: !surprise'''
        )

    if msg.startswith("!shadowslayer"):
        await message.channel.send(":u5272: 葉董好 :point_up::point_down:\n")

    if msg.startswith("!bosh"):
        await message.channel.send(
            "LIFELINE!!!!RES ME!!!!LIFELINE:face_with_symbols_over_mouth::face_with_symbols_over_mouth:\n"
        )

    if msg.startswith("!surprise"):
        await message.channel.send(
            '''小彩蛋:smirk:\nhttps://www.youtube.com/watch?v=UDWsT0Wh-IU''')

# get figure of history price
#     if msg.startswith("!figure"):

#         coin_type = msg.split('!figure', 1)[1]
#         official_coin = ''

#         if coin_type == 'bitcoin':
#             official_coin = 'BTCUSDT'
#         elif coin_type == 'ethercoin':
#             official_coin = 'ETHUSDT'
#         elif coin_type == 'dogecoin':
#             official_coin = 'DOGEUSDT'
#         elif coin_type == 'lunacoin':
#             official_coin = 'LUNAUSDT'
#         else:
#             await message.channel.send(
#                 'Sorry :worried:, we currently do not support this type of coin : ( '
#             )

#         file = get_figure.get_history_price_figure(official_coin, '1d')
#         await message.channel.send(
#             file=discord.File(f'./image/{file}_{official_coin}_test.jpg'))

# # get two figures of history price
#     if msg.startswith("!twofigure"):

#         combined_coin_type = msg.split('!twofigure', 1)[1]
#         coin_type1 = combined_coin_type.split('coin', 2)[0] + 'coin'
#         coin_type2 = combined_coin_type.split('coin', 2)[1] + 'coin'

#         if coin_type1 == 'bitcoin':
#             official_coin1 = 'BTCUSDT'
#         elif coin_type1 == 'ethercoin':
#             official_coin1 = 'ETHUSDT'
#         elif coin_type1 == 'dogecoin':
#             official_coin1 = 'DOGEUSDT'
#         elif coin_type1 == 'lunacoin':
#             official_coin1 = 'LUNAUSDT'
#         if coin_type2 == 'bitcoin':
#             official_coin2 = 'BTCUSDT'
#         elif coin_type2 == 'ethercoin':
#             official_coin2 = 'ETHUSDT'
#         elif coin_type2 == 'dogecoin':
#             official_coin2 = 'DOGEUSDT'
#         elif coin_type2 == 'lunacoin':
#             official_coin2 = 'LUNAUSDT'
#         else:
#             await message.channel.send(
#                 'Sorry :worried:, we currently do not support this type of coin : ( '
#             )

#         file = get_figure.get_two_history_price_figure(official_coin1,
#                                                        official_coin2, '1d')
#         await message.channel.send(file=discord.File(
#             f'./image/{file}_{official_coin1}_{official_coin2}_test.jpg'))


# get news of coin

    if msg.startswith("!news"):

        coin_type = msg.split('!news', 1)[1]
        official_coin = ''

        if coin_type == 'bitcoin':
            official_coin = 'bitcoin'
        elif coin_type == 'ethercoin':
            official_coin = 'ethereum'
        elif coin_type == 'dogecoin':
            official_coin = 'doge'
        elif coin_type == 'lunacoin':
            official_coin = 'luna'
        else:
            await message.channel.send(
                'Sorry :worried:, we currently do not support this type of coin : ( '
            )

        if official_coin == '':
            print('nothing')
        else:
            response = f'The latest news about bitcoin are :point_down:\n{get.get_coin_news_url(official_coin)}'
            await message.channel.send(response)

keep_alive()
client.run(token)
