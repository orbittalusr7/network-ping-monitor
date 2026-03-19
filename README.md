# network-ping-monitor
# Monitor de Rede com Interface Gráfica

Este projeto é um utilitário em Python desenvolvido para monitorar a conectividade de rede em tempo real. Ele identifica o IP local da máquina e mede a latência (ping) através de uma interface gráfica amigável.

## Funcionalidades

* **Detecção de IP Local:** Identifica o endereço IP interno da máquina.
* **Teste de Latência (Ping):** Mede o tempo de resposta em milissegundos (ms) consultando o DNS do Google (`8.8.8.8`).
* **Análise Visual:** O status da conexão é classificado por cores:
    * 🟢 **Excelente:** < 50ms
    * 🔵 **Boa:** 50ms - 150ms
    * 🟠 **Ruim:** > 150ms
    * 🔴 **Falha:** Sem conexão ou erro de rede.

##  Tecnologias Utilizadas

O projeto utiliza apenas bibliotecas nativas do Python (Standard Library), garantindo leveza e portabilidade:
* `tkinter`: Para a interface gráfica (GUI).
* `subprocess` & `re`: Para execução de comandos de sistema e extração de dados via Regex.
* `socket` & `platform`: Para gestão de rede e compatibilidade entre Windows e Linux.

##  Como Funciona?

O script identifica automaticamente o sistema operacional para ajustar os parâmetros do comando `ping`. Ele utiliza um socket UDP para forçar a descoberta do IP de rede sem a necessidade de pacotes externos, tornando a ferramenta rápida e eficiente para diagnósticos rápidos de infraestrutura.

## 💻 Como Rodar

1. Certifique-se de ter o **Python 3.x** instalado.
2. Clone o repositório ou baixe o arquivo `monitor_rede.py`.
3. Execute o comando:
   ```bash
   python monitor_rede.py
