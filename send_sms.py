from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "Sacar el codigo de la API de Twilio"
auth_token  = "Token de autentificacion de API en Twilio"

client = Client(account_sid, auth_token)


def crear_mensaje(link):
    message = client.messages.create(
    to="+595981415894",
    from_="+12672744332",
    body=f"BUENAS ESTOY EN PELIGRO Y NECESITO AYUDA! Mi ubicacion es: {link} ")

    return message
    
    
