from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from random import randint, sample
from static.listas_de_nomes import listas_de_nomes, nomes_por_numero,nomes_por_numero_lab,nomes_por_numero_lab,listas_de_nomes_lab
from typing import List



# Configuração do banco de dados SQLite
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Definição do modelo de sorteio
class Sorteio(Base):
    __tablename__ = "sorteios"
    id = Column(Integer, primary_key=True, index=True)
    equipe1 = Column(Integer)
    equipe2 = Column(Integer)

# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app= FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    
# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def sortear_numeros(db: Session = Depends(get_db)):
    sorteios = db.query(Sorteio).order_by(Sorteio.id.desc()).limit(10).all()
    numeros_proibidos = set()
    numeros_proibidos2 = set()
    for sorteio in sorteios:
        numeros_proibidos.add(sorteio.equipe1)
        numeros_proibidos2.add(sorteio.equipe2)

    print(numeros_proibidos)
    equipe1 = randint(1,58)


    while equipe1 == 22 or equipe1 == 23:
         equipe1 = randint(1,58)

    equipe2= randint(1,58)
    while equipe2 == equipe2 == 22 or equipe2 == 23:
        equipe2 = randint(1,58)
    
    #Garantir que os números não sejam iguais
    while equipe2 == equipe1:
          equipe2 = randint(1,58)

    while equipe1 in numeros_proibidos or equipe2 in numeros_proibidos2 or equipe1 == equipe2:
        equipe1 = randint(1, 58)
        equipe2 = randint(1, 58)

    # Armazena o sorteio no banco de dados
    novo_sorteio = Sorteio(equipe1=equipe1, equipe2=equipe2)
    db.add(novo_sorteio)
    db.commit()


    lista_associada1 = listas_de_nomes[equipe1]() if equipe1 == 52 else listas_de_nomes.get(equipe1, [])
    lista_associada2 = listas_de_nomes[equipe2]() if equipe2 == 52 else listas_de_nomes.get(equipe2, [])

   

    
    return equipe1, equipe2, lista_associada1, lista_associada2
def sortear_numeros_lab():
    equipe1 = randint(1,4)
    equipe2= randint(1,4)

    
    #Garantir que os números não sejam iguais
    while equipe2 == equipe1:
          equipe2 = randint(1,5)

    lista_associada1 = listas_de_nomes_lab[equipe1]() if equipe1 == 52 else listas_de_nomes_lab.get(equipe1, [])
    lista_associada2 = listas_de_nomes_lab[equipe2]() if equipe2 == 52 else listas_de_nomes_lab.get(equipe2, [])

   

    
    return equipe1, equipe2, lista_associada1, lista_associada2
    
@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/laboratorio", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("lab.html", {"request": request})


@app.post("/sorteio",response_class=HTMLResponse)
async def sorteio(request: Request, db: Session = Depends(get_db)):
     equipe1, equipe2, lista_associada1, lista_associada2 = sortear_numeros(db)
     nome_associado1 = nomes_por_numero.get(equipe1, "Nome Padrão 1")
     nome_associado2 = nomes_por_numero.get(equipe2, "Nome Padrão 2")

     return templates.TemplateResponse("index.html", {
         "request": request,
         "numero1": equipe1,
         "nomes_associados1": lista_associada1,
         "numero2": equipe2,
         "nomes_associados2": lista_associada2,
         "nome_associado1": nome_associado1,
         "nome_associado2": nome_associado2,
         })
     
@app.post("/sorteiolaboratorio",response_class=HTMLResponse)
async def sorteio(request: Request, db: Session = Depends(get_db)):
     equipe1, equipe2, lista_associada1, lista_associada2 = sortear_numeros_lab()
     nome_associado1 = nomes_por_numero_lab.get(equipe1, "Nome Padrão 1")
     nome_associado2 = nomes_por_numero_lab.get(equipe2, "Nome Padrão 2")

     return templates.TemplateResponse("lab.html", {
         "request": request,
         "numero1": equipe1,
         "nomes_associados1": lista_associada1,
         "numero2": equipe2,
         "nomes_associados2": lista_associada2,
         "nome_associado1": nome_associado1,
         "nome_associado2": nome_associado2,
         })




