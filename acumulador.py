class AcumuladorBits:

    def __init__(self):
        self.bits = ""


    def adicionar_bit(self, bit):

        self.bits += str(bit)



    def obter_resultado(self):

        return self.bits



    def limpar(self):

        self.bits = ""



    def quantidade_bits(self):

        return len(self.bits)



    def possui_byte(self):

        return len(self.bits) >= 8



    def pegar_byte(self):

        byte = self.bits[:8]

        self.bits = self.bits[8:]

        return byte
