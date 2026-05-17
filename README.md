# python-port-scanner

Um scanner de portas simples e leve que verifica portas comuns em um endereço IP alvo.

## Funcionalidades

- Escaneia uma lista predefinida de portas comuns
- Saída colorida para melhor legibilidade
- Interface simples por linha de comando
- Suporte multiplataforma (Windows/Linux/macOS)

## Portas Escaneadas

O scanner verifica as seguintes portas:

| Porta | Serviço     |
|-------|-------------|
| 21    | FTP         |
| 22    | SSH         |
| 23    | Telnet      |
| 25    | SMTP        |
| 53    | DNS         |
| 80    | HTTP        |
| 111   | RPC         |
| 135   | RPC         |
| 139   | NetBIOS     |
| 443   | HTTPS       |
| 3389  | RDP         |

## Requisitos

- Python 3.x
- Apenas biblioteca padrão (sem dependências externas)

## Instalação

bash:
git clone <url-do-repositorio>
cd port-scanner

## Como Usar

Execute o script:

python portScan.py

coloque o IP desejado

## Comandos:

exit	(Sai do programa)

clear	(Limpa a tela do console)

"IP"	(Escaneia o endereço IP informado)           

## Observações:

O scanner usa timeout de 0.1 segundo por porta para resultados rápidos

Escaneia apenas as 11 portas predefinidas (não é um escaneamento de faixa completa)

Resultados mostram portas abertas com status "open" em verde

## Limitações:

Não suporta faixas de portas personalizadas

Escaneamento single-thread (verifica portas sequencialmente)

Não possui escaneamento de portas UDP.
