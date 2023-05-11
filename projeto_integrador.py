import mysql.connector

# Cria uma conexão com o banco de dados
conn = mysql.connector.connect(
    host="host",
    user="usuario",
    password="senha",
    database="banco_de_dados"
)

#executar comandos no SQL
cursor = conn.cursor()

#adicionar uma amostra
def adicionar_amostra():

    certo = 1
    while certo == 1:
        try:
            o3 = float(input("digite o valor de O3 da amostra: "))
            co = float(input("digite o valor de CO da amostra: "))
            no2 = float(input("digite o valor de NO2 da amostra: "))
            so2 = float(input("digite o valor de SO2 da amostra: "))
            mp10 = float(input("digite o valor de MP10 da amostra: "))
            mp25 = float(input("digite o valor de MP25 da amostra: "))
            sql = "INSERT INTO amostras (o3, co, no2, so2, mp10, mp25) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (o3, co, no2, so2, mp10, mp25)
            cursor.execute(sql, values)
            conn.commit()
            print("\nAmostra adicionada com sucesso!")
            certo = 0
        except:
            print("\ncolocar apenas numericos\n")

#excluir uma amostra
def excluir_amostra():
    certo = 1
    while certo == 1:
        try:
            id = int(input("digite o ID da amostra que deseja excluir: "))
            sql = "DELETE FROM amostras WHERE id = %s"
            values = (id,)
            cursor.execute(sql, values)
            conn.commit()
            print("\namostra excluida com sucesso")
            certo = 0
        except:
            print("\ncoloque um id valido\n")

#alterar uma amostra
def alterar_amostra():
    certo = 1
    while certo == 1:
        try:
            id = int(input("digite o ID da amostra que deseja alterar: "))
            o3 = float(input("digite o novo valor de O3 da amostra: "))
            co = float(input("digite o novo valor de CO da amostra: "))
            no2 = float(input("digite o novo valor de NO2 da amostra: "))
            so2 = float(input("digite o novo valor de SO2 da amostra: "))
            mp10 = float(input("digite o novo valor de MP10 da amostra: "))
            mp25 = float(input("digite o novo valor de MP25 da amostra: "))
            sql = "UPDATE amostras SET o3 = %s, co = %s, no2 = %s, so2 = %s, mp10 = %s, mp25 = %s WHERE id = %s"
            values = (o3, co, no2, so2, mp10, mp25, id)
            cursor.execute(sql, values)
            conn.commit()
            print("\namostra alterada com sucesso")
            certo = 0
        except:
            print("\ncolocar apenas numericos\n")

#mostrar todas as amostras
def mostrar_amostras():
    cursor.execute("SELECT * FROM amostras")
    result = cursor.fetchall()
    for row in result:
        print("ID:", row[0], "\nO3:", row[1], "\nCO:", row[2], "\nNO2:", row[3], "\nSO2:", row[4], "\nMP10:", row[5], "\nMP25:", row[6], "\n------------")

# testar as amostras
def teste_amostra():

    cursor.execute(f"SELECT o3, co, no2, so2, mp10, mp25 FROM amostras")

    soma_o3 = 0
    soma_co = 0
    soma_no2 = 0
    soma_so2 = 0
    soma_mp10 = 0
    soma_mp25 = 0

    num_amostras = 0

    for (o3, co, no2, so2, mp10, mp25) in cursor:
        soma_o3 += o3
        soma_co += co
        soma_no2 += no2
        soma_so2 += so2
        soma_mp10 += mp10
        soma_mp25 += mp25
        num_amostras += 1

    media_o3 = soma_o3 / num_amostras
    media_co = soma_co / num_amostras
    media_no2 = soma_no2 / num_amostras
    media_so2 = soma_so2 / num_amostras
    media_mp10 = soma_mp10 / num_amostras
    media_mp25 = soma_mp25 / num_amostras



    if media_o3 < 0 or media_co < 0 or media_no2 < 0 or media_so2 < 0 or media_mp10 < 0 or media_mp25 < 0:
        qualidade_do_ar = "Por favor colocar apenas números positivos."
        efeito_saude = ""
    elif media_o3 <= 100 and media_co <= 9 and media_no2 <= 200 and media_so2 <= 20 and media_mp10 <= 50 and media_mp25 <= 25:
        qualidade_do_ar = "A qualidade do ar está boa."
        efeito_saude = ""
    elif media_o3 <= 130 and media_co <= 11 and media_no2 <= 240 and smedia_so2o2 <= 40 and media_mp10 <= 100 and media_mp25 <= 50:
        qualidade_do_ar = "A qualidade do ar está moderada."
        efeito_saude = "Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço. A população, em geral, não é afetada."
    elif media_o3 <= 160 and media_co <= 13 and media_no2 <= 320 and media_so2 <= 365 and media_mp10 <= 150 and media_mp25 <= 75:
        qualidade_do_ar = "A qualidade do ar está ruim."
        efeito_saude = "Toda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde."
    elif media_o3 <= 200 and media_co <= 15 and media_no2 <= 1130 and media_so2 <= 800 and media_mp10 <= 250 and media_mp25 <= 125:
        qualidade_do_ar = "A qualidade do ar está muito ruim."
        efeito_saude = "Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas)"
    else:
        qualidade_do_ar = "A qualidade do ar está péssima."
        efeito_saude = "Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis"

    print(f"{qualidade_do_ar}\n{efeito_saude}")


#menu
while True:
    print("\n\nescolha uma opcao:")
    print("1: adicionar amostra")
    print("2: excluir amostra")
    print("3: alterar amostra")
    print("4: mostrar todas as amostras")
    print("5: testar amostras")
    print("6: sair")
    opcao = input(">")
    if opcao == "1":
        adicionar_amostra()
    elif opcao == "2":
        excluir_amostra()
    elif opcao == "3":
        alterar_amostra()
    elif opcao == "4":
        mostrar_amostras()
    elif opcao == "5":
        teste_amostra()
    elif opcao == "6":
        break
    else:
        print("escolha uma das opcoes abaixo") 