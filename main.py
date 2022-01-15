import web #utiliza la libreria de web.py

web.config.debug = False # Desactiva el modo de depuraciondepuración 

urls = ( # urls que contendra nuestra pagina
    "/", "Index",
    "/count", "count",
    "/reset", "reset",
)

app = web.application(urls, locals()) # Direcciona las rutas