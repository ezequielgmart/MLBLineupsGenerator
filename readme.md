# Tipos de bateadores | Caracteristicas		
Contact hitter      | Contact | baserunning_ability | Vision | Discipline |
Fundamental         | Contact |  Vision |  Clutch | Discipline |
PowerHouse          | power   |  Clutch |  Contact | Vision |
Todoterreno         | Contact |  Power  |  Speed | Clutch |

# Como debe de estar organizada una alineacion
1	Contact hitter Rapido
2	Contact hitter Fundamental
3	Todoterreno
4	PowerHouse
5	PowerHouse
6	Todoterreno
7	Fundamental
8	Fundamental
9	Contact hitter

# Como funcionara: 
Cada jugador tendra 4 caracteristicas principales que seran el tipo de bateador. El tipo dominante sera el tipo que defnie al jugador. 
1. Contact hitter:  toma en cuenta el contacto, baserruning y la vision. Carateristicas que suman a la hora de embasarse.
2. Fundamental: el contacto, Vision, clutch y disciplina. Carateristicas que pueden conllevar a un jugador tenga buenas apariciones en el plato y sea capaz de dar un buen rendimiento en situaciones esenciales del juego
3. PowerHouse: Poder, clutch y contacto en mayor medida, en menor medida la disciplina. Las caracteristicas del jugador que tiene que limpiar las bases. 
4. Todoterreno: el jugador ofensivo equilibrado que es bueno en varias caracteristicas. Toma en cuenta el contacto, poder, speed y clutch

# Formulas
Cada uno de los arquetipo arriba mencionados se haran dandole una puntuacion de la siguiente manera: 
atributo / 100. Luego tomar el procentaje y multiplicarlo por una puntuacion que debe de tener por cada uno de los atributos que componen el arquetipo dependiendo de que tan importante sea ese atributo para el arquetipo. 

(atributo o avg / 100) * peso o puntuacion de dicho atributo en base a la puntuacion total del arquetipo

<!-- 1. Contact hitter = ((avg contact / 100) * 45) + ((baserunning ability / 100) * 30) + ((vision / 100) * 15) + ((discipline / 100) * 5) -->

1. Contact hitter = ((contact_ability / 100) * 60) + ((baserunning ability / 100) * 30) + ((batting_ability / 100) * 10)


2. Fundamental = ((avg contact / 100) * 20) + ((vision / 100) * 30) + ((clutch / 100) * 25) + ((discipline / 100) * 25)

3. PowerHouse = ((avg Power / 100) * 55) + ((clutch / 100) * 25) + ((avg contact / 100) * 15) + ((vision / 100) * 5)

4. TodoTerreno = ((contact_ability / 100) * 25) + ((power_ability / 100) * 25) + ((baserunning ability / 100) * 25) + ((clutch / 100) * 25)





