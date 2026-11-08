
# Taller de Pruebas Automatizadas

## Sistema de gestión de usuarios

Proyecto académico desarrollado para aplicar técnicas de automatización de pruebas funcionales sobre una aplicación web y una API REST.

## Tecnologías utilizadas

- Python
- FastAPI
- Pydantic
- Jinja2
- Selenium
- Postman
- HTML
- JavaScript
- Unittest

## Arquitectura del proyecto

La aplicación utiliza una arquitectura modular que separa las responsabilidades:

- **API:** definición de rutas y endpoints.
- **Schemas:** validación y estructura de los datos.
- **Services:** lógica de negocio.
- **Repositories:** almacenamiento y consulta de usuarios.
- **Templates:** interfaz web de inicio de sesión.
- **Tests:** pruebas automatizadas con Selenium.
- **Evidencias:** capturas de los resultados obtenidos.

## Funcionalidades

- Consultar usuarios registrados.
- Registrar nuevos usuarios.
- Rechazar registros con correos duplicados.
- Iniciar sesión con credenciales válidas.
- Rechazar credenciales incorrectas.

## Pruebas automatizadas

### Selenium

Se implementaron pruebas para verificar:

- Inicio de sesión exitoso.
- Inicio de sesión incorrecto.

Ejecución:

```bash
python -m unittest tests.test_login -v
```

### Postman

Se implementaron solicitudes y pruebas automatizadas para:

1. Consultar usuarios.
2. Registrar usuarios.
3. Rechazar usuarios duplicados.
4. Validar inicio de sesión exitoso.
5. Validar inicio de sesión incorrecto.

La colección de Postman se encuentra en:

`Pruebas_Automatizadas_Sistema_Usuarios.json`

## Ejecución del proyecto

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Iniciar el servidor:

```bash
uvicorn app.main:app --reload
```

Aplicación web:

`http://127.0.0.1:8000/`

Documentación de la API:

`http://127.0.0.1:8000/docs`

## Evidencias

Las capturas de las pruebas realizadas se encuentran en la carpeta `evidencias/`.

## Consideraciones

Este proyecto tiene fines académicos y demostrativos. El almacenamiento de usuarios es temporal y las contraseñas no están protegidas mediante hash, por lo que no debe utilizarse como sistema de producción.

## Autor

Boris Castro

## Propósito académico

Aplicar conocimientos de automatización de pruebas funcionales, validación de API REST y pruebas de interfaces web.
