from openai import OpenAI
import os 
import logging
import time

api_key = os.environ.get("API_GPT")
client = OpenAI(api_key=api_key, default_headers={"OpenAI-Beta": "assistants=v1"})
themes_prompt = os.environ.get("themes_prompt")
instructional_design_prompt = os.environ.get("instructional_design_prompt")
teoric_prompt = os.environ.get("teoric_prompt")
quiz_prompt = os.environ.get("quiz_prompt")
practic_prompt = os.environ.get("practic_prompt")
forum_prompt = os.environ.get("forum_prompt")
validator_prompt = os.environ.get("validator_prompt")

##Assistant id del hilo y del asistente 
asistant_id = os.environ.get("asistant_id")
thread_id = os.environ.get("thread_id")

def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            if run.completed_at:
                elapsed_time = run.completed_at - run.created_at
                formatted_elapsed_time = time.strftime(
                    "%H:%M:%S", time.gmtime(elapsed_time)
                )
                print(f"Run completed in {formatted_elapsed_time}")
                logging.info(f"Run completed in {formatted_elapsed_time}")
                # Get messages here once Run is completed!
                messages = client.beta.threads.messages.list(thread_id=thread_id)
                last_message = messages.data[0]
                response = last_message.content[0].text.value
                print(f"Assistant Response: {response}")
                break
        except Exception as e:
            logging.error(f"An error occurred while retrieving the run: {e}")
            break
        logging.info("Waiting for run to complete...")
        time.sleep(sleep_interval)

    return response

def themes_course(client, thread_id, course, description, competences, public):
    # Formateando el themes_prompt con las variables proporcionadas
    initial_message = themes_prompt.format(course=course, description=description, competences=competences, public=public)

    ##INICIAR CONVERSACIÓN CON EL ASISTENTE 
    message = client.beta.threads.messages.create(
        thread_id = thread_id, 
        role = "user", 
        content = initial_message
    )

    # Ejecutar el asistente para obtener una respuesta
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=asistant_id
    )

    content = wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)

    print ("respuesta asistente cursos: ", content)
    
    return content

def instructional_design(client, thread_id, course, themes, hours, lessons, lessons_types):
   initial_message = instructional_design_prompt.format(course=course, themes=themes, hours=hours, lessons=lessons, lessons_types=lessons_types )
   
   message = client.beta.threads.messages.create(
        thread_id = thread_id, 
        role = "user", 
        content = initial_message
    )
   run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=asistant_id
    )
   content = wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)
   print ("respuesta asistente diseño instruccional: ", content)
   return content

def teoric_lesson(client, thread_id, lessoName, durationMinutes):
    initial_message = teoric_prompt.format(lessoName=lessoName, durationMinutes=durationMinutes)
    ##INICIAR CONVERSACIÓN CON EL ASISTENTE 
    message = client.beta.threads.messages.create(
        thread_id = thread_id, 
        role = "user", 
        content = initial_message
    )

    # Ejecutar el asistente para obtener una respuesta
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=asistant_id
    )

    content = wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)

    print ("respuesta asistente curso teorico: ", content)
    
    return content

def practic_lesson(client, thread_id, lessoName):
    initial_message = practic_prompt.format(lessoName=lessoName)
    ##INICIAR CONVERSACIÓN CON EL ASISTENTE 
    message = client.beta.threads.messages.create(
        thread_id = thread_id, 
        role = "user", 
        content = initial_message
    )

    # Ejecutar el asistente para obtener una respuesta
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=asistant_id
    )

    content = wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)

    print ("respuesta asistente curso practico: ", content)
    
    return content

def forum_lesson(client, thread_id, lessoName):
    initial_message = forum_prompt.format(lessoName=lessoName)
    ##INICIAR CONVERSACIÓN CON EL ASISTENTE 
    message = client.beta.threads.messages.create(
        thread_id = thread_id, 
        role = "user", 
        content = initial_message
    )

    # Ejecutar el asistente para obtener una respuesta
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=asistant_id
    )

    content = wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)

    print ("respuesta asistente curso practico: ", content)
    
    return content

def quiz_lesson(client, thread_id, lessoName):
    initial_message = quiz_prompt.format(lessoName=lessoName)
    ##INICIAR CONVERSACIÓN CON EL ASISTENTE 
    message = client.beta.threads.messages.create(
        thread_id = thread_id, 
        role = "user", 
        content = initial_message
    )

    # Ejecutar el asistente para obtener una respuesta
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=asistant_id
    )

    content = wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)

    print ("respuesta asistente curso practico: ", content)
    
    return content
    
def validator_gpt(client, thread_id, error, result):
    initial_message = quiz_prompt.format(error=error, result=result)
    ##INICIAR CONVERSACIÓN CON EL ASISTENTE 
    message = client.beta.threads.messages.create(
        thread_id = thread_id, 
        role = "user", 
        content = initial_message
    )

    # Ejecutar el asistente para obtener una respuesta
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=asistant_id
    )

    content = wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)

    print ("Json: ", content)
    
    return content

