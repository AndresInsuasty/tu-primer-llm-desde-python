"""Paso 3 (la demo del video): la misma pregunta a los dos proveedores.

Compara respuesta, tiempo y tokens. Si un proveedor falla, lo reporta y sigue.
"""
import time

from openai import APIConnectionError, AuthenticationError, NotFoundError

from llm import crear_cliente

PREGUNTA = "Dame 3 ideas de proyectos con IA para un analista de datos. Una línea cada una."

for proveedor in ["ollama", "openai"]:
    print(f"\n=== {proveedor.upper()} ===")
    try:
        cliente, modelo = crear_cliente(proveedor)
        inicio = time.perf_counter()
        respuesta = cliente.chat.completions.create(
            model=modelo,
            messages=[{"role": "user", "content": PREGUNTA}],
        )
        segundos = time.perf_counter() - inicio
    except APIConnectionError:
        if proveedor == "ollama":
            print("No hay conexión. ¿Está corriendo Ollama? Ejecuta: ollama serve")
        else:
            print("No hay conexión con OpenAI. Revisa tu internet.")
        continue
    except NotFoundError:
        print("Modelo no encontrado. Descárgalo con: ollama pull llama3.2:3b")
        continue
    except AuthenticationError:
        print("Falta o es inválida OPENAI_API_KEY en tu archivo .env")
        continue
    except ValueError as error:
        print(error)
        continue

    print(respuesta.choices[0].message.content)
    print(f"\n{modelo} · {segundos:.1f} s · {respuesta.usage.total_tokens} tokens")
