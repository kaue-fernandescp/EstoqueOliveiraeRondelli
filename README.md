# ⚖️ Oliveira & Rondelli Advocacia
Este projeto é uma aplicação web completa desenvolvida para o escritório Oliveira & Rondelli Advocacia.

🚀 Sobre o Projeto

O sistema consiste numa aplicação de estoque para registrar as movimentações de entrada e saída dos produtos, bem como o cadastro de produtos. Além disso, conta com uma autenticação para registro e auditorias. O sistema foi construído utilizando o framework Django.

🧰 Tecnologias Utilizadas
- Linguagem: Python 3.14+
- Framework Web: Django 6.0+
- Banco de Dados: SQLite
- Front-end: Django Templates, HTML5 e CSS3 modular.

📂 Estrutura de Pastas (Principais Apps)
- EstoqueOliveiraeRondelli/: Principais configurações do projeto.
- core/: Páginas institucionais e arquivos estáticos globais.
- produtos/: Gerenciamento de itens do estoque e unidades.
- usuarios/: Gerenciamento dos usuários do sistema.
- movimentacoes/: Gerenciamento do estoque com as operações de entrada e saída.
- relatorios/: Relatórios do sistema.
- static/: Estilização.

🔧 Para acessar a aplicação:
- Clique no seguinte link: https://kauefernandescp.pythonanywhere.com/login/

🔧 Para executar a aplicação local:
- Clone o repositório: git clone https://github.com/kaue-fernancescp/EstoqueOliveiraeRondelli.git
- Crie um ambiente virtual: python -m venv venv
- Ative o ambiente:

Windows: venv\Scripts\activate
Linux/Mac: source venv/bin/activate

- Instale as dependências: pip install django
- Inicie o servidor: python manage.py runserver
