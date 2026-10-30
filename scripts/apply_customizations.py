#!/usr/bin/env python3
"""Apply the first safe Brazilian Portuguese and release-mode overlay to Guardian Monsters."""
from pathlib import Path

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
