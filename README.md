<div class="title-block" style="text-align: center;" align="center">


![Python Version](https://img.shields.io/python/required-version-toml?tomlFilePath=http%3A%2F%2Fraw.githubusercontent.com%2Fwsdoprado%2Fevent-driven-automation%2Frefs%2Fheads%2Fmain%2Fpyproject.toml)

# Curso - WTR POP RR - NIC.br

Este repositório contém os arquivos e instruções para o laboratório do curso de Automacao - WTR - POP RR


**[Pré-requisitos](#-pré-requisitos) &nbsp;&nbsp;&bull;&nbsp;&nbsp;**
**[Instalação das Dependências](#-instalação-das-dependências) &nbsp;&nbsp;&bull;&nbsp;&nbsp;**
**[NetBox (IPAM/DCIM)](#-netbox-ipamdcim) &nbsp;&nbsp;&bull;&nbsp;&nbsp;**
**[Laboratório com Containerlab](#-laboratório-com-containerlab) &nbsp;&nbsp;&bull;&nbsp;&nbsp;**
**[Ambiente para executar os exercícios](#ambiente-para-executar-os-exercícios) &nbsp;&nbsp;&bull;&nbsp;&nbsp;**
**[Exercícios de Automação de Rede](#-iniciando-os-exercícios-de-automação-de-rede) &nbsp;&nbsp;&bull;&nbsp;&nbsp;**
**[Projeto Final](#-projeto-final) &nbsp;&nbsp;&bull;&nbsp;&nbsp;**
**[Referências](#-referências)**

</div>

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de que o sistema possui:

- **Linux (Debian 12.10.0 netinst instalação limpa) - 1 host [16G RAM(ou mais), 50G Disco, 8vcpu (ou mais)]**
- Acesso a Internet para download de arquivos
- IDE para visualizar arquivos .py, compose.yml, Dockerfile. (VS Code, Pycharm)
  
## 🚀 Instalação das Dependências

Instalac̨ão do GIT

```bash
apt install git -y
```

Git clone do Repositorio

```bash
cd /opt
git clone https://github.com/wsdoprado/wtr-pop-rr-2025.git
```

Execute o script abaixo para instalar as dependências necessárias:

```bash
cd /opt/wtr-pop-rr-2025/
./install_dependencies.sh
```

## 📦 NetBox (IPAM/DCIM)

O NetBox será utilizado como fonte da verdade - NSOT

```bash
cd /opt
git clone -b release https://github.com/netbox-community/netbox-docker.git
```
```bash
cd netbox-docker
```
```bash
tee docker-compose.override.yml <<EOF
services:
  netbox:
    ports:
      - 8000:8080
EOF
```
```bash
docker compose pull
```

alterar o docker-compose.yml (depende de cada cenario)

```bash
start_period: 500s
timeout: 30s
interval: 30s
retries: 5
```

Para subir
```bash
docker compose up
```
ou
```bash
docker compose up -d
```

Definir ou alterar o usuário de acesso
```bash
docker compose exec netbox /opt/netbox/netbox/manage.py createsuperuser
```

O NetBox estará disponível em:
👉 http://localhost:8000

## 🧪 Laboratório com Containerlab

Baixe as imagens de Arista cEOS:
📂 Google Drive - Imagens de Laboratório
 - https://drive.google.com/drive/folders/1uLDcgJuoxOE7c4ZD3WsPwLmvPrJKqeLE

OBS: cEOS-lab-4.34.2F.tar.xz precisa estar no host do laboratório.
Dica: Transferir por SCP

### Dados de acesso aos equipamento
- user: admin
- password: admin

# Criando o container para Arista cEOS
Importe a imagem do Arista cEOS:
```bash
docker import cEOS-lab-4.34.2F.tar.xz ceos:4.34.2F
```

# Criando o laboratório do curso
Suba o laboratório de exemplo:
```bash
containerlab deploy -t wtr.yml
```

Destrua um laboratório específico:
```bash
containerlab destroy -t wtr.yml --cleanup
```

Liste e inspecione laboratórios ativos:
```bash
containerlab inspect --all
```

## Ambiente para executar os exercícios
### 🐍 Ambiente Python para execução dos scripts

Para executar os scripts em python é necessário criar um ambiente virtual e instalar as dependências.

Por padrão, o uv é instalado em ~/.local/bin. Para poder usá-lo de qualquer lugar no terminal, é necessário adicionar esse diretório ao PATH.
```bash
export PATH=$PATH:/root/.local/bin
```
Criar o ambiente virtual
```bash
uv venv
```
Ativar o ambiente virtual
```bash
source .venv/bin/activate
```
Instalar ou atualizar as dependências dentro do ambiente virtual
```bash
uv sync
```
Sair do ambiente virtual
```bash
deactivate
```

## 🖥️ Iniciando os Exercícios de Automação de Rede

Criar um arquivo .env.dev na raiz do projeto. E modificar os dados de acordo
```bash
cp .env.dev.example .env.dev
```
Esse arquivo será utilizado tanto nos exercícios quanto no projeto completo para fornecer os dados de acesso entre os serviços.


## 📚 Referências
- [Slides apresentação no Drive](https://drive.google.com/drive/folders/1uLDcgJuoxOE7c4ZD3WsPwLmvPrJKqeLE)
- [Documentação Pyeapi](https://pyeapi.readthedocs.io/en/master/index.html)
- [Documentação Netbox](https://netboxlabs.com/docs/welcome/)



