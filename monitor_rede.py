import tkinter as tk
import subprocess
import platform
import socket
import re

def obter_ip_local():
    """Descobre o IP local da máquina."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Tenta conectar ao DNS do Google (não envia dados de fato)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "Desconhecido"
    
def obter_ping():
    """Faz um ping para o DNS do Google (8.8.8.8) e retorna o tempo em ms."""
    host = "8.8.8.8"
    # No Windows o parâmetro é '-n', no Linux/Mac é '-c'
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    comando = ['ping', param, '1', host]

    try:
        #Roda o comando no terminal em segundo plano e  captura a saída
        saida = subprocess.check_output(comando, stderr=subprocess.STDOUT, universal_newlines=True) 
        
        #Procura o valor do tempo de resposta (ms) no texto retornado
        if platform.system().lower() == 'windows':
            resultado = re.search(r'tempo[=<](\d+)ms', saida, re.IGNORECASE)
            if not resultado:
                resultado = re.search(r'time[=<](\d+)ms', saida, re.IGNORECASE)
        else:
            resultado = re.search(r'time=([\d.]+) ms', saida)

        if resultado:
            return float(resultado.group(1))
        return None
    except subprocess.CalledProcessError:
        return None
    
def analisar_rede():
    """Analisa a rede e atualiza as informações na tela."""
    lbl_status.config(text="Analisando...", fg="black")
    root.update()

    ip = obter_ip_local()
    ping_ms = obter_ping()

    if ping_ms is None:
        texto_status = "A conexão da rede está inativa ou sem internet."
        texto_ping = "Ping: Falha"
        cor = "red"

    else:
        texto_ping = f"Ping: {ping_ms:.0f} ms"
        # Lógica de avaliação do Ping
        if ping_ms < 50:
            texto_status = "A conexão da rede está excelente"
            cor = "green"
        elif ping_ms < 150:
            texto_status = "A conexão da rede está boa"
            cor = "blue"
        else:
            texto_status = "A conexão da rede está ruim"
            cor = "orange"

     # Atualiza os textos na interface gráfica
    lbl_ip.config(text=f"IP da rede: {ip}")
    lbl_status.config(text=texto_status, fg=cor)
    lbl_ping.config(text=texto_ping)
    
 # ======================================
 # Configuração da Interface Gráfica (Tkinter)
 # ====================================== 

root = tk.Tk()
root.title("Monitor de Rede")
root.geometry("350x200")

# Elementos visuais
lbl_ip = tk.Label(root, text="IP da rede: Aguardando...", font=("Arial", 12))
lbl_ip.pack(pady=15)

lbl_status = tk.Label(root, text="IP da rede: Aguardando...", font=("Arial", 12, "bold"))
lbl_status.pack(pady=5)

lbl_ping = tk.Label(root, text="Ping: Aguardando...", font=("Arial", 12))
lbl_ping.pack(pady=10)

btn_analisar = tk.Button(root, text="Atualizar Análise", command=analisar_rede, font=("Arial", 10))
btn_analisar.pack(pady=10)

#Roda a primeira análise automaticamente ao abrir
analisar_rede()

#Inicia o loo da janela

root.mainloop()
