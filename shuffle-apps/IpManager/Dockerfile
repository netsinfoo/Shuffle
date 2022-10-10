# Imagem base do nosso aplicativo na imagem do SDK do aplicativo WALKOFF
FROM frikky/shuffle:python3-playground_1.0.0 as base

# Eliminamos todo o inchaço das ferramentas de compilação, criando um estágio do construtor
FROM base as builder

# Instale-se todas as ferramentas de construção alpine necessárias 
RUN apk --no-cache add --update alpine-sdk libffi libffi-dev musl-dev openssl-dev py3-pip

# Instale todos os nossos pacotes pip em um único diretório copiando para imagem base
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --prefix="/install" -r /requirements.txt

# Volte para imagem base e copie em todos os nossos pacotes construídos e código-fonte
FROM base
COPY --from=builder /install /usr/local
COPY src /app

# Finalmente subimos a aplicação
WORKDIR /app
CMD python app.py --log-level DEBUG
