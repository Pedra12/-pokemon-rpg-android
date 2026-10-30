#!/usr/bin/env python3
"""Apply the first safe Brazilian Portuguese and release-mode overlay to Guardian Monsters."""
from pathlib import Path
import shutil

root = Path("GuardianMonsters/GuardianMonsters")
constant = root / "core/src/de/limbusdev/guardianmonsters/Constant.java"
text = constant.read_text(encoding="utf-8")
text = text.replace("boolean DEBUGGING_ON = true;", "boolean DEBUGGING_ON = false;")
constant.write_text(text, encoding="utf-8")

strings = root / "android/res/values/strings.xml"
text = strings.read_text(encoding="utf-8").replace(
    "<string name=\"app_name\">GuardianMonsters</string>",
    "<string name=\"app_name\">Crônicas de Arvandor</string>"
)
strings.write_text(text, encoding="utf-8")

locale_dir = root / "android/assets/l18n"
translations = {
    "general": {
        "game": "Crônicas de Arvandor", "yes": "Sim", "no": "Não",
        "apply": "Aplicar", "next": "Próximo", "metamorphosis": "Metamorfose",
        "monster_metamorphs": "{0} começou sua metamorfose!",
        "monster_metamorph_complete": "{0} se transformou em {1}",
        "stat_inv_data_sheet": "Ficha da criatura",
        "main_menu_touch_start": "Toque para começar",
        "main_menu_start_new": "Novo jogo", "main_menu_load_saved": "Continuar",
        "main_menu_credits": "Créditos", "hud_menu": "Menu", "hud_quit": "Sair",
        "hud_save": "Salvar", "hud_battle": "Batalha", "hud_team": "Equipe",
        "sign_2_1_title": "Círculo de Cura",
        "sign_3_1_title": "Vila Timsey",
        "sign_3_1_text": "Bem-vindo à nossa pequena vila.",
    },
    "battle": {
        "suff_severe": "sofreu dano grave:",
        "suff_normal": "sofreu dano",
        "suff_less": "sofreu pouco dano:",
        "suff_healed": "foi curado",
        "suff_defense": "está se defendendo.",
        "batt_prepare": "Prepare sua habilidade.",
        "battle_game_over": "Fim de jogo",
        "battle_you_won": "Você venceu!",
        "batt_attack": "Atacar", "batt_defeated": "foi derrotado",
        "battle_message_ban_trial": "Você oferece {1} a {0}.",
        "battle_message_ban_failure": "{0} recusou sua oferta.",
        "battle_message_ban_success": "Você provou seu valor. {0} se juntou a você.",
        "batt_sleeping": "está dormindo", "batt_healthy": "está saudável",
        "batt_poisoned": "está envenenado", "batt_petrified": "está petrificado",
        "level_up": "{0} alcançou um novo nível!", "results": "Resultados",
        "battle_choose_area": "escolha a área",
    },
    "inventory": {
        "reassurance": "Deseja continuar?",
        "reassurance-throwaway": "Descartar {0}?",
        "learn": "Aprender", "hint": "Dica:",
        "sphere_full": "A esfera está cheia. Este item não pode ser usado.",
        "in_battle_item": "Mochila", "body": "Corpo", "hands": "Mãos",
        "head": "Cabeça", "feet": "Pés",
        "equip-body": "Armadura", "equip-hands": "Arma",
        "equip-head": "Proteção para cabeça", "equip-feet": "Calçados",
        "tent": "Barraca", "tent-description": "Recupera a vida e a energia de toda a equipe.",
        "angel-tear": "Lágrima Angelical",
        "antivenom": "Antídoto", "guardian-crystal": "Cristal",
        "potion-black": "Poção Negra", "potion-blue": "Poção Azul",
        "potion-red": "Poção Vermelha", "bread": "Pão", "milk": "Leite",
    },
    "elements": {
        "element_earth": "Terra", "element_water": "Água",
        "element_fire": "Fogo", "element_air": "Ar",
        "element_frost": "Gelo", "element_mountain": "Montanha",
        "element_forest": "Floresta", "element_arthropoda": "Artrópode",
        "element_demon": "Demônio", "element_lindworm": "Serpente",
        "element_spirit": "Espírito", "element_lightning": "Raio",
        "element_none": "Nenhum",
    },
    "attacks": {
        "attNone1_selfdef": "Defender", "attNone1_selfdef_desc": "Assume uma postura defensiva.",
        "attNone2_kick": "Chute", "attNone3_tooth": "Mordida",
        "attNone4_punch": "Soco", "attNone5_slap": "Tapa",
        "attNone6_triphazard": "Desequilíbrio", "attNone7_shield": "Escudo",
        "attNone8_sana": "Cura", "attNone9_somnum": "Sono",
        "attNone10_venenum": "Veneno",
        "attFire1_embers": "Brasas", "attFire2_fire": "Fogo",
        "attFire3_flame": "Chama", "attFire4_blaze": "Labareda",
        "attEarth1_dirt": "Terra", "attEarth2_mud": "Lama",
        "attEarth3_stones": "Pedras", "attEarth4_landslide": "Deslizamento",
        "attWater1_sprinkle": "Borrifo", "attWater2_shower": "Chuva",
        "attWater3_splash": "Jato d'água", "attWater4_waterjet": "Hidro Jato",
    },
}
for bundle, values in translations.items():
    source = locale_dir / f"{bundle}.properties"
    target = locale_dir / f"{bundle}_pt_BR.properties"
    lines = source.read_text(encoding="utf-8").splitlines()
    existing = {line.split("=", 1)[0] for line in lines if "=" in line and not line.lstrip().startswith("#")}
    with target.open("w", encoding="utf-8") as out:
        for line in lines:
            if "=" in line and not line.lstrip().startswith("#"):
                key = line.split("=", 1)[0].strip()
                if key in values:
                    line = f"{key}={values[key]}"
            out.write(line + "\n")

