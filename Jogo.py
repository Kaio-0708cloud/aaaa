def time_secreto():
    dicas = ["Time que possui cor preta", "Time brasileiro", "Campeão Mundial", "Campeão da Libertadores", "Nunca foi rebaixado", "Zico"]
    
    print("Acerte o time secreto!")
    print("OBS: Só letras minúsuculas, sem acento")

    time_certo = "flamengo"
    tentativas = 0

    while True:
        for i in dicas:
            print(i)
            time = input("Qual o time: ".lower().strip())

            if time == time_certo:
                print("PARABÉNS! SRN!")
                return 
            
            elif time == "campinense":
                print("MUDE URGENTEMENTE DE TIME! TREZE É O MAIOR DA PB!!!")
            
            elif time != time_certo:
                print("Erro dessa vez, escolha outro time!")

        tentativas +=1

time_secreto()