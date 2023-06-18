# fastapi libraries
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi import Response
from fastapi.middleware.cors import CORSMiddleware

import json

# Instantiate the API
app = FastAPI()

# Decide who can access te API
origins = [
    "http://localhost",
    "http://localhost:8501"
]

# Insert the access permissions in the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check if the API is Alive
@app.get("/", response_class=PlainTextResponse)
async def root():
    return "API is Alive"
  
# Return the report selected
@app.get("/report")
async def generateReport(reportType: str, month: str, year: str):

    print('Report Type: ' + reportType + ' Month: ' + month + ' Year: ' + year)

    x = {
      "text": "A ficha funcional é o documento eletrônico que demonstra todas as ocorrências funcionais já registradas: investidura, movimentação e vacância de cargos e funções, averbação de tempo de serviço, auxílios, benefícios, dependentes, descontos, faltas, folgas e licenças, gratificações, substituições e vantagens pessoais."
    }
    return Response(content=json.dumps(x), media_type="application/json")
