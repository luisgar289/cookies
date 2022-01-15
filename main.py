import web #utiliza la libreria de web.py

urls = ( # urls que contendra nuestra pagina
    "/set", "CookieSet",
    "/get", "CookieGet",
)

app = web.application(urls, locals()) # Direcciona las rutas

class CookieSet: #guarda una cookie
    def GET(self):
        i = web.input(age='19') #valor de la cookie
        web.setcookie('edad', i.age, 3600) #nombre de la cookie, valor y duracion
        return "Edad guardada en tus cookies" #Muestra un mensaje

class CookieGet: #Obtiene una cookie
    def GET(self):
        try:
             #return "Tu edad es: " + web.cookies().age + ". Usando el valor de la cookie." #Trae la cookie usando el valor.
             return "Tu edad es: " + web.cookies().get('edad') + ". Usando el nombre de la cookie." #Trae la cookie usando el nombre.
        except:
             # Si aun no se guarda la cookie
             return "Cookie no encontrada"

if __name__ == "__main__": #Inicia la pagina
    app.run()