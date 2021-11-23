import win32com.client as win32

def enviarMail (destinatario, assunto, corpo):
    #Integração com outlook
    outlook = win32.Dispatch('outlook.application')

    #Para criar o email
    email = outlook.CreateItem(0)

    # Configurações do email
    email.To = destinatario
    email.Subject = assunto
    email.Body = corpo
    email.Send()

    return True
