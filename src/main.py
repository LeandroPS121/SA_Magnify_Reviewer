import openai
import os
from dotenv import load_dotenv
from src.functions import formatar_resultados, processar_emails, salvar_resultados

# Carregar variáveis de ambiente
load_dotenv()

# Obter a chave da API do ambiente
api_key = os.environ.get("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("A chave da API do OpenAI não foi encontrada nas variáveis de ambiente.")
openai.api_key = api_key

def main():
    arquivo_emails = 'emails.txt'
    resultados = processar_emails(arquivo_emails)
    resultados_formatados = formatar_resultados(resultados)
    salvar_resultados(arquivo_resultados, resultados_formatados)
    
    upload = 'upload'
    os.makedirs(upload)
    
    arquivo_resultados = os.path.join(upload, 'resultados.csv')