# Crônicas de Arvandor — projeto Android

Projeto de RPG 2D de exploração e captura de criaturas, com mapas, personagens, inventário e batalhas por turnos. O código-base e os recursos gráficos estão vinculados pelo submódulo Guardian Monsters.

## Obter o projeto completo

Clone incluindo os recursos:

```bash
git clone --recurse-submodules https://github.com/Pedra12/-pokemon-rpg-android.git
```

Se já clonou sem os recursos:

```bash
git submodule update --init --recursive
```

## Compilação Android

O workflow [Build Guardian Monsters Android APK](https://github.com/Pedra12/-pokemon-rpg-android/actions/workflows/android.yml) compila a variante Debug e publica o APK como artefato da execução. Abra a aba Actions, escolha uma execução concluída com sucesso e baixe `guardian-monsters-android-debug`.

## Personalizações aplicadas no processo de build

O script `scripts/apply_customizations.py`:
- desativa o modo de depuração que iniciava o jogo em uma tela de teste;
- altera o nome exibido do aplicativo para **Crônicas de Arvandor**;
- adiciona os primeiros arquivos de localização pt-BR para menus, elementos, batalha, inventário e ataques.

A tradução ainda é parcial. Textos de mapas, diálogos, itens e outros menus precisam de revisão e tradução completa.

## Limitações ainda abertas

A base original usa orientação paisagem e resolução lógica 428×240. A adaptação correta para retrato 9:16 exige reorganizar telas, HUD, câmera e controles, não apenas trocar uma propriedade do manifesto. Por isso, a orientação paisagem foi mantida nesta etapa para evitar um APK que abre com a interface cortada. A campanha, nomes, criaturas e diálogos também ainda precisam de uma revisão criativa para estabelecer uma identidade totalmente original.

## Licenças e créditos

A base Guardian Monsters declara código sob Apache-2.0 e arte sob CC-BY-3.0. Há também bibliotecas, fontes, música, efeitos e outros recursos de terceiros com licenças próprias. Consulte [CREDITOS-E-LICENCAS.md](CREDITOS-E-LICENCAS.md) e `GuardianMonsters/third-party-notes/THIRD-PARTY-NOTES.md` antes de redistribuir ou publicar.
