# Dolarazo

Dolarazo es una aplicación para Discord que utiliza técnicas de web scraping para recopilar datos en tiempo real sobre la tasa de cambio del dólar en diferentes mercados financieros. Esta herramienta proporciona a los usuarios colombianos información actualizada y confiable sobre la tendencia del dólar en comparación con su moneda local, lo que les permite tomar decisiones financieras más informadas.


## Uso del bot

### Servidor dedicado
Puedes probar el bot uniéndote a nuestro servidor de prueba dedidado, solo haz click en el siguiente enlace:
> https://discord.gg/4WJAqK2zMa

### Invita a Dolarazo a tu servidor
Si quieres tener a Dolarazo en tu propio servidor de discord, puedes invitarlo con el siguiente enlace:
> https://discord.com/oauth2/authorize?client_id=1234348933250154589&permissions=551903554624&scope=bot+applications.commands

### Hostea tu propia versión de Dolarazo

Si deseas hostear tu propio bot en discord, sigue los pasos a continuación:

- Crea tu propia aplicación de Discord en el siguiente enlace: https://discord.com/developers/applications
- Una vez creada la aplicación, otorga los permisos de escritura y lectura de chats y obten el TOKEN de autorización de Discord
- Una vez obtenido el TOKEN, debes invitar a tu bot a discord

Tras realizar estos pasos, debes configurar el bot:

- Clonar el repositorio de Git
```
git clone https://github.com/lauramoyano/Dolarazo.git
```
- Crea un ambiente virtual de Python (opcional)
**Windows**
```
python -m venv venv
./venv/Scripts/activate
```
**Linux o Mac**
```
python3 -m venv venv
source venv/bin/activate
```
- Instala los requerimientos
```
pip3 install -r requirements.txt
```
- Añade el TOKEN a tu ambiente virtual
**Windows**
```
$env:TOKEN='TU_TOKEN_DE_DISCORD'
```
**Linux o Mac**
```
export TOKEN='TU_TOKEN_DE_DISCORD'
```
- Activa el bot
**Windows**
```
python main.py
```
**Linux o Mac**
```
python3 main.py
```
