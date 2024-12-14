from fastapi import FastAPI, UploadFile, File, Form
import os #Para acceder a la ruta del home
import uuid #generar un nombre aleatorio, unico
# creación del servidor
app = FastAPI()
#Form(...) -> operador ellipsis
@app.post("/fotos")
async def guarda_foto(nombre:str=Form(None),direccion:str=Form(...),foto:UploadFile=File(...),vip:bool=Form(False)):# vip:bool=Form(False) , si el usuario no marca el checkbox de Usuario vip sera FALSE A, si lo marca TRUE
    print("Nombre: ", nombre) 
    print("Direccion: ", direccion)
    print("vip: ", vip)
    home_usuario = os.path.expanduser("~")#home del usuario
    nombre_archivo = uuid.uuid4()#nombre en formato hexadecimal
    extension_foto = os.path.splitext(foto.filename)[1]
    if vip:#si el usuario es vip guardamos la foto en fotos-usurios.vip
     ruta_imagen = f'{home_usuario}/fotos-usuarios-vip/{nombre_archivo}{extension_foto}'
    else:#si no es vip guardamos la foto en fotos.usuarios
     ruta_imagen = f'{home_usuario}/fotos-usuarios/{nombre_archivo}{extension_foto}'
     
    print("Guardando la foto en ", ruta_imagen) #imprimir la ruta en donde se guardara la imagen
    with open(ruta_imagen,"wb") as imagen:
        contenido = await foto.read()
        imagen.write(contenido)

    respuesta = {
        "Nombre" : nombre,
        "Direccion" : direccion,
        "Ruta": ruta_imagen,
        "Checkbox":vip
    }
    return respuesta

# decorator
@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "Ejercicio formularios!"
    }

    return respuesta