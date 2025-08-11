from langflow.custom.custom_component.component import Component
from langflow.io import FloatInput, Output, MessageTextInput
from langflow.schema import Data


class FeasibilityStudyComponent(Component):
    display_name = "Feasibility Study"
    description = "Calcula viabilidade com base em coeficientes urbanísticos, área de outorga e VGV."
    icon = "calculator"

    inputs = [
        MessageTextInput(
            name="lot_area",
            display_name="Área do Terreno (m²)",
            info="Área total do terreno em metros quadrados.",
            required=True,
            tool_mode=True
        ),
        MessageTextInput(
            name="indice_basico",
            display_name="Coeficiente Básico",
            info="Coeficiente de aproveitamento básico permitido pela legislação.",
            required=True,
            tool_mode=True
        ),
        MessageTextInput(
            name="indice_maximo",
            display_name="Coeficiente Máximo",
            info="Coeficiente máximo permitido com outorga onerosa.",
            required=True,
            tool_mode=True
        ),
        MessageTextInput(
            name="valor_outorga_m2",
            display_name="Valor m² Outorga (R$)",
            info="Valor do metro quadrado da outorga onerosa.",
            required=True,
            tool_mode=True
        ),
        MessageTextInput(
            name="valor_m2",
            display_name="Valor m² de Venda (R$)",
            info="Valor estimado do metro quadrado de venda (para VGV).",
            required=True,
            tool_mode=True
        ),
    ]

    outputs = [
        Output(
            display_name="Estudo de Viabilidade (Data)",
            name="viability_result",
            method="calculate_viability",
            info="Retorna os cálculos de viabilidade em formato Data.",
        )
    ]

    def calculate_viability(self) -> Data:
        try:
            area_terreno = float(self.lot_area)
            indice_basico = float(self.indice_basico)
            indice_maximo = float(self.indice_maximo)
            valor_outorga_m2 = float(self.valor_outorga_m2)
            valor_m2 = float(self.valor_m2)
        except Exception as e:
            self.status = f"Erro de conversão: {e}"
            return Data(data={"error": self.status})

        area_computavel = area_terreno * indice_basico
        area_outorga = max(0, (indice_maximo - indice_basico) * area_terreno)
        area_total = area_computavel + area_outorga
        custo_outorga = area_outorga * valor_outorga_m2
        vgv = area_computavel * valor_m2

        resultado = {
            "area_computavel": round(area_computavel, 2),
            "area_outorga": round(area_outorga, 2),
            "area_total": round(area_total, 2),
            "valor_m2": round(valor_m2, 2),
            "valor_outorga_m2": round(valor_outorga_m2, 2),
            "custo_outorga": round(custo_outorga, 2),
            "vgv_estimado": round(vgv, 2),
        }

        self.status = "Cálculo de viabilidade concluído."
        return Data(data=resultado)
