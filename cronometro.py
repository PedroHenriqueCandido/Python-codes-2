import time

def cronometro_com_pausa():
    segundos = 0
    pausado = False
    print("Cronômetro iniciado! Pressione 'p' para pausar ou 'c' para continuar.")
    
    try:
        while True:
            if not pausado:
                minutos, segundos_restantes = divmod(segundos, 60)
                tempo_formatado = f"{minutos:02}:{segundos_restantes:02}"
                print(tempo_formatado, end="\r")
                time.sleep(1)
                segundos += 1  
            
         
            comando = input("Pressione 'p' para pausar ou 'c' para continuar: ").lower()
            if comando == 'p':
                pausado = True
                print("Cronômetro pausado!")
            elif comando == 'c':
                pausado = False
                print("Cronômetro continuado!")
                
    except KeyboardInterrupt:
        print("\nCronômetro finalizado!")


cronometro_com_pausa()
