FROM langflowai/langflow:latest

# garante permissões de root
USER root

# instala dependências nativas para o geopandas funcionar
RUN apt-get update && apt-get install -y \
    g++ python3-dev libgeos-dev libproj-dev proj-data proj-bin libproj-dev libspatialindex-dev \
    && rm -rf /var/lib/apt/lists/*

# copia requirements para dentro do container
COPY requirements.txt /app/requirements.txt

# instala dependências Python
RUN /app/.venv/bin/python -m ensurepip \
    && /app/.venv/bin/python -m pip install --upgrade pip \
    && /app/.venv/bin/python -m pip install --no-cache-dir -r /app/requirements.txt
