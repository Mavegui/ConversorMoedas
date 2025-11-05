# Conversor Moedas - Gui Feitosa (Mavegui)

Projeto conversor de moedas, trabalho da faculdade. 

Este projeto tem como objetivo aplicar a metodologia ágil Scrum, proposto pela disciplina projeto de software no curso de Engenharia de Software.  

Com objetivo de realizar a estruturação desde a fase inicial abordando todas as etapas do projeto como product backlog, Sprint 1 e 2, revisão, teste e concluído.

---

## Tecnologias utilizadas
- **Django**  
- **Bootstrap**  
- **Frankfurter API**
- **Scrum**    

---

## Arquivos trabalhados
  
Veja arquivos usados e criado como orientação para realização do projeto.

- **[Enunciado do trabalho](./arquivos/enunciado.pdf)**
- **[Trello imagem quadro Scrum](./arquivos/Trello_Scrum.png)**
- **[Relatório final do projeto](./arquivos/Trabalho_projeto_de_software.pdf)**

---

## Instalação

- Clone o repositório.
  ```plaintext
     https://github.com/Mavegui/ConversorMoedas.git
  ```
- Instale o ambiente virtual e execute ele.
  ```plaintext
    Instalar venv:
    python3 -m venv .venv

    Executar venv:
    source .venv/bin/activate   
  ```
- Execute migrations. 
  ```plaintext
    Rodar migrations:
    python3 -m venv .venv 
  ```
- Executar o servidor:
  ```plaintext
    Executar o projeto:
    python3 manage.py runserver

    Acesse o link gerado. 
  ```

---

## Estrutura do projeto baixado

```plaintext
.
├── .venv
├── arquivos
│   ├── enunciado.pdf
│   ├── Trello_Scrum.png
│   └── Trabalho_projeto_de_software.pdf
├── conversormoedas_app
│   ├── migrations
│   ├── static
│   │   ├── CSS
│   │   │   └── style.css
│   │   ├── js
│   │   │   └── conversor.js
│   ├── templates
│   │   ├── conversor
│   │   │   ├── index.html
│   │   │   └── layout.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py   
│   ├── urls.py
│   └── views.py
├── conversormoedas_root
│   ├── asgi.py
│   ├── settings.py   
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── db.sqlite3
├── manage.py
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Licença
Este projeto está licenciado sob a [MIT License](./LICENSE).
