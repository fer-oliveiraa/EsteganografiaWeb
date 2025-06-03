# 🕵️‍♂️ Esteganografia em Imagens - Plataforma Web

Projeto prático de Computação Gráfica: uma plataforma web para esconder e revelar mensagens secretas em imagens utilizando a técnica de LSB (Least Significant Bit).

## Objetivo

Permitir ao usuário:
- Inserir uma mensagem secreta em uma imagem (preferencialmente PNG).
- Enviar uma imagem modificada e descobrir se há uma mensagem secreta escondida.

## Tecnologias Utilizadas

- **Backend**: Python + Flask
- **Processamento de imagem**: Pillow
- **Frontend**: HTML + CSS
- **Hospedagem**: Render

## Acesse a Plataforma

https://esteganografia-web.onrender.com

---

## Funcionalidades

### Inserir mensagem em imagem

- Upload de imagem (PNG de preferência)
- Campo para digitar a mensagem secreta
- Botão para codificar a mensagem na imagem
- Download automático da imagem com a mensagem

### Ler mensagem de imagem

- Upload da imagem possivelmente modificada
- Botão para extrair e exibir a mensagem secreta (caso exista)

---

## Como Rodar Localmente

1. Clone este repositório:
   git clone https://github.com/fer-oliveiraa/EsteganografiaWeb.git

2. Crie um ambiente virtual e ative:
   python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows

3. Instale as dependências:
   pip install -r requirements.txt

4. Execute a aplicação:
   python app.py

5. Acesse em: http://localhost:5000
   
  
