"""Bonus: streaming, para ver la respuesta mientras se genera."""
import sys

from llm import crear_cliente

proveedor = sys.argv[1] if len(sys.argv) > 1 else None
cliente, modelo = crear_cliente(proveedor)

stream = cliente.chat.completions.create(
    model=modelo,
    messages=[{"role": "user", "content": "Escribe un haiku original sobre Python."}],
    stream=True,
)

for fragmento in stream:
    if fragmento.choices and fragmento.choices[0].delta.content:
        print(fragmento.choices[0].delta.content, end="", flush=True)
print()
