# FastAPI-CRUD
# .env

```
SECRET_KEY=8a7354a1b97dd9d6a2cf435855c5334f2632a6f91261a9cf6b26976c7ee074a5
ALGORITHM=HS256
DATABASE_URL=mysql+mysqlconnector://root:@localhost:3306/mydatabase
URL_ONE=http://localhost:8000
URL_TWO=https://localhost:8000
```

# installation

```
pip3 install -r requirements.txt
```

# migration

```
cd src/
alembic upgrade head
```

# Run application

```
cd src/
python3 main.py
```
