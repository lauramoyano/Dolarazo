import discord
from discord.ext import commands
from scrapper import *
from utils import *

class commands_cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Comando para mostrar el precio del dólar de La Republica
    @commands.command(name="dollar", aliases=["dolar", "dólar", "dlr"], help="Muestra el precio del dólar")
    async def dollar(self, ctx):
        first_msg = await ctx.send("Un momento, voy a buscar el precio del dólar...")

        try:
            tomorrow_trm = False
            # Traer el precio del dolar
            driver = get_driver()
            prices = scrap_dollar(driver)
            if len(prices) > 9:
                tomorrow_trm = True

            # prices = [dolar, apertura, promedio, maximo, minimo, nro_operaciones, trm, trm_dia_sig, compra_casa_cambio, venta_casa_cambio]
            current_price = prices.pop(0)
            current_price_value = get_float_value_from_str(current_price)
            open_price_value = get_float_value_from_str(prices[0])
            prices = [f"> *{price}*" for price in prices]

            if len(prices) < 9:
                raise Exception("Page didn't load correctly.")
            driver.quit()
        
        except Exception as e:
            print(e)
            await ctx.send("Hubo un error al buscar el precio del dólar. Inténtalo de nuevo más tarde.")
            await first_msg.delete()
            driver.quit()

        # Mensaje a enviar
        embed = discord.Embed(
            #title="Precio del dólar",
            description=f"## Precio actual del dólar:\n> # {current_price}",
            color=get_embed_color(current_price_value, open_price_value)
        )
        embed.add_field(name="Promedio", value=prices[1], inline=False)
        embed.add_field(name="TRM", value=prices[5], inline=False)
        if tomorrow_trm: embed.add_field(name="TRM Mañana", value=prices[6], inline=False)
        embed.add_field(name="Apertura", value=prices[0], inline=False)
        embed.add_field(name="Precio máximo", value=prices[3], inline=False)
        embed.add_field(name="Precio mínimo", value=prices[4], inline=False)

        embed.set_footer(text="Fuente: La República 🗿")
        # embed.set_author(name="La República", url="https://www.larepublica.co/", icon_url="https://www.larepublica.co/favicon.ico")

        # msg = f"### El precio actual del dólar es: **{prices[0]}**\n"
        # msg += f"- Precio de apertura: {prices[1]}\n"
        # msg += f"- Precio promedio: {prices[2]}\n"
        # msg += f"- Precio más alto: {prices[3]}\n"
        # msg += f"- Precio más bajo: {prices[4]}\n"
        # msg += f"- TRM: {prices[6]}\n"
        await ctx.send("Este es el precio del dólar hoy", embed=embed)
        await first_msg.delete()



    # Comando para mostrar el historial de la TRM de Superfinanciera
    @commands.command(name="trm", aliases=["tasa"], help="Muestra el historial de la TRM")
    async def return_trm(self, ctx, days=5):
        first_msg = await ctx.send("Un momento, voy a buscar el historial de la TRM...")

        try:
            # Traer el historial de la TRM
            driver = get_driver()
            history = scrap_trm_prices(driver, days)
            driver.quit()
        except Exception as e:
            print(e)
            await ctx.send("Hubo un error al buscar el historial de la TRM. Inténtalo de nuevo más tarde.")
            await first_msg.delete()
            driver.quit()

        # history = [(price1, date1), (price2, date2), (price3, date3), (price4, date4), (price5, date5)]
        history = [f"> **{price}** - {date}" for price, date in history]

        # Mensaje a enviar
        embed = discord.Embed(
            title="Historial de la TRM",
            description="\n".join(history),
            color=discord.Color.yellow()
        )

        embed.set_footer(text="Fuente: Superfinanciera 🏦")
        # embed.set_author(name="Superfinanciera", url="https://www.superfinanciera.gov.co/")

        await ctx.send("Este es el historial de la TRM", embed=embed)
        await first_msg.delete()
        driver.quit()

    
    # Comando para ver el precio actual y dar predicción de TRM
    @commands.command(name="predict", aliases=["prediction", "prediccion", "predicion", "predic"], help="Muestra el precio actual y predicción de la TRM para mañana")
    async def trm_predict(self, ctx):
        first_msg = await ctx.send("Un momento, voy a buscar el precio del dólar...")

        try:
            tomorrow_trm = False
            # Traer el precio del dolar
            driver = get_driver()
            prices = scrap_dollar(driver)
            if len(prices) > 9:
                tomorrow_trm = True

            # prices = [dolar, apertura, promedio, maximo, minimo, nro_operaciones, trm, trm_dia_sig, compra_casa_cambio, venta_casa_cambio]
            current_price = prices.pop(0)
            average_price_value = get_float_value_from_str(prices[0])
            trm_price_value = get_float_value_from_str(prices[5])
            
            if len(prices) < 9:
                raise Exception("Page didn't load correctly.")
            
            driver.quit()
        
        except Exception as e:
            print(e)
            await ctx.send("Hubo un error al buscar el precio del dólar. Inténtalo de nuevo más tarde.")
            await first_msg.delete()
            driver.quit()



        # Mensaje a enviar
        msg = f"### El precio actual del dólar es: **{current_price}**\n"
        msg += f"- Precio de apertura: {prices[0]}\n"
        msg += f"- Precio promedio: {prices[1]}\n"
        # msg += f"- Precio más alto: {prices[3]}\n"
        # msg += f"- Precio más bajo: {prices[4]}\n"
        msg += f"- TRM: {prices[5]}\n"

        if tomorrow_trm:
            msg += f"- TRM Mañana: {prices[6]}\n"
            msg += "\n\nYa hay una TRM establecida para el día de mañana, vuelve mañana para intentar predecir el día siguiente\n"

        else:
            msg += "\n\n" + trm_prediction(average_price_value, trm_price_value)

        await ctx.send(msg)
        await first_msg.delete()
        driver.quit()


    # Comando para mostrar la ayuda
    @commands.command(name="help", aliases=["ayuda", "h"], help="Muestra la ayuda")
    async def help(self, ctx):
        msg = "Hola, esta es la lista de comandos disponibles:\n"
        
        embed = discord.Embed(
            title="Comandos disponibles",
            description="Listado de comandos del Dolarazo",
            color=discord.Color.blue()
        )

        for command in self.bot.commands:
            embed.add_field(name=command.name, value=command.help, inline=False)
        
        await ctx.send(msg, embed=embed)


# Setup del cog
async def setup(bot):
    await bot.add_cog(commands_cog(bot))