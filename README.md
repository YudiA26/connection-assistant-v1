# OpenAI Connection Assistant v1

Este proyecto proporciona un conjunto de funciones para interactuar con el API de OpenAI y realizar varias tareas como diseño instruccional, lecciones teóricas, lecciones prácticas, creación de foros, quizzes, y validación de datos.

## Requisitos Previos

1. Python 3.6 o superior
2. Una cuenta en OpenAI con acceso a su API
3. Variables de entorno configuradas para la clave API y otros prompts

## Instalación

1. Clona este repositorio:
    ```bash
    git clone <URL-del-repositorio>
    cd <nombre-del-repositorio>
    ```

2. Instala las dependencias:
    ```bash
    pip install openai
    ```

## Configuración

Configura las siguientes variables de entorno en tu sistema:

- `API_GPT`: Tu clave API de OpenAI
- `themes_prompt`: Prompt para generar temas de curso
- `instructional_design_prompt`: Prompt para el diseño instruccional
- `teoric_prompt`: Prompt para lecciones teóricas
- `quiz_prompt`: Prompt para quizzes
- `practic_prompt`: Prompt para lecciones prácticas
- `forum_prompt`: Prompt para foros
- `validator_prompt`: Prompt para validación de datos
- `asistant_id`: ID del asistente
- `thread_id`: ID del hilo

Puedes configurarlas en tu archivo `.env` o directamente en tu entorno de desarrollo.

## Uso

### Inicialización

Asegúrate de que las variables de entorno estén configuradas correctamente antes de ejecutar el script. Puedes usar un archivo `.env` para configurarlas y cargarlas usando `python-dotenv`.

```python
from openai import OpenAI
import os
import logging
import time
import json

api_key = os.environ.get("API_GPT")
client = OpenAI(api_key=api_key, default_headers={"OpenAI-Beta": "assistants=v1"})
