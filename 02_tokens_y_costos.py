import sys

from llm import crear_cliente

PRECIOS_POR_MILLON = {
    "llama3.2:3b":{"entrada":0, "salida":0},
    "gpt-6-luna":{"entrada":0.1, "salida":0.5},
    }


proveedor = sys.argv[1] if len(sys.argv) > 1 else None
cliente, modelo = crear_cliente(proveedor)
print(f"Usando el Modelo: {modelo}")

respuesta = cliente.chat.completions.create(
    model=modelo,
    messages=[
        {"role": "system", "content": "Eres un profesor de python. Responde en Español en maximo 3 frases"},
        {"role": "user", "content": "Explica que es un token en una frase"},
    ]
)

uso = respuesta.usage
print(f"Uso de tokens: {uso}")

costo = ((uso.prompt_tokens*PRECIOS_POR_MILLON[modelo]["entrada"]) + (uso.completion_tokens*PRECIOS_POR_MILLON[modelo]["salida"]))/1_000_000
print(f"Costo estimado: ${costo:.6f}")
print(f"Respuesta: {respuesta.choices[0].message.content}")
