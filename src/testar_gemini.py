import os
from dotenv import load_dotenv
from google import genai

# 1. Ativa a leitura do arquivo .env que você criou na raiz
load_dotenv()

def testar_conexao():
    # 2. Busca a chave que salvamos lá dentro
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("❌ Erro: Não encontrei a variável GEMINI_API_KEY. Verifique se o arquivo .env está na raiz.")
        return

    print("🧙‍♂️ Conectando à API do Google... Aguarde.")
    
    try:
        # 3. Inicializa o cliente oficial da API
        client = genai.Client(api_key=api_key)
        
        # 4. Envia uma mensagem de teste usando o modelo gratuito e rápido
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents='Olá! Se você estiver me ouvindo, responda com: Diga amigo e entre!'
        )
        
        # 5. Mostra a resposta na tela
        print("\n✨ Resposta do Gemini:")
        print(response.text)
        print("\n✅ Conexão realizada com sucesso! A chave está funcionando perfeitamente.")
        
    except Exception as e:
        print(f"\n❌ Algo deu errado na invocação: {e}")

if __name__ == "__main__":
    testar_conexao()