# Projeto 04 - Simulador de votação:
# Crie um programa que simule um sistema de votação, ele deve receber votos até
# que o usuário diga que não tem mais ninguém para votar, esse programa precisa ter
# duas funções:
# A 1° Função precisa ser chamada autoriza_voto() ela vai receber como parâmetro o
# ano de nascimento de uma pessoa que será digitado pelo usuário, retornando um
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.
# A 2° Função será a votacao(), ela vai receber dois parâmetros, autorização (que virá
# da função autoriza_voto()) e o voto que é o número que a pessoa votou.
# Se ela não puder votar, a 2° função terá que retornar “Você não pode votar”, caso o
# contrário a 2° função deve validar o número que a pessoa escolheu, ela pode
# escolher de 1 a 5 (crie 3 candidatos para a votação):
# ● 1, 2 ou 3 - Votos para os respectivos candidatos
# ● 4- Voto Nulo
# ● 5 - Voto em Branco
# Sua função votacao() tem que calcular e mostrar:
# ● O total de votos para cada candidato;
# ● O total de votos nulos;
# ● O total de votos em branco;
# ● Qual candidato venceu a votação

import os # Biblioteca utilizada para limpar o console
from time import sleep # Biblioteca utilizada para pausas (efeitos)
from tqdm import tqdm # Biblioteca utilizada para a barra de progresso
from rich import print
import pygame # Biblioteca utilizada para executar áudio
pygame.mixer.init() # Função para iniciar a aplicação que executa o áudio

def linhas(): # Função para linhas decorativas
    print(f'[blue]*'*65)

def screen_clear():
   # função de limpeza de tela
    if os.name == 'posix': # para SO MAC
        _ = os.system('clear')
    else:
        _ = os.system('cls') # Versão WIN
   

def autoriza_voto(): # Função de verificação da idade
    from datetime import date # Biblioteca para calcular a idade
    anoAtual = date.today().year # função TODAY que retorna a data de HOJE e separa o ANO '.year'
    nasc = int(input('Informe o ano de Nascimento com no formato XXXX: ')) 
    idade = anoAtual - nasc
    
    if idade < 16:
        return f'NEGADO'
    elif 16 >= idade < 18 and idade > 70:
        return f'OPCIONAL'
    else:
        return f'OBRIGATÓRIO'

def votacao(voto): # Função para votação com o menu dos candidatos e contadores
    candidato1 = candidato2 = candidato3 = nulo = branco = 0 # Contadores
    continua = ''
    while True:
        while True: # Laço para verificar se a pessoa pode votar ou não. Se NEGADO pede a data novamente.
            if autoriza_voto() == 'NEGADO':
                print( f'Você não pode votar.')
            else:
                break    
        voto = int(input('''
        [ 1 ] - GULOSITOS
        [ 2 ] - FOFURA
        [ 3 ] - ELMA CHIPS
        [ 4 ] - NULO
        [ 5 ] - BRANCO

        VOTO: 
        '''))
        
        if voto == 1:
            candidato1 += 1
        elif voto == 2:
            candidato2 += 1
        elif voto == 3:
            candidato3 += 1
        elif voto == 4:
            nulo += 1
        elif voto == 5:
            branco += 1
        elif 1 < voto > 5 :
            print('''OPÇÃO INVÁLIDA''')
        #pygame.mixer.init()
        pygame.mixer.music.load("urna_eletronica2.mp3") # carregamento do arquivo mp3
        pygame.mixer.music.play() # Após votar toca o áudio a vinheta de urna eletrônica    
        continua = input('Continuar votação ? [S/N] ').upper()
        screen_clear()
        if continua == 'N':
            break   
    print(f'[cyan]APURANDO OS VOTOS')
    for i in tqdm(range(900)):
        sleep(0.001)
    sleep(2)
    print()
    print(f''' [yellow]APURAÇÃO DE FINALIZADA
    Votos GULOSITOS: {candidato1}
    Votos FOFURA: {candidato2}
    Votos ELMA CHIPS: {candidato3}
    Votos Nulos: {nulo}
    Votos BRANCOS: {branco}
''')        
    
    if candidato2 < candidato1 > candidato3:
        return f"O salgadinho eleito foi [yellow]GULOSITOS"
    elif candidato3 < candidato2 > candidato1:
        return f'O salgadinho eleito foi [yellow]FOFURA'
    elif candidato1 < candidato3 > candidato2:
        return f'O salgadinho eleito foi [yellow]ELMA CHIPS'

       
#Programa Principal
screen_clear()
  
print(f'{"[blue]ELEIÇÕES 2021":^60}')

linhas()
print(f'{"Decida qual o salgadinho mais GOSTOSO":^60}')
linhas()

print(votacao(autoriza_voto))
