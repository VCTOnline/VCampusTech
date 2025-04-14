# VCampusTech - Validador de QR Code

Este projeto é um exemplo simples de como validar QR Codes com Python.

## Como funciona?

O QR Code contém uma URL no formato: "https://vcampustech.com/validar?id=123&token=abc123xyz"

O script valida:

- Se a URL está bem formatada.
- Se o token dentro da URL é reconhecido (como se fosse um token de autenticação).

## Como usar

1. Execute o script:

```bash
python validador_qr.py

Cole o conteúdo do QR Code quando for solicitado.