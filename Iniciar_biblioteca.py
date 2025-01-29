# Aquí se agregan a los pokemons
from Contador_letras import contar_letras
from Pokemon import Pokemon
from Biblioteca_pokemon import Biblioteca

# lista: https://pokemon.fandom.com/es/wiki/Lista_de_Pok%C3%A9mon_seg%C3%BAn_la_Pok%C3%A9dex_de_Kanto
biblioteca = Biblioteca()

bulbasaur = Pokemon("bulbasaur", contar_letras("bulbasaur"), "planta/veneno", 0, 0, 1)
biblioteca.agregar_pokemon(bulbasaur)

ivysaur = Pokemon("ivysaur", contar_letras("ivysaur"), "planta/veneno", 0, 0, 2)
biblioteca.agregar_pokemon(ivysaur)

venusaur = Pokemon("venusaur", contar_letras("venusaur"), "planta/veneno", 0, 0, 3)
biblioteca.agregar_pokemon(venusaur)

charmander = Pokemon("charmander", contar_letras("charmander"), "fuego", 0, 0, 4)
biblioteca.agregar_pokemon(charmander)

charmeleon = Pokemon("charmeleon", contar_letras("charmeleon"), "fuego", 0, 0, 5)
biblioteca.agregar_pokemon(charmeleon)

charizard = Pokemon("charizard", contar_letras("charizard"), "fuego/volador", 0, 0, 6)
biblioteca.agregar_pokemon(charizard)

squirtle = Pokemon("squirtle", contar_letras("squirtle"), "agua", 0, 0, 7)
biblioteca.agregar_pokemon(squirtle)

wartortle = Pokemon("wartortle", contar_letras("wartortle", "agua"), 0, 0, 8)
biblioteca.agregar_pokemon(wartortle)

blastoise = Pokemon("blastoise", contar_letras("blastoise"), "agua", 0, 0, 9)
biblioteca.agregar_pokemon(blastoise)

caterpie = Pokemon("caterpie", contar_letras("caterpie"), "bicho", 0, 0, 10)
biblioteca.agregar_pokemon(caterpie)

metapod = Pokemon("metapod", contar_letras("metapod"), "bicho", 0, 0, 11)
biblioteca.agregar_pokemon(metapod)

butterfree = Pokemon("butterfree", contar_letras("butterfree"), "bicho/volador", 0, 0, 12)
biblioteca.agregar_pokemon(butterfree)

weedle = Pokemon("weedle", contar_letras("weedle"), "bicho/veneno", 0, 0, 13)
biblioteca.agregar_pokemon(weedle)

kakuna = Pokemon("kakuna", contar_letras("kakuna"), "bicho/veneno", 0, 0, 14)
biblioteca.agregar_pokemon(kakuna)

beedril = Pokemon("beedril", contar_letras("beedril", "bicho/veneno"), 0, 0, 15)
biblioteca.agregar_pokemon(beedril)

pidgey = Pokemon("pidgey", contar_letras("pidgey"), "normal/volador", 0, 0, 16)
biblioteca.agregar_pokemon(pidgey)

pidgeotto = Pokemon("pidgeotto", contar_letras("pidgeotto"), "normal/volador", 0, 0, 17)
biblioteca.agregar_pokemon(pidgeotto)

pidgeot = Pokemon("pidgeot", contar_letras("pidgeot"), "normal/volador", 0, 0, 18)
biblioteca.agregar_pokemon(pidgeot)

rattata = Pokemon("rattata", contar_letras("rattata"), "normal", 0, 0, 19)
biblioteca.agregar_pokemon(rattata)

raticate = Pokemon("raticate", contar_letras("raticate"), "normal", 0, 0, 20)
biblioteca.agregar_pokemon(raticate)

spearow = Pokemon("spearow", contar_letras("spearow"), "normal/volador", 0, 0, 21)
biblioteca.agregar_pokemon(spearow)

fearow = Pokemon("fearow", contar_letras("fearow"), "normal/volador", 0, 0, 22)
biblioteca.agregar_pokemon(fearow)

ekans = Pokemon("ekans", contar_letras("ekans"), "veneno", 0, 0, 23)
biblioteca.agregar_pokemon(ekans)

arbok = Pokemon("arbok", contar_letras("arbok"), "veneno", 0, 0, 24)
biblioteca.agregar_pokemon(arbok)

pikachu = Pokemon("pikachu", contar_letras("pikachu"), "eléctrico", 0, 0, 25)
biblioteca.agregar_pokemon(pikachu)

raichu = Pokemon("raichu", contar_letras("raichu"), "eléctrico", 0, 0, 26)
biblioteca.agregar_pokemon(raichu)

sandshrew = Pokemon("sandshrew", contar_letras("sandshrew"), "tierra", 0, 0, 27)
biblioteca.agregar_pokemon(sandshrew)

sandslash = Pokemon("sandslash", contar_letras("sandslash"), "tierra", 0, 0, 28)
biblioteca.agregar_pokemon(sandslash)

nidoran = Pokemon("nidoran", contar_letras("nidoran"), "veneno", 0, 0, 29)
biblioteca.agregar_pokemon(nidoran)

nidorina tierra

nidoqueen veneno/tierra

nidoran tierra
nidorino tierra
nidoking veneno/tierra
