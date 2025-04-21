# Proyecto Grupo A - Construcción de Software

## Estructura del Proyecto
- `src/`: Código fuente de la aplicación
  - `models/`: Modelos de datos con SQLAlchemy
  - `tests/`: Pruebas unitarias
  - `app.py`: Aplicación Flask principal
- `templates/`: Plantillas HTML
- `static/`: Archivos estáticos (CSS, JS, imágenes)

## Requisitos
- Python 3.9+
- Flask
- SQLAlchemy
- pytest

## Instalación
1. Clonar el repositorio
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno: `source venv/bin/activate` (Linux/Mac) o `venv\Scripts\activate` (Windows)
4. Instalar dependencias: `pip install -r requirements.txt`

## Ejecución
- Desarrollo: `flask run`
- Pruebas: `pytest src/tests -v`

## Metodologías Implementadas
1. **TDD (Test-Driven Development)**: Desarrollo guiado por pruebas
2. **Katas TDD**: Ejercicios prácticos de programación
3. **ORM (SQLAlchemy)**: Mapeo objeto-relacional
4. **Integración Continua**: GitHub Actions para pruebas automáticas

## API Endpoints
- `GET /api/members`: Lista de miembros del equipo
- `GET /api/technologies`: Lista de tecnologías utilizadas
