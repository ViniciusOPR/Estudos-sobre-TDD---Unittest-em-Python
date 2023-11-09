"""
1 - Receber um número inteiro
2 - Saber se o número é multiplo de 3 e 5:
    Chocolate com Amendoim
3 - Saber se o número NÃO é multiplo de 3 e 5:
    Passa fome
4 - Saber se o número é multiplo somente de 3:
    Chocolate
5 - Saber se o número é multiplo somente de 5:
    Amendoim
"""

def chocolate_com_amendoim(n):
    assert isinstance(n, int), 'n deve ser int'

    if n % 3 == 0 and n % 5 == 0:
        return 'Chocolate com Amendoim'
    
    if n % 3 == 0:
        return 'Chocolate'
    
    if n % 5 == 0:
        return 'Amendoim'
    
    return 'Passar fome'