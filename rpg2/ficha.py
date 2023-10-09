def gerar_personagem():
    import random
    personagem = {
        "habilidade" : (random.randint(1,6) + 6),
        "sorte" : (random.randint(1,6) + 6),
        "energia" : ((random.randint(1,6) + random.randint(1,6)) + 12)
    }
    return personagem

def ficha_formatada(personagem):
    ficha = f'Habilidade: {personagem["habilidade"]}\nEnergia: {personagem["energia"]}\nSorte: {personagem["sorte"]}'
    return ficha

