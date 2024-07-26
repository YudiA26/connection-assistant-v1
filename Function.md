# Funciones Disponibles

Este proyecto incluye varias funciones para interactuar con el API de OpenAI. Antes de utilizar estas funciones, asegúrate de haber entrenado tu asistente con los formatos JSON requeridos y configurado las variables de entorno adecuadamente. A continuación, se presentan ejemplos de cómo utilizar cada función.

## Ejemplos de Uso

### 1. `instructional_design`

**Descripción**: Esta función genera un diseño instruccional para un curso. Utiliza información sobre el curso, temas, horas disponibles, lecciones y tipos de lecciones para crear un plan detallado.

**Uso**:

| Parámetro         | Tipo              | Descripción                                               |
|-------------------|-------------------|-----------------------------------------------------------|
| `client`          | `OpenAI Client`   | El cliente de OpenAI configurado.                         |
| `thread_id`       | `str`             | El ID del hilo de conversación en el que se ejecutará la solicitud. |
| `course`          | `str`             | El nombre del curso para el cual se está creando el diseño instruccional. |
| `themes`          | `str`             | Temas que se abordarán en el curso.                      |
| `hours`           | `int`             | Número de horas disponibles para el curso.               |
| `lessons`         | `int`             | Cantidad de lecciones en el curso.                       |
| `lessons_types`   | `str`             | Tipos de lecciones que se incluirán.                     |



## 2. Code usses: 

```python
content = instructional_design(client, thread_id, course, themes, hours, lessons, lessons_types)
print(content)

content = themes_course(client, thread_id, course, description, competences, public)
print(content) 

content = teoric_lesson(client, thread_id, lessonName, durationMinutes)
print(content)

content = practic_lesson(client, thread_id, lessonName)
print(content)

content = forum_lesson(client, thread_id, lessonName)
print(content)

content = quiz_lesson(client, thread_id, lessonName)
print(content)

content = validator_gpt(client, thread_id, error, result)
print(content)

