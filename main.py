import os
import cx_Oracle
import shutil

try:

    dsn_tns = cx_Oracle.makedsn('Host',
                                        'port',
                                        service_name='String de conexão')
    conOracle = cx_Oracle.connect(user=r'usuario',
                                         password='senha',
                                         dsn=dsn_tns)
    curOracle = conOracle.cursor()
    print("Conectado ao BD-Oracle com sucesso! Executando query...")

    queryEanControle = curOracle.execute('''Select no banco alvo''').fetchall()

    curOracle.close()
    conOracle.close()

except:
    print('erro ao abrir o banco oracle C5')
    
for nome in os.listdir("\\Local do diretorio"):
    dados = str(nome).split(".")
    EAN = dados[0].split("_")
    for linha in queryEanControle:
        if str(linha[0]) == str(EAN[0]) and str(EAN[1]) == '26':
            for existe in os.listdir('\\Local do diretorio'):
                pluExt = str(existe).split(".")
                if str(pluExt[0]) == str(linha[1]):
                    break
            if str(pluExt[0]) != str(linha[1]):
                PLU = str(linha[1]) + ".png"
                ##os.rename("\\Local do diretorio" + nome, "\\Local do diretorio" + PLU)
                shutil.copy2("\\Local do diretorio" + nome, "\\Local do diretorio" + PLU)
                print("arquivo " + nome + " alterado para " + PLU)
        else:
            pass
