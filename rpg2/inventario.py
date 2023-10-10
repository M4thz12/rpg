
def gerar_mochila():
    
    mochila = { "Poção de Vida" : 5, 
                "Poção de Sorte" : 3 , 
                "espada" : 0,
                "poção da réplica": 0,
                "itens_diversos": [],
                "Peça de Ouro": 0
                }

    return mochila

def adicionar_item(mochila, loot):
    
    loot = {
        "espada" : 1,
        "Poção de Vida" : 2,
        "Poção de Sorte" : 1
    }

    inv_atualizado = { 
        key: mochila.get(key, 0) + loot.get(key, 0)
        for key in set(mochila | loot)
    }

    return inv_atualizado

def remover_item(mochila, item):
    if item in mochila:
        mochila[item] -= 1 
        if mochila[item] <= 0:
            mochila.pop(item)








# class Mochila:
#     def __init__(self, capacidade_maxima):
#         self.capacidade_maxima = capacidade_maxima
#         self.itens = []

#     def adicionar_item(self, item):
#         if len(self.itens) < self.capacidade_maxima:
#             self.itens.append(item)
#             print(f"{item} foi adicionado à mochila.")
#         else:
#             print("A mochila está cheia!")

#     def remover_item(self, item):
#         if item in self.itens:
#             self.itens.remove(item)
#             print(f"{item} foi removido da mochila.")
#         else:
#             print(f"{item} não está na mochila.")

#     def listar_itens(self):
#         if self.itens:
#             print("Itens na mochila:")
#             for item in self.itens:
#                 print(item)
#         else:
#             print("A mochila está vazia.")

# # Exemplo de uso
# mochila_do_jogador = Mochila(5)  # Mochila com capacidade máxima de 5 itens

# mochila_do_jogador.adicionar_item("Espada")
# mochila_do_jogador.adicionar_item("Poção de Cura")
# mochila_do_jogador.adicionar_item("Escudo")
# mochila_do_jogador.listar_itens()

# mochila_do_jogador.remover_item("Poção de Cura")
# mochila_do_jogador.listar_itens()
