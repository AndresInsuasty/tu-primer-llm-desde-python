import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROVEEDORES = {
    "ollama": {
        "base_url": "http://localhost:11434/v1",
        "api_key": "OLLAMA",
        "modelo": "llama3.2:3b"
    },
    "openai": {
        "base_url": None,
        "api_key": os.getenv("OPENAI_API_KEY"),
        "modelo": "gpt-6-luna"
    },
}

def crear_cliente(proveedor: str|None = None) -> tuple[OpenAI, str]:
    """Devuelve (cliente, modelo) según el proveedor seleccionado"""
    proveedor = proveedor or os.getenv("PROVEEDOR", "ollama")
    if proveedor not in PROVEEDORES:
        raise ValueError(f"Proveedor desconocido: '{proveedor}'. Usa uno de: {', '.join(PROVEEDORES)}")
    config = PROVEEDORES[proveedor]
    if not config["api_key"]:
        raise ValueError("Falta OPENAI_API_KEY en tu archivo .env (copia .env.example como .env)")

    cliente = OpenAI(base_url=config["base_url"], api_key=config["api_key"])
    return cliente, config["modelo"]
