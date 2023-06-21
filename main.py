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

    result = {
      "title": "Relatório " + reportType + " do mês de " + str(month) + " do ano de " + str(year),
      "subtitle": "Departamento Financeiro",
      "tableDescription1": "Detalhamento das despesas financeiras, das despesas com pessoal, da receita de venda de produtos e serviços, receita de cursos e depespesas com juros e multas:",
      "tableContentDescription1" : "Despesas Financeiras",
      "table1" : 
          [
         { "Ano": "2022", "Despesa com tarifa bancária": 0.00,"Taxa de Cartão de Crédio VISA":0.00,"Taxa de Cartão de Crédio Mastercard":14030926.69,"Taxa de Cartão de Crédio ELO":14030926.69},
         { "Ano": "2021", "Despesa com tarifa bancária": 0.00,"Taxa de Cartão de Crédio VISA":14030926.69,"Taxa de Cartão de Crédio Mastercard":14030926.69,"Taxa de Cartão de Crédio ELO":14030926.69}
         ],
      "tableContentDescription2" : "Despesas com Pessoal",
      "table2" : 
          [
         { "Exercício": "2022", "Salários": 0.00,"Assistência Saúde":0.00,"Auxílio Alimentação":14030926.69,"Tributos":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Exercício": "2021", "Salários": 0.00,"Assistência Saúde":0.00,"Auxílio Alimentação":14030926.69,"Tributos":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription3" : "Receita de Vendas dos Produtos",
      "table3" : 
          [
         { "Exercício": "2022", "Produto": "Produto 1","Total":14030926.69},
         { "Exercício": "2021", "Produto": "Produto 1","Total":14030926.69}
         ],
      "tableContentDescription4" : "Receita de Vendas dos Servicos",
      "table4" : 
          [
         { "Exercício": "2022", "Serviço": "Serviço 1","Total":14030926.69},
         { "Exercício": "2021", "Serviço": "Serviço 2","Total":14030926.69}
         ],
      "tableContentDescription5" : "Receita de Vendas de Cursos (incluindo cursos in company)",
      "table5" : 
          [
         { "Exercício": "2022", "Curso": "Curso 1","Total":14030926.69},
         { "Exercício": "2021", "Curso": "Curso 2","Total":14030926.69}
         ],
      "tableContentDescription6" : "Despesas de Juros/Multas",
      "table6" : 
          [
         { "Exercício": "2022", "Juros": 0.00,"Multas":0.00,"Total":0.00},
         { "Exercício": "2021", "Juros": 0.00,"Multas":0.00,"Total":0.00}
         ],
      "observation": "Justificativa da variação: as despesas com pessoal de 2022 superaram as despesas de 2021 por ter sido um ano de mais contratação e com mais projetos, o que demandou mais horas extras, que contribuíu para aumentar a despesa.",
      "table200" : 
          [
         { "CARGO": "Diretor", "QUANTIDADE DE CARGOS": 1},
         { "CARGO": "Chefe", "QUANTIDADE DE CARGOS": 8},
         { "CARGO": "Funcionários", "QUANTIDADE DE CARGOS": 34},
         { "CARGO": "Gerentes de Projeto", "QUANTIDADE DE CARGOS": 16},
         { "CARGO": "Funcionários dos setores de Limpeza e Segurança", "QUANTIDADE DE CARGOS": 10}
         ],
    }

    return Response(content=json.dumps(result), media_type="application/json")


# Add the employee
# URL /addEmployee?employee_name='employee_name'&CPF='CPF'&RG='RG'&RG_issuance_date='RG_issuance_date'&RG_issuer='RG_issuer'
# &employee_address='employee_address'&employee_address_number='employee_address_number'&employee_address_complement='employee_address_complement'
# &employee_apartment_number='employee_apartment_number'&employee_condominium='employee_condominium'&employee_CEP='employee_CEP'
# &employee_neighborhood='employee_neighborhood'&employee_state='employee_state'&employee_salary='employee_salary'
# &employee_worload='employee_worload'&employee_hour_a_day='employee_hour_a_day'&employee_contract='employee_contract'
@app.get("/addEmployee")
async def addEmployee(employee_name: str, 
                      CPF: str, 
                      RG: str,
                      RG_issuance_date: str,
                      RG_issuer: str,
                      employee_address: str,
                      employee_address_number: str,
                      employee_address_complement: str,
                      employee_apartment_number: str,
                      employee_condominium: str,
                      employee_CEP: str,
                      employee_neighborhood: str,
                      employee_state: str,
                      employee_salary: str,
                      employee_worload: str,
                      employee_hour_a_day: str,
                      employee_contract: str):


    print("employee_name" + employee_name +
      "RG"+ RG +
      "RG_issuance_date" + RG_issuance_date +
      "RG_issuer" + RG_issuer +
      "employee_address" + employee_address +
      "employee_address_number" + employee_address_number +
      "employee_address_complement" + employee_address_complement +
      "employee_apartment_number" + employee_apartment_number +
      "employee_condominium" + employee_condominium +
      "employee_CEP" + employee_CEP +
      "employee_neighborhood" + employee_neighborhood +
      "employee_state" + employee_state +
      "employee_salary" + employee_salary +
      "employee_worload" + employee_worload +
      "employee_hour_a_day" + employee_hour_a_day +
      "employee_contract" + employee_contract)

    result = {
      "text": "Employee added",
      "employee_name": employee_name,
      "RG": RG,
      "RG_issuance_date": RG_issuance_date,
      "RG_issuer": RG_issuer,
      "employee_address": employee_address,
      "employee_address_number": employee_address_number,
      "employee_address_complement": employee_address_complement,
      "employee_apartment_number": employee_apartment_number,
      "employee_condominium": employee_condominium,
      "employee_CEP": employee_CEP,
      "employee_neighborhood": employee_neighborhood,
      "employee_state": employee_state,
      "employee_salary": employee_salary,
      "employee_worload": employee_worload,
      "employee_hour_a_day": employee_hour_a_day,
      "employee_contract": employee_contract
    }
    
    return Response(content=json.dumps(result), media_type="application/json")
