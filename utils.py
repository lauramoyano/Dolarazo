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
    

def trm_prediction(average, trm):
    if abs(average - trm) < 5:
        return "El precio del dólar para mañana puede subir o bajar pero no será muy significativo"
    if average > trm:
        return "Según el comportamiento del dólar el día de hoy, es probable que el precio de la TRM de mañana sea más alto que el de hoy"
    elif average < trm:
        return "Teniendo en cuenta los movimientos del dólar hoy, es probable que el precio de la TRM de mañana baje con respecto al de hoy"
    else:
        return "Parece ser que el dólar se ha mantenido estable hoy, por lo que el precio de la TRM de mañana será muy similar al de hoy"
