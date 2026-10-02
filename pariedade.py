def calcular_paridade(bits):
    """
    Recebe 8 bits e retorna o bit de paridade par.
    
    Se a quantidade de 1 for par:
        retorna 0
    
    Se a quantidade de 1 for ímpar:
        retorna 1
    """

    quantidade_uns = bits.count("1")

    if quantidade_uns % 2 == 0:
        return "0"
    else:
        return "1"



def criar_quadro(bits):
    """
    Recebe 8 bits de dados
    e adiciona o bit de paridade.
    
    Retorna 9 bits.
    """

    if len(bits) != 8:
        raise ValueError(
            "O quadro precisa possuir exatamente 8 bits de dados"
        )


    paridade = calcular_paridade(bits)

    quadro = bits + paridade

    return quadro



def verificar_quadro(quadro):
    """
    Recebe 9 bits.
    Separa dados e paridade.
    Verifica se está correto.
    """

    if len(quadro) != 9:
        return False


    dados = quadro[:8]

    paridade_recebida = quadro[8]


    paridade_calculada = calcular_paridade(dados)


    if paridade_recebida == paridade_calculada:
        return True
    else:
        return False