print("Overlay aplicado: modo normal, nome localizado e primeiros textos pt-BR.")


# Narrative and encyclopedia localization for every map bundled with the base game.
supplemental = {
    "general": {
        "person_3_1": "Um dia vou conseguir um barco e navegar por este planeta tão bonito.",
        "person_3_2": "Algo está se aproximando. Ainda não está claro o bastante para saber o que é.",
        "person_4_1": "Estou tão nervoso que não consigo ficar parado.",
        "person_5_1": "Papai passa o dia inteiro indo de um lado para o outro.",
        "sign_2_1_title": "Círculo de Cura",
        "sign_2_1_text": "Há centenas de anos, pessoas vêm a este lugar antigo em busca de cura. É possível sentir uma presença acolhedora por aqui.",
        "sign_3_1_title": "Vila Timsey",
        "sign_3_1_text": "Boas-vindas à nossa pequena vila.",
        "sign_3_2_title": "Família Eckdon",
        "sign_3_2_text": "Entre, por favor. Todos são bem-vindos.",
        "sign_3_3_title": "Vila Timsey",
        "sign_3_3_text": "Oeste: Ponte do Canal de Timsey, 1 km.",
        "sign_4_1_title": "Forno",
        "sign_4_1_text": "O fogo está quentinho e é muito agradável.",
        "sign_4_2_title": "Estante",
        "sign_4_2_text": "Muitos livros interessantes sobre o mundo antigo.",
        "hud_menu": "Menu", "hud_quit": "Sair", "hud_save": "Salvar",
        "hud_battle": "Batalha", "hud_team": "Equipe",
    },
    "battle": {
        "suff_severe": "sofreu dano grave:",
        "suff_normal": "sofreu dano:",
        "suff_less": "sofreu pouco dano:",
        "suff_healed": "foi curado",
        "suff_defense": "está se defendendo.",
        "batt_prepare": "Prepare sua habilidade.",
        "battle_game_over": "Fim de jogo",
        "battle_you_won": "Você venceu!",
        "batt_attack": "Atacar",
        "batt_defeated": "foi derrotado",
        "battle_message_ban_trial": "Você oferece {1} a {0}.",
        "battle_message_ban_failure": "{0} recusou sua oferta.",
        "battle_message_ban_success": "Você provou seu valor. {0} se juntou à sua equipe.",
        "batt_sleeping": "está dormindo",
        "batt_healthy": "está saudável",
        "batt_poisoned": "está envenenado",
        "batt_petrified": "está petrificado",
        "batt_lunatic": "está fora de controle",
        "batt_change_sleeping": "adormeceu",
        "batt_change_healthy": "se recuperou",
        "batt_change_poisoned": "foi envenenado",
        "batt_change_petrified": "foi petrificado",
        "batt_change_lunatic": "perdeu o controle",
        "batt_info_status_effect_poisoned": "está sofrendo com veneno.",
        "batt_info_status_effect_sleeping": "está dormindo.",
        "batt_info_status_effect_petrified": "está petrificado.",
        "batt_info_status_effect_lunatic": "perdeu o controle.",
        "batt_info_status_effect_healthy": "está saudável.",
        "battle_start": "Você caiu em uma armadilha.",
        "escape_success": "Você conseguiu fugir!",
        "escape_fail": "Não há como escapar!",
        "level_up": "{0} alcançou um novo nível!",
        "results": "Resultados",
        "battle_choose_area": "escolha a área",
    },
    "inventory": {
        "reassurance": "Deseja continuar?",
        "reassurance-throwaway": "Descartar {0}?",
        "learn": "Aprender", "hint": "Dica:",
        "sphere_full": "A Guardosfera está cheia. Este item não pode ser usado.",
        "in_battle_item": "Mochila",
        "body": "Corpo", "hands": "Mãos", "head": "Cabeça", "feet": "Pés",
        "equip-body": "Armadura", "equip-hands": "Arma",
        "equip-head": "Proteção para cabeça", "equip-feet": "Calçados",
        "ability-carry-equipment": "Carrega {0}.",
        "tent": "Barraca", "tent-description": "Recupera a vida e a energia de toda a equipe.",
        "angel-tear": "Lágrima Angelical", "angel-tear-description": "Revive uma criatura.",
        "antivenom": "Antídoto", "antivenom-description": "Cura uma criatura envenenada.",
        "guardian-crystal": "Cristal", "guardian-crystal-description": "Necessário para capturar uma criatura.",
        "guardian-crystal-air": "Cristal de Ar", "guardian-crystal-water": "Cristal de Água",
        "guardian-crystal-earth": "Cristal de Terra", "guardian-crystal-fire": "Cristal de Fogo",
        "guardian-crystal-forest": "Cristal da Floresta", "guardian-crystal-mountain": "Cristal da Montanha",
        "guardian-crystal-spirit": "Cristal Espiritual", "guardian-crystal-lightning": "Cristal de Raio",
        "guardian-crystal-frost": "Cristal de Gelo",
        "potion-black": "Poção Negra", "potion-blue": "Poção Azul",
        "potion-cyan": "Poção Ciano", "potion-gold": "Poção Dourada",
        "potion-green": "Poção Verde", "potion-pink": "Poção Rosa",
        "potion-purple": "Poção Roxa", "potion-red": "Poção Vermelha",
        "bread": "Pão", "milk": "Leite",
        "sword-wood": "Espada de Madeira", "sword-rusty": "Espada Enferrujada",
        "sword-iron": "Espada de Ferro", "sword-steel": "Espada de Aço",
        "helmet-iron": "Capacete de Ferro", "shield-iron": "Escudo de Ferro",
        "shoes-leather": "Sapatos de Couro",
    },
    "attacks": {
        "attNone1_selfdef": "Defender", "attNone1_selfdef_desc": "Assume uma postura defensiva.",
        "attNone2_kick": "Chute", "attNone2_kick_desc": "Um chute alto.",
        "attNone3_tooth": "Mordida", "attNone3_tooth_desc": "Morde com dentes afiados.",
        "attNone4_punch": "Soco", "attNone4_punch_desc": "Um soco baixo.",
        "attNone5_slap": "Tapa", "attNone5_slap_desc": "Um tapa furioso.",
        "attNone6_triphazard": "Desequilíbrio", "attNone6_triphazard_desc": "Faz o oponente tropeçar.",
        "attNone7_shield": "Escudo", "attNone7_shield_desc": "Protege com um escudo.",
        "attNone8_sana": "Cura", "attNone8_sana_desc": "Cura um alvo com uma prece.",
        "attNone9_somnum": "Sono", "attNone9_somnum_desc": "Faz o alvo adormecer.",
        "attNone10_venenum": "Veneno", "attNone10_venenum_desc": "Envenena um alvo.",
        "attFire1_embers": "Brasas", "attFire1_embers_desc": "Lança brasas quentes no alvo.",
        "attFire2_fire": "Fogo", "attFire2_fire_desc": "Lança uma pequena chama.",
        "attFire3_flame": "Chama", "attFire3_flame_desc": "Lança uma bola de fogo maior.",
        "attFire4_blaze": "Labareda", "attFire4_blaze_desc": "Envolve o oponente em chamas.",
        "attEarth1_dirt": "Terra", "attEarth1_dirt_desc": "Lança terra.",
        "attEarth2_mud": "Lama", "attEarth2_mud_desc": "Lança lama.",
        "attEarth3_stones": "Pedras", "attEarth3_stones_desc": "Lança pedras.",
        "attEarth4_landslide": "Deslizamento", "attEarth4_landslide_desc": "Soterra o oponente sob um deslizamento de terra.",
        "attWater1_sprinkle": "Borrifo", "attWater1_sprinkle_desc": "Lança um pouco de água.",
        "attWater2_shower": "Chuva", "attWater2_shower_desc": "Faz chover sobre o oponente.",
        "attWater3_splash": "Jato d'água", "attWater3_splash_desc": "Dispara água contra o alvo.",
        "attWater4_waterjet": "Hidro Jato", "attWater4_waterjet_desc": "Dispara um jato forte de água.",
        "attWater5_icepillars": "Pilares de Gelo", "attWater5_icepillars_desc": "Esmaga o oponente entre pilares de gelo.",
        "attFire5_hellfire": "Fogo Infernal", "attFire5_hellfire_desc": "Queima todos os oponentes em um vórtice de fogo.",
    },
    "elements": {
        "element_earth": "Terra", "element_water": "Água", "element_fire": "Fogo",
        "element_air": "Ar", "element_frost": "Gelo", "element_mountain": "Montanha",
        "element_forest": "Floresta", "element_arthropoda": "Artrópode",
        "element_demon": "Demônio", "element_lindworm": "Serpente",
        "element_spirit": "Espírito", "element_lightning": "Raio", "element_none": "Nenhum",
    },
    "map_1": {
        "person_name_1_1": "Sonhador",
        "person_1_1": "Um dia vou conseguir um barco e navegar por este planeta tão bonito.",
        "sign_1_1_title": "Lago dos Bosques do Sul",
        "sign_1_1_text": "Tenha cuidado ao nadar aqui.",
        "sign_1_2_title": "Bosques do Sul",
        "sign_1_2_text": "Caminho para a Vila Timsey",
    },
    "map_2": {
        "person_name_2_1": "Caminhante",
        "person_2_1": "Cuidado ao caminhar sozinho pela floresta. Há criaturas fortes e perigosas por aqui.",
        "person_name_2_2": "Caminhante",
        "person_2_2": "Quando estou cansado, venho para a floresta. O ar fresco e o céu azul renovam minhas forças.",
        "sign_2_1_title": "Círculo de Cura",
        "sign_2_1_text": "Há centenas de anos, pessoas vêm a este lugar antigo em busca de cura. É possível sentir uma presença acolhedora por aqui.",
    },
    "map_25": {
        "guardian_25_1_text": "Miaaau",
        "guardian_25_1_title": "Shari",
        "sign_25_1_title": "Poço da Cidade",
        "sign_25_1_text": "Diz a lenda que Garia, a Serpente Dourada, fincou a cauda no chão e fez surgir uma fonte que devolveu a vida à terra.",
        "sign_25_2_title": "Catedral dos Elementos",
        "sign_25_2_text": "Boas-vindas à nossa catedral. Entre e encontre a paz.",
        "sign_25_3_title": "Boas-vindas",
        "sign_25_3_text": "Você mora aqui.",
        "sign_25_4_title": "Boas-vindas",
        "sign_25_4_text": "Boas-vindas a Exordia, a cidade dos novos começos.",
        "object_25_1_title": "Livro",
        "object_25_1_text": "Um livro pesado. A escrita é muito antiga e quase ilegível.",
        "object_25_2_text": "O livro está aberto, mas foi escrito em uma língua antiga. Você não consegue entendê-lo.",
        "object_25_3_title": "Panela",
        "object_25_3_text": "Um prato de aparência exótica. O cheiro é delicioso.",
        "object_25_4_text": "Uma sopa quase transparente. Tem cheiro de flores.",
        "object_25_5_text": "Muitos insetos fritos. Alguns parecem muito estranhos, mas têm um cheiro ótimo.",
        "object_25_6_title": "Kroki",
        "object_25_6_text": "Kroaah!",
        "object_25_7_title": "Poço",
        "object_25_7_text": "A água é limpa e potável.",
        "object_25_8_title": "Caixa",
        "object_25_8_text": "Não é muito pesada. Você consegue empurrá-la.",
        "person_name_25_1": "Comerciante",
        "person_25_1": "Olá! Sua mãe mandou você? Tenho o livro que ela estava procurando.",
        "person_name_25_2": "Cozinheiro Viajante",
        "person_25_2": "Olá! Prove um dos meus pratos deliciosos. Viajei pelo mundo e reuni muitas receitas.",
        "person_name_25_3": "Comerciante",
        "person_25_3": "Pode olhar os livros. Alguns são muito raros.",
        "person_name_25_4": "Cozinheiro",
        "person_25_4": "Está com fome? Não? Volte quando quiser provar meus pratos especiais.",
        "person_name_25_5": "Comerciante",
        "person_25_5": "Queria ter mais livros aqui. O vendedor do outro lado tem os mesmos livros, mas muito mais baratos.",
        "person_name_25_6": "Comerciante",
        "person_25_6": "Precisa de uma panela nova? Tenho peças de ótima qualidade: cobre, ferro e até prata.",
        "person_name_25_7": "Jona",
        "person_25_7": "Kroki e eu estamos esperando a cerimônia começar. Disseram que você completa 16 anos hoje. Feliz aniversário!",
        "person_name_25_8": "Homem Feliz",
        "person_25_8": "Que dia lindo! Não me importo nem com a chuva.",
        "person_name_25_9": "Piere",
        "person_25_9": "Com meu guardião ao meu lado, não tenho medo de nada.",
        "person_name_25_10": "Criança",
        "person_25_10": "Queria ter idade suficiente para receber meu primeiro Guardião.",
        "person_name_25_11": "Sr. Agricultor",
        "person_25_11": "Estou pensando em cultivar algumas frutas no meu jardim. O que acha?",
        "person_name_25_12": "Sr. Haro",
        "person_25_12": "Não saia da cidade agora. A cerimônia está prestes a começar.",
        "person_name_25_13": "Sr. Melodia",
        "person_25_13": "Estou cantaaando na chuva...",
        "person_name_25_14": "Hapi",
        "person_25_14": "Está vendo aquele botão no chão? Sempre que encontrar um, pise nele e veja o que acontece! Instalei este para abrir a escada até a plataforma ali.",
        "person_name_25_15": "Tio Fir",
        "person_25_15": "Você deveria ver seus pais antes do início da cerimônia.",
        "person_name_25_16_0": "Pessoa A",
        "person_25_16_0": "Você ouviu isso?",
        "person_name_25_16_1": "De onde veio?",
        "person_name_25_17_0": "Pessoa B",
        "person_25_17_0": "Sim. Vamos dar uma olhada.",
        "person_name_25_17_1": "De algum lugar ali, perto da catedral!",
    },
    "map_251": {
        "person_name_251_1": "Pai",
        "person_251_1": "Feliz aniversário! Estou muito animado. Hoje, na cerimônia, você receberá seu Guardião! Tio Fir está esperando por nós. Vamos nos encontrar na catedral.",
        "person_name_251_2": "Mãe",
        "person_251_2": "Feliz aniversário, meu querido. Seu pai parece ainda mais animado que você. Estamos saindo. Seu tio está esperando. Não se atrase!",
        "object_book": "Livro Antigo",
        "object_book_desc": "Está bem empoeirado. Faz muito tempo que ninguém o abre.",
        "object_fireplace": "Lareira",
        "object_fireplace_desc": "Há um fogo quentinho queimando. Dá para sentir o cheiro da madeira fresca.",
    },
    "map_252": {
        "object_book": "Estante de Livros",
        "object_book_desc": "Muitos livros grossos sobre ciência, Guardiões, filosofia...",
        "object_fireplace": "Lareira",
        "object_fireplace_desc": "Há um fogo quentinho queimando. Dá para sentir o cheiro da madeira fresca.",
    },
    "map_253": {
        "person_253_1_text": "Este ano temos quatro jovens que completaram 16 anos. Prepare-se, a cerimônia está prestes a começar.",
        "person_253_1_name": "Sábio Kahu",
        "person_253_2_text": "Meu filho também completou 16 anos. Mas você já sabe disso, é claro.",
        "person_253_3_text": "Silêncio, por favor. Antes da cerimônia começar, quero fazer uma prece aos deuses.",
        "person_253_4_text": "Seus pais já chegaram? Não estou conseguindo vê-los.",
        "person_253_5_text": "A cerimônia vai começar muito em breve. Já está animado?",
        "person_253_6_text": "O sábio disse que quatro jovens completaram 16 anos este ano. Será uma cerimônia especial.",
        "person_253_7_text": "Já decidiu qual Guardião vai escolher?",
        "person_253_8_text": "Quando completei 16 anos, escolhi um Guardião da Água. Adoro nadar e estar perto do mar.",
        "person_253_9_text": "Como se sentiu quando seu primeiro chakra despertou? Eu fiquei animado e com medo ao mesmo tempo.",
    },
    "monsters": {
        "g1_desc": "Os Fordin estão entre os primeiros Guardiões que saíram da Guardosfera para se aproximar dos humanos. O broto em sua cauda cresce muito devagar, e poucos chegaram a florescer.",
        "g2_desc": "Apesar da aparência assustadora, os Kroki mantêm sua natureza gentil durante toda a vida, tornando-se companheiros ideais para crianças e famílias.",
        "g3_desc": "Diz a lenda que os primeiros Devidin eram criaturas perversas, que atacavam outros Guardiões e humanos sem motivo. Hoje, costumam ser amigáveis.",
        "g4_desc": "Os Aerodin têm ossos ocos, mas muito resistentes. Um Aerostag adulto pesa apenas cerca de 20 kg e consegue saltar mais de 30 metros.",
        "g5_desc": "Os Weastoat são criaturas atrevidas que pregam peças em viajantes na floresta, mas nunca fazem mal se não forem provocados.",
        "g6_desc": "Em noites claras, Mootys se reúnem em grandes grupos nas clareiras iluminadas pela lua, no fundo da floresta. O menor ruído os faz fugir.",
        "g7_desc": "À medida que envelhecem, os Wuppys perdem sua forma engraçada. Ao se transformar em Deemog, ganham chifres que ficam cada vez mais prateados.",
        "g8_desc": "Embora os Dradder possam injetar veneno mortal com os dentes, quase nunca fazem isso. Só recorrem a essa arma em situações extremas.",
        "g9_desc": "Os Spreye têm uma perna muito elástica e tentam saltar cada vez mais alto. Quando não conseguem superar sua própria marca, criam asas e se transformam em Buttereye.",
        "g10_desc": "Os Breem só colocam ovos nas maçãs mais perfeitas. Se outro Breem colocar um ovo do sexo oposto na mesma maçã, os dois podem se transformar juntos.",
        "g11_desc": "Nos primeiros anos, os Marvillar são preguiçosos e estão sempre com fome. Depois de comer mil vezes o próprio peso, transformam-se em Marvantis versáteis e protetores.",
        "g12_desc": "Os Palmpot podem viver muitos anos. Algumas famílias convivem com os Bonose, que chegaram ao nosso mundo há muitas gerações.",
        "g13_desc": "Os Erimat são criaturas solitárias das montanhas e raramente aparecem para humanos. Conquistar sua confiança leva tempo, mas tornam-se aliados muito leais.",
        "g14_desc": "Muitas pessoas confundem Eggatch com o café da manhã e acabam cobertas pela substância viscosa que ele cospe para se defender. Os Owlock adoram chaves.",
    },
}
for bundle, values in supplemental.items():
    source = locale_dir / f"{bundle}.properties"
    target = locale_dir / f"{bundle}_pt_BR.properties"
    if not source.exists():
        raise FileNotFoundError(f"Bundle original ausente: {source}")
    lines = source.read_text(encoding="utf-8").splitlines()
    with target.open("w", encoding="utf-8") as out:
        for line in lines:
            if "=" in line and not line.lstrip().startswith("#"):
                key = line.split("=", 1)[0].strip()
                if key in values:
                    line = f"{key}={values[key]}"
            out.write(line + "\n")

