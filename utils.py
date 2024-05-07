import discord

def get_float_value_from_str(string_price):
    string_price = string_price.replace(".", "").replace(" ", "").replace("$", "").replace(",", ".")

    return float(string_price)

def get_embed_color(current, open):
    if current > open:
        return discord.Color.green()
    elif current < open:
        return discord.Color.red()
    else:
        return discord.Color.lighter_grey()
