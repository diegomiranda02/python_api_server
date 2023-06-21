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
      "title": "Relatório de Gestão 2022",
      "subtitle": "SECRETARIA DE GESTÃO DE PESSOAS - COPAG",
      "tableDescription1": "Detalhamento da despesa de pessoal (ativo, inativo e pensionista), evolução dos últimos anos e justificativa para o aumento/diminuição:",
      "tableContentDescription1" : "Despesas Financeiras",
      "table1" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription2" : "Despesas com Pessoal",
      "table2" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription3" : "Receita de Vendas dos Produtos",
      "table3" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription4" : "Receita de Vendas dos Servicos",
      "table4" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription5" : "Receita de Vendas de Cursos (incluindo cursos in company)",
      "table5" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "tableContentDescription6" : "Despesas de Juros/Multas",
      "table6" : 
          [
         { "Tipologias/Execicios": "2022", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69},
         { "Tipologias/Execicios": "2021", "Vencimentos e Vantagens Fixas": 0.00,"Retribuicoes":0.00,"Gratificacoes":14030926.69,"Adicionais":14030926.69,"Indenizacoes":14030926.69,"Beneficios Assistenciais e previdenciarios":14030926.69, "Demais Despesas":14030926.69,"Despesas de Exercicios Anteriores":14030926.69,"Despesas Judiciais":14030926.69,"Totais":14030926.69}
         ],
      "observation": "Justificativa variação: as despesas de 2022 superaram as despesas de 2021 por ter sido um ano eleitoral em que são pagas horas extras, jetons extraordinários e gratificação de juízes e de procuradores auxiliares. Além disso, houve reestruturação interna do Tribunal, com a criação de novos cargos em comissão (Resolução TRE-RS n. 390/2022), que contribuíram para aumentar a despesa.",
      "table200" : 
          [
         { "CARGOS GERENCIAIS": "CJ4", "QUANTIDADE DE CARGOS GERENCIAIS": 1 ,"PERCENTUAL OCUPADO POR SERVIDORES EFETIVOS": "100,00%"},
         { "CARGOS GERENCIAIS": "CJ3", "QUANTIDADE DE CARGOS GERENCIAIS": 8 ,"PERCENTUAL OCUPADO POR SERVIDORES EFETIVOS": "100,00%"},
         { "CARGOS GERENCIAIS": "CJ2", "QUANTIDADE DE CARGOS GERENCIAIS": 34 ,"PERCENTUAL OCUPADO POR SERVIDORES EFETIVOS": "97,14% (34 efetivos e 1 comissionado)"},
         { "CARGOS GERENCIAIS": "CJ1", "QUANTIDADE DE CARGOS GERENCIAIS": 16 ,"PERCENTUAL OCUPADO POR SERVIDORES EFETIVOS": "95,00% [19 efetivos (16 gerenciais, 3, não) e 1 comissionado]"},
         { "CARGOS GERENCIAIS": "FC6", "QUANTIDADE DE CARGOS GERENCIAIS": 224 ,"PERCENTUAL OCUPADO POR SERVIDORES EFETIVOS": "97,82% (224 efetivos, 4 removidos e 1 vago)"}
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