print("Overlay aplicado: identidade, textos de interface, batalha, itens, ataques, criaturas e diálogos dos mapas em pt-BR.")



# Import the supplied Clover Valley art pack into the APK without changing the upstream submodule.
from zipfile import ZipFile
from PIL import Image, ImageOps

clover_archive = Path("Clover Valley V2 Free.zip")
clover_prefix = "Clover Valley V2 Free/"
clover_assets = root / "android/assets/clover_valley"
clover_assets.mkdir(parents=True, exist_ok=True)
with ZipFile(clover_archive) as zf:
    for info in zf.infolist():
        if info.is_dir() or not info.filename.startswith(clover_prefix):
            continue
        relative = Path(info.filename[len(clover_prefix):])
        if ".." in relative.parts:
            raise ValueError(f"Unsafe archive path: {info.filename}")
        target = clover_assets / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        with zf.open(info) as src, target.open("wb") as dst:
            shutil.copyfileobj(src, dst)

# Preserve the supplied map previews as references inside the app package.
map_archive = Path("pokemon-rpg-android-clover-valley-map.zip")
with ZipFile(map_archive) as zf:
    for preview_name in ("map_preview.png", "map_preview2.png"):
        matches = [n for n in zf.namelist() if n.endswith("/" + preview_name) or n == preview_name]
        if matches:
            target = clover_assets / preview_name
            with zf.open(matches[0]) as src, target.open("wb") as dst:
                shutil.copyfileobj(src, dst)

