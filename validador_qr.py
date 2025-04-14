import re

# Simula o conteúdo do QR Code (ex: lido por scanner ou câmera)
conteudo_qr = input("Cole aqui o conteúdo do QR Code: ").strip()

# Padrão esperado da URL no QR
padrao = r"^https:\/\/vcampustech\.com\/validar\?id=\d+&token=[a-zA-Z0-9]+$"

# Lista de tokens válidos (simulando uma base de dados)
tokens_validos = ["abc123xyz", "def456uvw", "gh789klm"]

def validar_qr(conteudo):
    if not re.match(padrao, conteudo):
        return "QR Code inválido: formato incorreto."

    token = conteudo.split("token=")[-1]
    
    if token in tokens_validos:
        return "QR Code válido e autenticado!"
    else:
        return "QR Code inválido: token não reconhecido."

# Executa a função
print(validar_qr(conteudo_qr))
