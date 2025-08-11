import json
from langflow.custom.custom_component.component import Component
from langflow.io import MessageTextInput, Output
from langflow.schema import Data
from langflow.logging import logger


class JsonLoads(Component):
    display_name = "JSON Loads"
    description = "Limpa e carrega um JSON a partir de texto, ignorando marcações como ```json."
    icon = "braces"

    inputs = [
        MessageTextInput(
            name="raw_json",
            display_name="JSON Bruto",
            info="Texto que contém o JSON, possivelmente com marcações Markdown.",
            required=True,
        ),
    ]

    outputs = [
        Output(
            display_name="JSON",
            name="clean_json",
            method="clean_and_load",
            info="Retorna um objeto Data com o JSON parseado.",
        )
    ]

    def clean_and_load(self) -> Data:
        raw_text = self.raw_json

        # Remove blocos de markdown ```...```
        cleaned = raw_text.replace("```json", "").strip()
        cleaned = cleaned.replace("```", "").strip()

        try:
            parsed = json.loads(cleaned)
            self.status = "JSON carregado com sucesso."
            return Data(data=parsed)
        except json.JSONDecodeError as e:
            logger.error(f"Erro ao parsear JSON: {e}")
            self.status = f"Erro ao parsear JSON: {e}"
            return Data(data={})
