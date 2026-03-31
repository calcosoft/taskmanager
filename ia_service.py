import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(description):
    if not os.getenv("OPENAI_API_KEY"):
        return ["Error: LA API KEY de OpenAI no está configurada. Por favor, configure la variable de entorno OPENAI_API_KEY."]
    try:
        prompt = f"""Dessglosa la siguiente tarea compleja en una lista de 3 a 5 subtareas simples y accionables.
    
    Tarea: {description}
    Formato de respuesta:
    - Subtarea 1
    - Subtarea 2
    - Subtarea 3
    - Subtarea 4 (opcional)
    - etc.

    Responde solo con la lista de subtareas, una por linea, empezando cada linea con un guion """
        
        params = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "system", "content": "Eres un asistente experto en gestión de tareas que ayuda "
            "a dividir tareas complejas en pasoso simples y accionables."}, {"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 300,
            "n": 1,
            "verbosity": "medium",
            "reasoning_effort": "minimal"
        }
        response = client.chat.completions.create(**params)
        content = response.choices[0].message.content.strip()
        subtasks = []
        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                print(f"Subtarea generada: {subtask}")
                if subtask:
                    subtasks.append(subtask)
        return subtasks if subtasks else ["Error: No se pudieron generar subtareas. Por favor, intenta con una descripción diferente o más detallada."]
   
    except Exception:
        print("Error: Ocurrió un error al generar las subtareas. Por favor, intenta nuevamente más tarde.")    
    


        
