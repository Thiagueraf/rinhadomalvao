# listas_de_nomes.py
from random import sample
lista_todos_camps = ["Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "AurelionSol", "Azir", "Bardo", "Belveth", "Blitzcrank", "Brand", "Braum", "Briar", "Caitlyn", "Camille", "Cassiopeia", "Chogath", "Corki", "Darius", "Diana", "DrMundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Ivern", "Janna", "JarvanIV", "Jax", "Jayce", "Jhin", "Jinx", "KSante", "Kaisa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Khazix", "Kindred", "Kled", "KogMaw", "Leblanc", "LeeSin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "MasterYi", "Milio", "MissFortune", "Mordekaiser", "Morgana", "Naafiri", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "RekSai", "Rell", "Renata", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "TahmKench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "TwistedFate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Velkoz", "Vex", "Vi", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "XinZhao", "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"]
def gerar_lista_5_nomes():
 
 return sample(lista_todos_camps, 5)





listas_de_nomes = {
    1: ["Corki", "Lulu", "Rumble","Teemo","Tristana","Veigar","Yuumi"],
    2: ["Fiora", "Galio", "Garen","JarvanIV","Kayle","Lucian", "Lux","Morgana","Poppy","Quinn","Shyvana","Sona","Sylas","Vayne","XinZhao"],
    3: ["Anivia","Ashe","Braum","Gnar","Gragas","Lissandra","Nunu","Olaf","Ornn","Sejuani","Trundle","Tryndamere","Udyr","Volibear"],
    4: ["Caitlyn", "Camille", "Ezreal","Heimerdinger","Jayce","Orianna","Seraphine","Vi"],
    5: ["Ahri", "Akali", "Irelia","Ivern","Jhin","Karma","Kayn","Kennen","LeeSin","Lillia","MasterYi","Wukong","Rakan","Sett","Shen","Syndra","Varus","Xayah","Yasuo","Yone","Zed"],
    6: ["Malphite", "Milio", "Neeko","Nidalee","Qiyana","Rengar","Zyra"],
    7: ["Briar", "Cassiopeia", "Darius","Draven","Katarina","Kled","Leblanc","Mordekaiser","Rell","Riven","Samira","Sion","Swain","Talon","Vladimir"],
    8: ["Elise", "Gwen", "Hecarim","Karthus","Maokai","Senna","Thresh","Vex","Viego","Yorick"],
    9: ["Akshan", "Amumu", "Azir","KSante","Naafiri","Nasus","Rammus","Renekton","Rengar","Sivir","Skarner","Taliyah","Xerath"],
    10: ["Aphelios", "AurelionSol", "Diana","Leona","Pantheon","Soraka","Taric","Zoe"],
    11: ["Belveth", "Chogath", "Kaisa","Kassadin","Khazix","KogMaw","Malzahar","RekSai","Velkoz"],
    12: ["Blitzcrank", "DrMundo", "Ekko","Janna","Jinx","Renata","Singed","Twitch","Urgot","Viktor","Warwick","Zac","Ziggs","Zeri"],
    13: ["Aatrox", "Alistar", "Annie","Bardo","Brand","Evelynn","Fiddlesticks","Ivern","Jax","Kindred","Nami","Nilah","Nocturne","Ryze","Shaco"],
    14: ["Akali", "Akshan", "Diana","Ekko","Evelynn","Fizz","Kassadin","Katarina","Khazix","Naafiri","Nocturne","Pyke","Qiyana","Rengar","Shaco","Talon","Yone","Zed"],
    15: ["Jayce", "Lux", "Velkoz", "Xerath", "Ziggs", "Anivia", "AurelionSol", "Cassiopeia", "Karthus", "Malzahar", "Rumble", "Ryze", "Swain", "Mordekaiser", "Taliyah", "Viktor", "Vladimir", "Ahri", "Annie", "Brand", "Karma", "Leblanc", "Lissandra", "Lux", "Neeko", "Orianna", "Seraphine", "Sylas", "Syndra", "TwistedFate", "Veigar", "Vex", "Zoe"],
    16: ["Briar", "Camille", "Diana", "Elise", "Hecarim", "Irelia", "JarvanIV", "LeeSin", "Olaf", "XinZhao", "Wukong", "Warwick", "Vi", "Skarner", "Renekton", "RekSai", "Pantheon", "Aatrox", "Darius", "Sett", "Shyvana", "DrMundo", "Garen", "Udyr", "Trundle", "Illaoi", "Urgot", "Mordekaiser", "Volibear", "Nasus", "Yorick"],
    17: ["Bardo", "Blitzcrank", "Neeko", "Pyke", "Ivern", "Rakan", "Jhin", "Thresh", "Morgana", "Zyra", "Janna", "Karma", "Lulu", "Milio", "Nami", "Senna", "Seraphine", "Sona", "Soraka", "Taric", "Renata", "Yuumi", "Mordekaiser"],
    18: ["Akshan", "KogMaw", "Aphelios", "Lucian", "Ashe", "MissFortune", "Caitlyn", "Samira", "Corki", "Senna", "Draven", "Sivir", "Ezreal", "Tristana", "Jhin", "Twitch", "Jinx", "Varus", "Kaisa", "Vayne", "Kalista", "Xayah", "Kindred", "Zeri"],
    19: ["Aatrox","Alistar", "Amumu","Blitzcrank","Braum", "Camile","Chogath","Darius","DrMundo","Elise","Galio","Garen","Gnar","Gragas","Hecarim","Illaoi","Irelia","JarvanIV","Jax","LeeSin","Leona","Malphite","Maokai","Nasus","Nautilus","Nunu", "Olaf", "Ornn", "Poppy", "Pyke","Rammus", "Reksai","Rell","Renekton", "Sejuani","Sett","Shen","Shyvana","Singed","Sion","Skarner","TahmKench","Taric","Thresh","Trundle","Udyr","Urgot","Vi","Vladmir","Volibear","Warwick","Yorick","Zac"],
    20: ["Aatrox", "Akali", "Belveth", "Briar", "DrMundo", "Garen", "Gnar", "Katarina", "Kennen", "Kled", "LeeSin", "Mordekaiser", "RekSai", "Renekton", "Rengar", "Riven", "Rumble", "Sett", "Shen", "Shyvana", "Tryndamere", "Viego", "Vladimir", "Yasuo", "Yone", "Zac", "Zed"],
    21:["Fizz", "Gangplank", "Graves","Illaoi","MissFortune","Nautilus","Pyke","TahmKench", "TwistedFate"],
    22:["Aatrox", "Akali", "Akshan", "Aphelios", "Ashe", "Belveth", "Briar", "Caitlyn", "Camille", "Corki", "Darius", "DrMundo", "Draven", "Ezreal", "Fiora", "Gangplank", "Garen", "Gnar", "Graves", "Gwen", "Hecarim", "Illaoi", "Irelia", "JarvanIV", "Jax", "Jayce", "Jhin", "Jinx", "KSante", "Kaisa", "Kalista", "Kayle", "Kayn", "Kennen", "Khazix", "Kindred", "Kled", "KogMaw", "LeeSin", "Lucian", "MasterYi", "MissFortune", "Naafiri", "Nasus", "Nilah", "Nocturne", "Olaf", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "RekSai", "Renekton", "Rengar", "Riven", "Samira", "Senna", "Sett", "Shaco", "Shyvana", "Sion", "Sivir", "Skarner", "Talon", "Thresh", "Tristana", "Trundle", "Tryndamere", "TwistedFate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Vi", "Viego", "Volibear", "Warwick", "Wukong", "Xayah", "XinZhao", "Yasuo", "Yone", "Yorick", "Zed", "Zeri"],
    23:["Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "AurelionSol", "Azir", "Bardo", "Blitzcrank", "Brand", "Braum", "Cassiopeia", "Chogath", "Diana", "DrMundo", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fizz", "Galio", "Gragas", "Gwen", "Heimerdinger", "Ivern", "Janna", "Jax", "Kaisa", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kennen", "Leblanc", "Leona", "Lillia", "Lissandra", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Milio", "Mordekaiser", "Morgana", "Nami", "Nautilus", "Neeko", "Nidalee", "Nunu", "Orianna", "Ornn", "Rakan", "Rammus", "Rell", "Renata", "Rumble", "Ryze", "Sejuani", "Seraphine", "Shaco", "Shen", "Shyvana", "Singed", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "TahmKench", "Taliyah", "Taric", "Teemo", "Thresh", "TwistedFate", "Twitch", "Udyr", "Varus", "Veigar", "Velkoz", "Vex", "Viktor", "Vladimir", "Volibear", "Warwick", "Xerath", "XinZhao", "Yuumi", "Zac", "Ziggs", "Zilean", "Zoe", "Zyra"],
    24:["Akshan", "Diana", "Graves", "Irelia", "Lucian", "Olaf", "Pyke", "Rengar", "Riven", "Senna", "Vayne"],
    25:["Ahri", "Akshan", "Anivia", "Aphelios", "Azir", "Brand", "Corki", "Ekko", "Gangplank", "Graves", "Gwen", "Jinx", "KogMaw","Lissandra", "Lucian", "Lux", "Malzahar", "Orianna","Qiyana" ,"Rumble", "Ryze", "Sivir", "Syndra", "Tristana", "Veigar", "Velkoz", "Viktor", "Vladimir", "Xayah", "Xerath", "Yasuo", "Yone", "Zed", "Zeri", "Ziggs", "Zilean"],
    26:["Akshan","Aphelios", "Azir", "Caitlyn", "Corki", "Diana", "Ezreal", "Gangplank", "Gnar", "Heimerdinger", "Jayce", "Kaisa", "Karma", "Karthus", "KogMaw", "Lillia", "Lux", "Nidalee", "Senna", "Seraphine", "Sona", "Syndra", "Varus", "Velkoz", "Xerath", "Yone", "Zeri", "Ziggs", "Zoe", "Zyra"],
    27:["Amumu", "Anivia", "AurelionSol", "Azir", "Bardo", "Braum", "Cassiopeia", "Corki", "Ekko", "Gragas", "Janna", "Jinx", "LeeSin", "Leona", "Nami", "Rumble", "Sejuani", "Sivir", "Sona", "Syndra", "Taliyah", "Thresh", "Tristana", "Vex", "Viego", "XinZhao", "Yuumi", "Ziggs", "Zilean"],
    28:["Aatrox", "Alistar", "Amumu", "Annie", "Ashe", "AurelionSol", "Bardo", "Blitzcrank", "Braum", "Camille", "Ekko", "Fiddlesticks", "Galio", "Gnar", "Gragas", "Hecarim", "Illaoi", "Ivern", "JarvanIV", "Kalista", "Kennen", "Kled", "Leona", "Lissandra", "Malphite", "Maokai", "Morgana", "Nami", "Nautilus", "Neeko", "Nocturne", "Nunu", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Rakan", "Rammus", "RekSai", "Rell", "Riven", "Rumble", "Sejuani", "Shen", "Shyvana", "Sion", "Sylas", "Thresh", "Urgot", "Varus", "Vi", "Wukong", "Yone", "Yorick", "Zac", "Zyra"],
    29:["Aatrox", "Ahri", "Akali", "Alistar", "Amumu", "Anivia", "Annie", "Ashe", "AurelionSol", "Azir", "Bardo", "Blitzcrank", "Brand", "Braum", "Camille", "Cassiopeia", "Chogath", "Darius", "Diana", "Draven", "Ekko", "Elise", "Evelynn", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Garen", "Gnar", "Gragas", "Hecarim", "Heimerdinger", "Irelia", "Ivern", "Janna", "JarvanIV", "Jax", "Jayce", "Kalista", "Kayn", "Kennen", "Kled", "LeeSin", "Leona", "Lissandra", "Lulu", "Malphite", "Malzahar", "Maokai", "Morgana", "Nami", "Nautilus", "Neeko", "Nocturne", "Nunu", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Rakan", "Rammus", "RekSai", "Rell", "Renekton", "Riven", "Samira", "Sejuani", "Seraphine", "Sett", "Shen", "Shyvana", "Singed", "Sion", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "TahmKench", "Taric", "Thresh", "Tristana", "Trundle", "TwistedFate", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Velkoz", "Vex", "Vi", "Viego", "Viktor", "Volibear", "Warwick", "Wukong", "Xerath", "XinZhao", "Yasuo", "Yone", "Zac", "Ziggs", "Zyra"],
    30:["Amumu", "Anivia", "Annie", "AurelionSol", "Azir", "Bardo", "Braum", "Caitlyn", "Camille", "Cassiopeia", "Chogath", "Corki", "Darius", "Diana", "DrMundo", "Evelynn", "Ezreal", "Fiora", "Fizz", "Galio", "Gnar", "Gragas", "Gwen", "Irelia", "Janna", "Jhin", "Kaisa", "Kalista", "Karma", "Karthus", "Kassadin", "Kayn", "Khazix", "KogMaw", "Lillia", "Lucian", "Lulu", "MasterYi", "Mordekaiser", "Nasus", "Nautilus", "Nidalee", "Nunu", "Pantheon", "Pyke", "Qiyana", "Quinn", "Rakan", "Rell", "Rengar", "Riven", "Rumble", "Ryze", "Senna", "Sett", "Shen", "Skarner", "Sona", "Sylas", "TahmKench", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Tryndamere", "Twitch", "Udyr", "Urgot", "Vayne", "Veigar", "Viego", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "XinZhao", "Yasuo", "Yone", "Yuumi", "Zac", "Zeri", "Zoe"],
    31:["Ahri", "Akshan", "Alistar", "Amumu", "Anivia", "Aphelios", "Ashe", "Blitzcrank", "Brand", "Braum", "Chogath", "Diana", "DrMundo", "Draven", "Ekko", "Elise", "Fiddlesticks", "Fiora", "Gangplank", "Garen", "Graves", "Hecarim", "Heimerdinger", "Illaoi", "Ivern", "Janna", "JarvanIV", "Jax", "Jayce", "Jhin", "Jinx", "Katarina", "Kayle", "Kayn", "Kindred", "Kled", "LeeSin", "Leona", "Lillia", "Lissandra", "Lucian", "Lux", "Malphite", "Malzahar", "Maokai", "MissFortune", "Mordekaiser", "Neeko", "Orianna", "Poppy", "Rammus", "RekSai", "Rell", "Rumble", "Ryze", "Samira", "Sejuani", "Seraphine", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Taliyah", "Taric", "Tristana", "Trundle", "TwistedFate", "Twitch", "Urgot", "Varus", "Velkoz", "Vex", "Vi", "Viego", "Viktor", "Volibear", "Warwick", "Xayah", "XinZhao", "Yasuo", "Yorick", "Zed", "Ziggs", "Zilean"],
    32:["Aatrox", "Akali", "Aphelios", "Ashe", "AurelionSol", "Bardo", "Blitzcrank", "Brand", "Caitlyn", "Camille", "Corki", "Darius", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fizz", "Gangplank", "Gnar", "Graves", "Hecarim", "Illaoi", "Irelia", "JarvanIV", "Jayce", "Kaisa", "Kalista", "Karma", "Kayle", "Kennen", "Khazix", "Kindred", "Leblanc", "LeeSin", "Leona", "Lux", "Maokai", "Morgana", "Nami", "Nautilus", "Nocturne", "Olaf", "Ornn", "Pantheon", "Poppy", "Pyke", "Quinn", "Renekton", "Rengar", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Sion", "Soraka", "Sylas", "Syndra", "TahmKench", "Thresh", "Tryndamere", "TwistedFate", "Varus", "Velkoz", "Vi", "Xerath", "Yone", "Yorick", "Zac", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"],
    33:["Aatrox", "Akali", "Alistar", "Amumu", "Belveth", "Blitzcrank", "Braum", "Briar", "Camille", "Chogath", "Darius", "Diana", "DrMundo", "Ekko", "Elise", "Evelynn", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Gwen", "Hecarim", "Illaoi", "Irelia", "JarvanIV", "Jax", "Jayce", "KSante", "Kassadin", "Katarina", "Kayle", "Kayn", "Khazix", "Kled", "LeeSin", "Leona", "Malphite", "Maokai", "MasterYi", "Mordekaiser", "Naafiri", "Nasus", "Nautilus", "Nidalee", "Nocturne", "Nunu", "Olaf", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Rakan", "Rammus", "RekSai", "Rell", "Renekton", "Riven", "Rumble", "Sejuani", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Skarner", "Sylas", "TahmKench", "Talon", "Taric", "Trundle", "Tryndamere", "Udyr", "Vi", "Viego", "Volibear", "Warwick", "Wukong", "XinZhao", "Yasuo", "Yone", "Yorick", "Zac", "Zed"],
    34:["Ahri", "Akshan", "Anivia", "Aphelios", "Ashe", "AurelionSol", "Azir", "Bardo", "Brand", "Caitlyn", "Cassiopeia", "Corki", "Draven", "Elise", "Ezreal", "Fiddlesticks", "Gnar", "Graves", "Heimerdinger", "Ivern", "Janna", "Jayce", "Jhin", "Jinx", "Kaisa", "Kalista", "Karma", "Karthus", "Kayle", "Kennen", "Kindred", "KogMaw", "Leblanc", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malzahar", "Milio", "MissFortune", "Morgana", "Nami", "Neeko", "Nidalee", "Nilah", "Orianna", "Quinn", "Renata", "Rengar", "Ryze", "Samira", "Senna", "Seraphine", "Sivir", "Sona", "Soraka", "Swain", "Syndra", "Taliyah", "Teemo", "Thresh", "Tristana", "TwistedFate", "Twitch", "Urgot", "Varus", "Vayne", "Veigar", "Velkoz", "Vex", "Viktor", "Vladimir", "Xayah", "Xerath", "Yuumi", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"],
    35:["Briar", "Camille", "Diana", "Hecarim", "Irelia", "JarvanIV", "LeeSin", "Olaf", "Pantheon", "RekSai", "Renekton", "Rengar", "Skarner", "Vi", "Warwick", "Wukong", "XinZhao"],
    36:["Aatrox", "Darius", "DrMundo", "Garen", "Illaoi", "Mordekaiser", "Nasus", "Sett", "Shyvana", "Trundle", "Udyr", "Urgot", "Volibear", "Yorick"],
    37:["Ahri", "Annie", "Brand", "Karma", "Leblanc", "Lissandra", "Lux", "Neeko", "Orianna", "Seraphine", "Sylas", "Syndra", "TwistedFate", "Veigar", "Vex", "Zoe"],
    38:["Azir", "Chogath", "Fiddlesticks", "Gangplank", "Gnar", "Graves", "Heimerdinger", "Kayle", "Kennen", "Nidalee", "Quinn", "Singed", "Teemo", "Zilean"],
    39:["O Outro Time escolhe seus campeões"],
    40:["Braum", "Galio", "KSante", "Poppy", "Shen", "TahmKench", "Taric"],
    41:["Aatrox", "Alistar", "Amumu", "Gragas", "Leona", "Malphite", "Maokai", "Nautilus", "Nunu", "Ornn", "Rammus", "Rell", "Sejuani", "Sion", "Zac"],
    42:["Campeões da aba TOP da Seleção de Campeão"],
    43:["Campeões da aba JUNGLE da Seleção de Campeão"],
    44:["Campeões da aba MID da Seleção de Campeão"],
    45:["Campeões da aba ADC da Seleção de Campeão"],
    46:["Campeões da aba SUP da Seleção de Campeão"],
    47:["Akali", "Akshan", "Annie", "Aphelios", "Ashe", "Braum", "Caitlyn", "Camille", "Darius", "Diana", "Draven", "Ekko", "Ezreal", "Fiora", "Gangplank", "Garen", "Gragas", "Graves", "Illaoi", "Irelia", "Janna", "JarvanIV", "Jax", "Jayce", "Jhin", "Jinx", "KSante", "Kaisa", "Kalista", "Karma", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Leblanc", "LeeSin", "Leona", "Lucian", "Lux", "MasterYi", "Milio", "MissFortune", "Morgana", "Nidalee", "Nilah", "Nunu", "Olaf", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rell", "Renata", "Riven", "Ryze", "Samira", "Sejuani", "Seraphine", "Sett", "Shen", "Singed", "Sivir", "Sona", "Swain", "Sylas", "Syndra", "Taliyah", "Talon", "Taric", "Tryndamere", "TwistedFate", "Udyr", "Urgot", "Varus", "Vayne", "Vex", "Vi", "Viego", "Viktor", "Vladimir", "XinZhao", "Yasuo", "Yone", "Yorick", "Zed", "Zeri", "Zilean"],
    48:["Aatrox", "Ahri", "Alistar", "Amumu", "Anivia", "AurelionSol", "Azir", "Bardo", "Belveth", "Blitzcrank", "Brand", "Briar", "Cassiopeia", "Chogath", "Corki", "DrMundo", "Elise", "Evelynn", "Fiddlesticks", "Fizz", "Galio", "Gnar", "Gwen", "Hecarim", "Heimerdinger", "Ivern", "Kaisa", "Kalista", "Karma", "Karthus", "Kayle", "Kayn", "Kennen", "Khazix", "Kindred", "Kled", "KogMaw", "Lillia", "Lissandra", "Lulu", "Malphite", "Malzahar", "Maokai", "Mordekaiser", "Morgana", "Naafiri", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu", "Orianna", "Ornn", "Pyke", "Qiyana", "Rakan", "Rammus", "RekSai", "Renekton", "Rengar", "Rumble", "Ryze", "Senna", "Shaco", "Shyvana", "Sion", "Skarner", "Soraka", "Swain", "Syndra", "TahmKench", "Teemo", "Thresh", "Tristana", "Trundle", "Twitch", "Veigar", "Velkoz", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Yorick", "Yuumi", "Zac", "Zed", "Ziggs", "Zoe", "Zyra"],
    49:["Aatrox", "Alistar", "Azir", "Blitzcrank", "Braum", "Chogath", "Galio", "Gragas", "Ivern", "Janna", "JarvanIV", "Jax", "KSante", "Kayn", "LeeSin", "Lulu", "Malphite", "Maokai", "Nami", "Nautilus", "Nunu", "Ornn", "Poppy", "Qiyana", "Rakan", "Rammus", "RekSai", "Sejuani", "Sett", "Shyvana", "Sion", "Syndra", "Taliyah", "Thresh", "Tristana", "Urgot", "Vi", "Volibear", "Wukong", "XinZhao", "Yasuo", "Yone", "Zac", "Ziggs", "Zyra"],
    50:["Ahri", "Akali", "Anivia", "Annie", "Ashe", "Belveth", "Briar", "Caitlyn", "Camille", "Cassiopeia", "Diana", "Elise", "Evelynn", "Fiora", "Gwen", "Illaoi", "Irelia", "Janna", "Jinx", "Kaisa", "Kalista", "Karma", "Katarina", "Kayle", "Kindred", "Leblanc", "Leona", "Lillia", "Lissandra", "Lulu", "Lux", "MissFortune", "Morgana", "Naafiri", "Nami", "Neeko", "Nidalee", "Nilah", "Orianna", "Poppy", "Qiyana", "Quinn", "RekSai", "Rell", "Renata", "Riven", "Samira", "Sejuani", "Senna", "Seraphine", "Shyvana", "Sivir", "Sona", "Soraka", "Syndra", "Taliyah", "Tristana", "Vayne", "Velkoz", "Vex", "Vi", "Xayah", "Yuumi", "Zeri","Zoe", "Zyra"],
    51:["Akshan", "Alistar", "Amumu", "Aphelios", "AurelionSol", "Azir", "Bardo", "Blitzcrank", "Brand", "Braum", "Chogath", "Corki", "Darius", "DrMundo", "Draven", "Ekko", "Ezreal", "Fiddlesticks", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Hecarim", "Heimerdinger", "Ivern", "JarvanIV", "Jax", "Jayce", "Jhin", "KSante", "Karthus", "Kassadin", "Kayn", "Kennen", "Khazix", "Kindred", "Kled", "KogMaw", "LeeSin", "Lucian", "Malphite", "Malzahar", "Maokai", "MasterYi", "Milio", "Mordekaiser", "Nasus", "Nautilus", "Nocturne", "Nunu", "Olaf", "Ornn", "Pantheon", "Pyke", "Rakan", "Rammus", "Renekton", "Rengar", "Rumble", "Ryze", "Sett", "Shaco", "Shen", "Singed", "Sion", "Skarner", "Swain", "Sylas", "TahmKench", "Talon", "Taric", "Teemo", "Thresh", "Trundle", "Tryndamere", "TwistedFate", "Twitch", "Udyr", "Urgot", "Varus", "Veigar", "Velkoz", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xerath", "XinZhao", "Yasuo", "Yone", "Yorick", "Zac", "Zed", "Ziggs", "Zilean"],
    52:gerar_lista_5_nomes,
    53:["Hecarim", "Fiddlesticks", "Nocturne", "Warwick", "Vex", "Shaco", "Urgot", "Aatrox", "Darius"],
    54:["Belveth", "Briar", "LeeSin", "Nasus", "Olaf", "Senna", "Sion", "Udyr", "Aatrox", "Aphelios", "Camille", "Fiddlesticks", "Gwen", "Hecarim", "Mordekaiser", "Morgana", "Nilah", "Kayn", "Trundle", "Viego", "Vladimir", "Warwick","Swain"],
    55:["Annie", "Azir", "Aphelios", "Bardo", "Elise", "Ekko", "Heimerdinger", "Illaoi", "Ivern", "Kalista", "Kindred", "Kled", "Lulu", "Maokai", "Malzahar", "Nunu", "Quinn", "Sejuani","Thresh", "Zyra", "Yorick"],
    56:["Akshan", "Annie", "Azir", "Blitzcrank", "Braum", "Camille", "Diana", "Ekko", "Galio", "Garen", "Ivern", "Janna", "JarvanIV", "KSante", "Kaisa", "Karma", "Kassadin", "Kled", "LeeSin", "Leona", "Lulu", "Lux", "Malphite", "Malzahar", "Milio", "Mordekaiser", "Morgana", "Nami", "Nautilus", "Nilah", "Nocturne", "Nunu", "Olaf", "Orianna", "Poppy", "Pantheon", "Rakan", "Rell", "Renata", "Riven", "Rumble", "Senna", "Seraphine", "Sett", "Shen", "Sion", "Sivir", "Skarner", "Sona", "TahmKench", "Taric", "Thresh", "Udyr", "Urgot", "Vex", "Vi", "Viktor", "Volibear", "Yasuo", "Yone", "Yuumi"],
    57:["Azir", "Nasus", "Renekton", "Xerath", "Diana", "Leona", "Pantheon", "Taric", "Zoe", "Anivia", "Ornn", "Volibear", "Kindred", "Janna", "Bardo", "AurelionSol", "Soraka","Kayle","Morgana"],
    58:["Yone", "Yasuo", "Viego", "Tryndamere", "Shen", "Riven", "Master Yi", "Garen", "Fiora", "Ekko", "Aatrox", "Samira", "Leona"]




}

nomes_por_numero = {
1: "Bandopolis",
2: "Demacia",
3: "Freljord",
4: "Piltover",
5: "Ionia",
6: "Ixtal",
7: "Noxus",
8: "Ilha Das Sombras",
9: "Shurima",
10:"Targon",
11:"Vazio",
12: "Zaun",
13:"Sem Região",
14:"Assasino",
15:"Maguinhos",
16:"Lutador",
17:"Controlador",
18:"Atirador",
19:"Tank",
20: "Os sem mana",
21:"Águas de Sentina",
22:"AD",
23:"AP",
24:"Sentinelas da Luz",
25:"Waveclear",
26:"Poke",
27:"Disengage",
28:"Hard Engage",
29:"Hard CC",
30:"Late Game",
31:"Mid Game",
32:"Early Game",
33:"Melee",
34:"Range",
35:"Diver(Mergulhador)",
36:"Juggernaut",
37:"Burst",
38:"Especialistas",
39:"Time do Adversário",
40:"Guardiões",
41:"Vanguarda",
42:"Tops",
43:"Junglers",
44:"Mids",
45:"Adcs",
46:"Sups",
47:"Humanos",
48:"Não Humanos",
49:"Joga pro alto",
50:"Feminino",
51:"Masculino",
52:"Time Aleatório",
53:"Boo(Time dos sustos)",
54: "Ladrões de vida",
55: "Sempre ao seu lado",
56:"Campões que tem Shield",
57:"Seres Divinos/Celestiais",
58:"Espadachim"
}


nomes_por_numero_lab = {
1: "Personagens que eu amasso de Poppy",
2: "Os personagens favoritos do Thiaguera",
3: "Aqui é bodybuilder",
4:"Personagens que tem problema de cabeça",
5:"Um Mix do mundo (Um campeão aleatório de cada região)",
6:"Campeões que eu chamaria pra um churrasco"
}

listas_de_nomes_lab = {
    1: ["Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "AurelionSol", "Azir", "Bardo", "Belveth", "Blitzcrank", "Brand", "Braum", "Briar", "Caitlyn", "Camille", "Cassiopeia", "Chogath", "Corki", "Darius", "Diana", "DrMundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Illaoi", "Irelia", "Ivern", "Janna", "JarvanIV", "Jax", "Jayce", "Jhin", "Jinx", "KSante", "Kaisa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Khazix", "Kindred", "Kled", "KogMaw", "Leblanc", "LeeSin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "MasterYi", "Milio", "MissFortune", "Mordekaiser", "Morgana", "Naafiri", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nilah", "Nocturne", "Nunu", "Olaf", "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "RekSai", "Rell", "Renata", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "TahmKench", "Taliyah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "TwistedFate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Velkoz", "Vex", "Vi", "Viego", "Viktor", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "XinZhao", "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"],
    2:["Poppy","Ornn","Warwick","Vi","Shen","Kayn","Karma","Ezreal","Braum","Ekko"],
    3:["Aatrox","Alistar","Braum","DrMundo","Gangplank","Darius","Garen","Illaoi","Ksante","LeeSin","Olaf","Pantheon","Ornn","Sett","Sion","Taric","Tryndamere","Udyr","Zac"],
    4:["Aatrox","Amumu","Annie","Teemo","Aphelios","Draven","Hwei","Jinx","Kayn","Kled","Lulu","Poppy","Rumble","Shaco","Sylas","Veigar","Vex","Ziggs","Zoe"],
    5:["Gangplank","Tristana","Lux","Braum","Elise","Irelia","Neeko","Darius","Kaisa","Urgot","AurelionSol","Azir","Vi"],
    6:["Brand","Braum","Corki","Ekko","Fizz","Gangplank","Kled","Gnar","Gragas","Irelia","Jinx","Karma","Kennen","Kled","MasterYi","Nunu","Ornn","Poppy","Rammus","Rumble","Shen","Taliyah","Teemo","Vi",]
}
