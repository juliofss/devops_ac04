class Media():
    def media_ar(self, lista_num):
        res = 0
        qtd_num = len(lista_num)
        for i in lista_num:
            res += i
        return res / qtd_num