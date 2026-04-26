# Controle de Equipamentos - Escola

Aplicação Django para controlar equipamentos vinculados a salas e status.

## Instalação

1. Crie um ambiente virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Instale dependências:

```powershell
pip install -r requirements.txt
```

3. Crie e execute migrações:

```powershell
python manage.py makemigrations
python manage.py migrate
```

4. Crie um superusuário:

```powershell
python manage.py createsuperuser
```

5. Carregue os status iniciais:

```powershell
python manage.py loaddata inventory/fixtures/status_initial.json
```

6. Execute o servidor:

```powershell
python manage.py runserver
```

## Modelo de dados

- Sala: nome, descrição
- Status: nome, descrição
- Equipamento: nome, sala, status, data de atualização
