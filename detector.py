import sounddevice as sd
import numpy as np
import time

from config import (
    TAXA_AMOSTRAGEM,
    TAMANHO_BLOCO,
    THRESHOLD,
    DEBOUNCE_MS,
    JANELA_BIT_MS
)

from acumulador import AcumuladorBits

from paridade import criar_quadro, verificar_quadro

ultima_batida = 0

batidas = []

acumulador = AcumuladorBits()


def detectar_volume(indata):

    volume = np.linalg.norm(indata)

    return volume



def callback(indata, frames, tempo, status):

    global ultima_batida


    volume = detectar_volume(indata)


    agora = time.time() * 1000


    if volume > THRESHOLD:


        if agora - ultima_batida > DEBOUNCE_MS:

            print("BATIDA DETECTADA")
            
            batidas.append(agora)

            ultima_batida = agora



def iniciar_detector():

    print("Ouvindo microfone...")
    print("Reproduza as batidas")


    with sd.InputStream(
        channels=1,
        samplerate=TAXA_AMOSTRAGEM,
        blocksize=TAMANHO_BLOCO,
        callback=callback
    ):

        while True:

            processar_batidas()



def processar_batidas():

    global batidas


    if len(batidas) == 0:
        return


    agora = time.time() * 1000


    primeira = batidas[0]


    if agora - primeira > JANELA_BIT_MS:


        quantidade = len(batidas)


        if quantidade == 1:

            acumulador.adicionar_bit(0)
            print("BIT RECEBIDO: 0")


        elif quantidade == 2:

            acumulador.adicionar_bit(1)
            print("BIT RECEBIDO: 1")


        else:

            print("Erro: quantidade inválida de batidas")


        # Verifica se acumulou 8 bits
        if acumulador.possui_byte():

            dados = acumulador.pegar_byte()

            quadro = criar_quadro(dados)

            print("Quadro criado:")
            print(quadro)

            if verificar_quadro(quadro):

                print("Status: TRANSMISSÃO OK")

            else:

                print("Status: FALHA DE TRANSMISSÃO")


        batidas = []


        print("Sequência recebida:")
        print(acumulador.obter_resultado())
