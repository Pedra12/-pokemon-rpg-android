# Tuxemon Android

Este projeto integra o jogo open-source [Tuxemon](https://github.com/Tuxemon/Tuxemon), fixado em um commit específico da branch `development`, preservando os arquivos originais do jogo, mapas, personagens, criaturas, músicas, efeitos sonoros e créditos.

O código completo fica vinculado como submódulo Git em `Tuxemon/`. Para obter o conteúdo junto com este repositório, clone com:

```bash
git clone --recurse-submodules https://github.com/Pedra12/-pokemon-rpg-android.git
```

## Android

O workflow **Android APK** prepara a configuração mobile (retrato, tela cheia, direcional touch e botões A/B ativados), executa o teste do controle por toque e tenta compilar o APK de depuração. O APK é publicado como artefato da execução do GitHub Actions.

## Créditos e licença

O código e os recursos originais permanecem sob as licenças e atribuições indicadas pelo projeto Tuxemon, incluindo `Tuxemon/LICENSE` e `Tuxemon/ATTRIBUTIONS.md`. O código principal é GPL-3.0-or-later; recursos individuais podem ter termos próprios.