# Build the player's directional atlas from the user's supplied six-frame Clover walk sheets.
walk_dir = clover_assets / "Character/Boy/Walk"
direction_sources = {
    "n": ("walk_up.png", False),
    "e": ("walk_side.png", False),
    "s": ("walk_down.png", False),
    "w": ("walk_side.png", True),
}
directions = []
for direction, (filename, mirror) in direction_sources.items():
    sheet = Image.open(walk_dir / filename).convert("RGBA")
    if sheet.width % 6 != 0 or sheet.height != 64:
        raise ValueError(f"Unexpected Clover sprite sheet dimensions: {filename} {sheet.size}")
    frames = []
    for frame_index in range(6):
        frame = sheet.crop((frame_index * 64, 0, (frame_index + 1) * 64, 64))
        bounds = frame.getbbox()
        if not bounds:
            raise ValueError(f"Empty sprite frame: {filename} #{frame_index}")
        sprite = frame.crop(bounds)
        if mirror:
            sprite = ImageOps.mirror(sprite)
        if sprite.width > 16 or sprite.height > 32:
            sprite.thumbnail((16, 32), Image.Resampling.NEAREST)
        cell = Image.new("RGBA", (16, 32), (0, 0, 0, 0))
        cell.alpha_composite(sprite, ((16 - sprite.width) // 2, 32 - sprite.height))
        frames.append(cell)
    directions.append((direction, frames))

hero_image = Image.new("RGBA", (433, 34), (0, 0, 0, 0))
atlas_lines = [
    "hero.png",
    "format: RGBA8888",
    "filter: Nearest,Nearest",
    "repeat: none",
]
frame_number = 0
for direction, frames in directions:
    for index, frame in enumerate(frames, start=1):
        x = 1 + frame_number * 18
        y = 1
        hero_image.alpha_composite(frame, (x, y))
        atlas_lines.extend([
            direction,
            "  rotate: false",
            f"  xy: {x}, {y}",
            "  size: 16, 32",
            "  orig: 16, 32",
            "  offset: 0, 0",
            f"  index: {index}",
        ])
        frame_number += 1

spritesheet_dir = root / "android/assets/spritesheets"
hero_image.save(spritesheet_dir / "hero.png")
(spritesheet_dir / "hero.pack").write_text("\n".join(atlas_lines) + "\n", encoding="utf-8")
print("Clover Valley imported; player atlas now uses six directional walk frames from the supplied sprites.")
