while True:
    try:
        o3=float(input("\nColocar ozonio: "))
        co=float(input("colocar monoxido de carbono: "))
        no2=float(input("colocar nitrogenio: "))
        so2=float(input("colocar enxofre: "))
        mp10=float(input("colocar particulas inalaveis: "))
        mp25=float(input("colocar particulas finas inalaveis: "))

        soma_o3 = 0
        soma_co = 0
        soma_no2 = 0
        soma_so2 = 0
        soma_mp10 = 0
        soma_mp25 = 0

        # calcula a média de cada amostra
        media_o3 = soma_o3
        media_co = soma_co
        media_no2 = soma_no2
        media_so2 = soma_so2
        media_mp10 = soma_mp10
        media_mp25 = soma_mp25


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
        
        resposta=input("gostaria de checar outras outra estatisticas S/N: ")
        if resposta.lower()!="s":
            break
    except:
        print("\npor favor colocar apenas numericos tente novamente")    


print("\nobrigado por usar este progama\n")