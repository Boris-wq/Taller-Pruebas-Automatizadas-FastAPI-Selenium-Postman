
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from app.api.routes import auth, users


app = FastAPI(
    title="Sistema de Pruebas Automatizadas",
    description="Aplicación para probar formularios web y API REST",
    version="1.0.0"
)

templates = Jinja2Templates(directory="app/templates")


# Registrar las rutas de autenticación y usuarios
app.include_router(auth.router)
app.include_router(users.router)


# Página principal
@app.get("/", tags=["Web"])
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={}
    )
