class Time():
    def __init__(self, *args, **kwargs):
        self.nome = args[0]
        self.defesa = kwargs.pop('defesa')
        self.ataque = kwargs.pop('ataque')
        self.meio = kwargs.pop('meio')
        self.overall = sum(kwargs.values())//3
        self.dic = kwargs
        self.titulos_liga = 0
        self.titulos_copa = 0
        self.pontos_totais = 0
        self.clear()
        
    def __str__(self)->str:
        return f'{self.nome}'
    def get_pontos(self)->int:
        try:
            return 3*self.vitorias + self.empates
        except:
            return 0
    def get_stats(self)->str:
        jogos = self.vitorias + self.derrotas + self.empates
        sg = self.gols_pro - self.gols_contra
        return f"{self.nome:<15} {jogos:<2}  {self.vitorias:<2}  {self.empates:<2}  {self.derrotas:<2}  {self.gols_pro:<3}  {self.gols_contra:<3}  {sg:>4}  {self.get_pontos():>2}"
    def clear(self):
        self.pontos_totais += self.get_pontos()
        self.vitorias = 0
        self.derrotas = 0
        self.empates = 0
        self.gols_pro = 0
        self.gols_contra = 0