import sqlalchemy,databases
from fastapi import FastAPI
from pydantic import BaseModel,Field, main
#from sqlalchemy.sql.sqltypes import CHAR
from typing import List
from fastapi.middleware.cors import CORSMiddleware
## postgres database
DATABASE_URL = "postgresql://postgres:1234@127.0.0.1:5432/db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

fruits = sqlalchemy.Table(
    "fruits",
    metadata,
    sqlalchemy.Column("name" ,sqlalchemy.String,primary_key=True),
    sqlalchemy.Column("alias" ,sqlalchemy.String),
    sqlalchemy.Column("varities" ,sqlalchemy.String),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)


## Models
class fruitlist(BaseModel):
    name : str
    alias : str
    varities : str

class fruit(BaseModel):
    name : str

class fruitAlias(BaseModel):
    name : str
    alias : str

class fruitEntry(BaseModel):
    name : str = Field(...,example="anc")
    alias : str = Field(...,example="abcd")
    varities : str = Field(...,example="abx")
    
'''
    class Config:
        orm_mode = True
'''

class fruitupdate(BaseModel):
    name : str = Field(...,example="Enter the fruit name")
    alias : str = Field(...,example="abcd")
    varities : str = Field(...,example="abx")
    

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/fruits",response_model=List[fruitlist])
async def find_fruits(search:str=""):
   # query_colmns='SELECT TOP 1* FROM FRUITS'

   # var=database.fetch_all(query_colmns)
   # col_list=var.List()
   # col_list=(','.join(var))
    query = 'SELECT name,alias,varities FROM  FRUITS '\
    "WHERE name like '%"+search+"%'"
    print(query)
    var= await database.fetch_all(query)
    return var 

@app.get("/fruits/{name}",response_model=List[fruit])
async def find_fruit_name(search:str=""):
    query = 'SELECT name FROM  FRUITS '\
    "WHERE name like '%"+search+"%'"
    var= await database.fetch_all(query)
    return var

@app.get("/fruits/{name,alias}",response_model=List[fruitAlias])
async def find_fruit_name_alias(search:str=""):
    query = 'SELECT name,alias FROM FRUITS'\
    "WHERE name like '%"+search+"%'"
    var=database.fetch_all(query)
    return await var 

@app.post("/fruits",response_model=fruitlist)
async def register_fruit(user: fruitEntry):
    
    query = fruits.insert().values(
        name = user.name,
        alias = user.alias,
        varities = user.varities
        
    )

    await database.execute(query)
    return {
        
        **user.dict()
    }