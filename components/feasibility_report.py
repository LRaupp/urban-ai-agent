from pathlib import Path

from langflow.custom.custom_component.component import Component
from langflow.schema.message import Message
from langflow.io import (
    Output,
    MessageTextInput
)

TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório - {nome_estudo}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}
        
        .container {{
            width: 210mm;
            min-height: 297mm;
            background: #ffffff;
            box-shadow: 0 25px 80px rgba(0,0,0,0.3);
            border-radius: 16px;
            overflow: hidden;
            position: relative;
        }}
        
        .container::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 15% 25%, rgba(79, 172, 254, 0.06) 0%, transparent 60%),
                radial-gradient(circle at 85% 15%, rgba(120, 119, 198, 0.08) 0%, transparent 60%),
                radial-gradient(circle at 50% 85%, rgba(255, 154, 158, 0.05) 0%, transparent 60%),
                linear-gradient(135deg, rgba(79, 172, 254, 0.02), rgba(120, 119, 198, 0.02));
            pointer-events: none;
        }}
        
        .report-container {{
            position: relative;
            z-index: 1;
            padding: 50px 60px;
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 50px;
            position: relative;
            padding-bottom: 30px;
        }}
        
        .header::after {{
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 120px;
            height: 4px;
            background: linear-gradient(90deg, #4facfe, #00f2fe);
            border-radius: 2px;
        }}
        
        .main-title {{
            font-size: 42px;
            font-weight: 900;
            color: #1a202c;
            margin-bottom: 12px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -1px;
        }}
        
        .subtitle {{
            font-size: 18px;
            color: #718096;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 2px;
        }}
        
        .study-name {{
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            padding: 25px 35px;
            border-radius: 16px;
            text-align: center;
            margin-bottom: 40px;
            box-shadow: 0 15px 35px rgba(79, 172, 254, 0.3);
        }}
        
        .study-name h2 {{
            font-size: 28px;
            font-weight: 700;
            margin-bottom: 8px;
        }}
        
        .study-name p {{
            font-size: 16px;
            opacity: 0.9;
            font-weight: 400;
        }}
        
        .section {{
            margin-bottom: 35px;
            background: rgba(255, 255, 255, 0.7);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.08);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        
        .section-title {{
            font-size: 22px;
            font-weight: 700;
            color: #2d3748;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            gap: 12px;
            padding-bottom: 15px;
            border-bottom: 2px solid #e2e8f0;
        }}
        
        .section-title .icon {{
            font-size: 24px;
        }}
        
        .data-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 25px;
        }}
        
        .data-grid.single {{
            grid-template-columns: 1fr;
        }}
        
        .data-item {{
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.05);
            border-left: 4px solid #4facfe;
            transition: all 0.3s ease;
        }}
        
        .data-item:hover {{
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        }}
        
        .data-item.full-width {{
            grid-column: 1 / -1;
        }}
        
        .data-label {{
            font-size: 13px;
            font-weight: 600;
            color: #718096;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 8px;
        }}
        
        .data-value {{
            font-size: 18px;
            font-weight: 700;
            color: #2d3748;
            line-height: 1.2;
        }}
        
        .data-value.large {{
            font-size: 22px;
        }}
        
        .financial-section .data-item {{
            border-left-color: #48bb78;
        }}
        
        .financial-section .data-value {{
            color: #38a169;
        }}
        
        .vgv-highlight {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            margin-top: 40px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
        }}
        
        .vgv-highlight::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: rotate 15s linear infinite;
        }}
        
        @keyframes rotate {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
        
        .vgv-content {{
            position: relative;
            z-index: 1;
        }}
        
        .vgv-title {{
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 15px;
            opacity: 0.9;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .vgv-value {{
            font-size: 48px;
            font-weight: 900;
            margin-bottom: 10px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .vgv-subtitle {{
            font-size: 16px;
            opacity: 0.8;
            font-weight: 500;
        }}
        
        .location-section {{
            background: linear-gradient(135deg, rgba(72, 187, 120, 0.1), rgba(56, 161, 105, 0.05));
        }}
        
        .zoning-section {{
            background: linear-gradient(135deg, rgba(79, 172, 254, 0.1), rgba(0, 242, 254, 0.05));
        }}
        
        .financial-section {{
            background: linear-gradient(135deg, rgba(236, 201, 75, 0.1), rgba(245, 158, 11, 0.05));
        }}
        
        @media print {{
            body {{
                background: white;
                margin: 0;
                padding: 0;
            }}
            
            .container {{
                width: 100%;
                min-height: auto;
                box-shadow: none;
                border-radius: 0;
                margin: 0;
            }}
            
            .vgv-highlight::before {{
                animation: none;
            }}
        }}
        
        /* Animações de entrada */
        .section {{
            animation: slideIn 0.8s ease-out;
            animation-fill-mode: both;
        }}
        
        .section:nth-child(1) {{ animation-delay: 0.1s; }}
        .section:nth-child(2) {{ animation-delay: 0.2s; }}
        .section:nth-child(3) {{ animation-delay: 0.3s; }}
        .section:nth-child(4) {{ animation-delay: 0.4s; }}
        .section:nth-child(5) {{ animation-delay: 0.5s; }}
        
        @keyframes slideIn {{
            from {{
                opacity: 0;
                transform: translateX(-30px);
            }}
            to {{
                opacity: 1;
                transform: translateX(0);
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="report-container">
            <div class="header">
                <h1 class="main-title">RELATÓRIO TÉCNICO</h1>
                <p class="subtitle">Estudo de Viabilidade Imobiliária</p>
            </div>
            
            <div class="study-name">
                <h2>{nome_estudo}</h2>
                <p>Análise Completa de Viabilidade</p>
            </div>
            
            <div class="section location-section">
                <div class="section-title">
                    <span class="icon">📍</span>
                    <span>Localização do Empreendimento</span>
                </div>
                <div class="data-grid">
                    <div class="data-item">
                        <div class="data-label">Cidade</div>
                        <div class="data-value">{cidade}</div>
                    </div>
                    <div class="data-item">
                        <div class="data-label">Estado</div>
                        <div class="data-value">{estado}</div>
                    </div>
                    <div class="data-item full-width">
                        <div class="data-label">Endereço do Terreno</div>
                        <div class="data-value large">{endereco_terreno}</div>
                    </div>
                </div>
            </div>
            
            <!-- Seção Zoneamento -->
            <div class="section zoning-section">
                <div class="section-title">
                    <span class="icon">🏗️</span>
                    <span>Parâmetros de Zoneamento</span>
                </div>
                <div class="data-grid">
                    <div class="data-item">
                        <div class="data-label">Zona</div>
                        <div class="data-value">{zona}</div>
                    </div>
                    <div class="data-item">
                        <div class="data-label">Área do Lote</div>
                        <div class="data-value">{area_lote}</div>
                    </div>
                    <div class="data-item">
                        <div class="data-label">Índice Básico</div>
                        <div class="data-value">{indice_basico}</div>
                    </div>
                    <div class="data-item">
                        <div class="data-label">Índice Máximo</div>
                        <div class="data-value">{indice_maximo}</div>
                    </div>
                </div>
            </div>
            
            <div class="section financial-section">
                <div class="section-title">
                    <span class="icon">💰</span>
                    <span>Informações Financeiras</span>
                </div>
                <div class="data-grid">
                    <div class="data-item">
                        <div class="data-label">Valor do m²</div>
                        <div class="data-value">{valor_m2}</div>
                    </div>
                    <div class="data-item">
                        <div class="data-label">Valor de Outorga</div>
                        <div class="data-value">{valor_outorga}</div>
                    </div>
                </div>
            </div>
            
            <!-- VGV em Destaque -->
            <div class="vgv-highlight">
                <div class="vgv-content">
                    <div class="vgv-title">🎯 VGV - Valor Geral de Vendas</div>
                    <div class="vgv-value">{vgv}</div>
                    <div class="vgv-subtitle">Potencial Total do Empreendimento</div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""

class FeasibilityReportComponent(Component):
    display_name = "Feasibility Report Generator"
    description = "Gera um relatório HTML de estudo imobiliário com base nos parâmetros fornecidos."
    icon = "file-text"

    inputs = [
        MessageTextInput(
            name="nome_estudo",
            display_name="Nome do Estudo",
            required=True,
            tool_mode=True,
        ),
        MessageTextInput(
            name="cidade",
            display_name="Cidade",
            required=True,
            tool_mode=True,
        ),
        MessageTextInput(
            name="estado",
            display_name="Estado (UF)",
            required=True,
            tool_mode=True,
        ),
        MessageTextInput(
            name="endereco_terreno",
            display_name="Endereço do Terreno",
            required=True,
            tool_mode=True,
        ),
        MessageTextInput(
            name="area_lote",
            display_name="Área do Lote (m²)",
            required=True,
            tool_mode=True,
        ),
        MessageTextInput(
            name="zona",
            display_name="Zona",
            required=True,
            tool_mode=True,
        ),
        MessageTextInput(
            name="indice_basico",
            display_name="Índice Básico",
            required=True,
            tool_mode=True,
        ),
        MessageTextInput(
            name="indice_maximo",
            display_name="Índice Máximo",
            required=True,
            tool_mode=True,
        ),
        MessageTextInput(
            name="valor_m2",
            display_name="Valor do m² (R$)",
            required=True,
            tool_mode=True,
        ),
        MessageTextInput(
            name="valor_outorga",
            display_name="Valor da Outorga (R$)",
            required=True,
            tool_mode=True,
        ),
        MessageTextInput(
            name="vgv",
            display_name="VGV (R$)",
            required=True,
            tool_mode=True,
        ),
        MessageTextInput(
            name="caminho_pasta",
            display_name="Caminho da Pasta",
            required=True,
        ),
    ]

    outputs = [
        Output(
            display_name="Caminho do Arquivo",
            name="relatorio_html",
            method="generate_report",
            info="Retorna o caminho do arquivo HTML gerado.",
        )
    ]

    def generate_report(self) -> Message:
        """
        Gera um relatório HTML de estudo imobiliário.
        """
        html_content = TEMPLATE.format(
            nome_estudo=self.nome_estudo,
            cidade=self.cidade,
            estado=self.estado,
            endereco_terreno=self.endereco_terreno,
            area_lote=self.area_lote,
            zona=self.zona,
            indice_basico=self.indice_basico,
            indice_maximo=self.indice_maximo,
            valor_m2=self.valor_m2,
            valor_outorga=self.valor_outorga,
            vgv=self.vgv
        )
        
        Path(self.caminho_pasta).mkdir(parents=True, exist_ok=True)
        # Exemplo de placeholder de retorno:
        caminho_arquivo = f"{self.caminho_pasta}/relatorio_{self.nome_estudo}.html"
        
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(html_content)
        
        self.status = "Relatório gerado com sucesso (placeholder)."
        
        return Message(text=caminho_arquivo)
