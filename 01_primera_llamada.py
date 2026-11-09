import sys

from llm import crear_cliente

proveedor = sys.argv[1] if len(sys.argv) > 1 else None
cliente, modelo = crear_cliente(proveedor)
print(f"Usando el Modelo: {modelo}")

respuesta = cliente.chat.completions.create(
    model=modelo,
    messages=[
        {"role": "system", "content": "Eres un profesor de python. Responde en Español en maximo 3 frases"},
        {"role": "user", "content": "Que es un agente de IA?"},
    ]
)

print(respuesta.choices[0].message.content)
