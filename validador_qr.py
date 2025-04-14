import re

# Entrada do usuário (conteúdo do QR)
conteudo_qr = input("Cole aqui o conteúdo do QR Code: ").strip()

# Padrão atualizado: aceita "/validar" OU "/lander"
padrao = r"^https:\/\/vcampustech\.com\/(validar|lander)\?id=\d+&token=([a-zA-Z0-9]+)$"

# Tokens válidos (simulando banco de dados)
tokens_validos = ["abc123xyz", "def456uvw", "gh789klm"]

def validar_qr(conteudo):
    match = re.match(padrao, conteudo)
    
    if not match:
        return "❌ QR Code inválido: formato incorreto."

    token = match.group(2)  # token agora está no grupo 2

    if token in tokens_validos:
        return "✅ QR Code válido e autenticado!"
    else:
        return "⚠️ QR Code inválido: token não reconhecido."

# Resultado
print(validar_qr(conteudo_qr))
