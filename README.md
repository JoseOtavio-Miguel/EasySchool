# Easy School - Sistema de Gestão Escolar Inteligente

## 📋 Índice
- [Visão Geral](#-visão-geral)
- [Características Principais](#-características-principais)
- [Tipos de Usuários](#-tipos-de-usuários)
- [Funcionalidades](#-funcionalidades)
- [Solução de Problemas Comuns](#-solução-de-problemas-comuns)
- [Instalação e Execução do Sistema](#-instalação-e-execução-do-sistema)
- [Contribuição](#-contribuição)


---

## 🎯 Visão Geral
O **Easy School** é uma plataforma completa de gestão escolar projetada para modernizar e simplificar a administração de instituições educacionais. Com uma interface intuitiva e moderna, o sistema integra todas as funcionalidades necessárias para gerenciar alunos, professores, turmas, cursos e finanças em uma única solução.

⚠️ **Nota Importante:**  
Os números apresentados nas imagens (como "+500 escolas usando", "+50k usuários ativos", "99% satisfação") são exemplos ilustrativos e não representam dados reais.

---

## ✨ Características Principais

### 📱 Totalmente Responsivo
- Interface adaptável para qualquer dispositivo
- Design mobile-first
- Experiência consistente em todos os navegadores

### 🛠️ Suporte Completo
- Interface intuitiva que não requer treinamento extenso
- Documentação clara e exemplos práticos
- Sistema projetado para fácil manutenção

---

## 👥 Tipos de Usuários
### 🎓 Estudante
- Acesso às notas e histórico escolar
- Consulta de frequência e horários
- Download de materiais de estudo
- Visualização de atividades e prazos
- Comunicação com professores

### 👨‍🏫 Professor
- Gerenciamento de turmas e alunos
- Lançamento de notas e avaliações
- Controle de frequência detalhado
- Planejamento de aulas e atividades
- Comunicação com alunos e responsáveis

### 👨‍👩‍👧‍👦 Responsável
- Acompanhamento do desempenho de dependentes
- Acesso a boletins e relatórios
- Comunicação com a escola
- Gestão financeira escolar
- Recebimento de comunicados

### ⚙️ Administrador
- Gestão completa da instituição
- Controle de usuários e permissões
- Relatórios financeiros e estatísticos
- Configurações do sistema
- Integração com outros sistemas

---

## 🚀 Funcionalidades
### 📊 Dashboard Inteligente
- Métricas em tempo real
- Gráficos interativos
- Alertas e notificações personalizadas
- Visão geral rápida de todas as áreas

### 🎯 Gestão Acadêmica
- Matrículas e rematrículas online
- Grade curricular flexível
- Calendário escolar integrado
- Histórico completo do aluno

### 💰 Gestão Financeira
- Controle de mensalidades e taxas
- Emissão de lembretes de pagamento
- Relatórios financeiros detalhados
- Controle de fluxo de caixa

### 📋 Comunicação Integrada
- Portal de comunicados oficial
- Agenda de eventos escolar
- Sistema de mensagens interno
- Notificações importantes

---

## 🐛 Solução de Problemas Comuns
### Problema: "ModuleNotFoundError"

```bash
# Verifique se o ambiente virtual está ativado
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Verifique instalação do Django
pip list | grep Django
```

### Problema: Erros de Migração
```bash
# Resetar migrações (DEV apenas!)
python manage.py migrate --fake [app_name] zero
python manage.py makemigrations [app_name]
python manage.py migrate [app_name]
```

### Problema: Banco de dados corrompido
```bash
# Backup primeiro!
cp db.sqlite3 db_backup.sqlite3

# Recriar banco
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

---
## 🚀 Instalação e Execução do Sistema

Siga os passos abaixo para instalar e rodar o **EasySchool** localmente.
### 📋 Pré-requisitos

Certifique-se de ter instalado em sua máquina:

- 🐍 **Python 3.10+**
- 📦 **pip** (gerenciador de pacotes do Python)
- 🌐 **Git**
- 🗄️ **SQLite** (já incluso no Python)
- (Opcional) 🧰 **Virtualenv**

### 📥 Clonando o Repositório

```bash
git clone https://github.com/seu-usuario/easyschool.git
cd easyschool
```

### 🧪 Criando e Ativando o Ambiente Virtual

- Windows
```bash
python -m venv venv
venv\Scripts\activate
```

- Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

- Instalando as Dependências
```bash
pip install -r requirements.txt
```
---

## ⚙️ Configurando o Banco de Dados

### Execute as migrações para criar as tabelas no banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 👤 Criando um Superusuário (Opcional)

Para acessar o painel administrativo do Django:

```bash
python manage.py createsuperuser
```

### ▶️ Executando o Servidor
```bash
python manage.py runserver
```


### Acesse no navegador:

- 🌐 Página inicial: http://127.0.0.1:8000/

- 🔐 Admin Django: http://127.0.0.1:8000/admin/



### 🧠 Dicas Úteis

- Caso ocorra erro de migração, veja a seção 🐛 Solução de Problemas

- Sempre ative o ambiente virtual antes de rodar o projeto

- Use python manage.py runserver 0.0.0.0:8000 para acesso em rede local

---

## 🤝 Contribuição

### Contribuições são **muito bem-vindas**!  
### Se você deseja melhorar o **EasySchool**, siga os passos abaixo:

1. 🍴 Faça um **Fork** do projeto  
2. 🌱 Crie uma nova branch para sua feature:
   ```bash
   git checkout -b feature/nova-funcionalidade


---

## ⭐ Se este projeto foi útil, dê uma estrela no GitHub!

