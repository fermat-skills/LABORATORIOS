# Instrucciones para ejecutar `main.py` en LABORATORIOS

Este README describe los pasos para ejecutar el archivo `main.py` del proyecto, desde la activación del entorno con Poetry hasta la ejecución del servicio.

## 1. Clonar el repositorio (si aplica)

```
git clone https://github.com/fermat-skills/LABORATORIOS
cd LABORATORIOS
```

## 2. Instalar Poetry (si no lo tienes)

Sigue la [documentación oficial de Poetry](https://python-poetry.org/docs/#installation) para instalarlo en tu sistema.

## 3. Instalar dependencias

Desde la raíz del proyecto (donde está el archivo `pyproject.toml`):

```
poetry install
```

## 4. Activar el entorno virtual de Poetry

```
cd .\laboratorios_env\
poetry shell
```

## 5. Ejecutar el archivo `main.py`

Ubícate en la carpeta donde está el archivo `main.py`:

```
cd ..
cd .\LABORATORIOS\LEVEL\
```

Ejecuta el script:

```
uvicorn main:app --reload  
```

---

**Notas:**
- Si el script requiere variables de entorno o archivos de configuración, asegúrate de tenerlos preparados antes de ejecutar.
- Si tienes problemas con dependencias, revisa que estés usando el entorno de Poetry correctamente.
