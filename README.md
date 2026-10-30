# Projeto RPG Android

Projeto de RPG 2D para Android, com exploração por mapas, personagens, criaturas, inventário e batalhas por turnos.

## Código-fonte e recursos

A pasta `GuardianMonsters/` é um submódulo Git fixado em uma revisão do projeto aberto [Guardian Monsters](https://github.com/lucidtanooki/guardian_monsters). Ela disponibiliza a base de código, mapas, sprites, animações, fontes e demais recursos.

Para baixar o conteúdo completo, clone com:

```bash
git clone --recurse-submodules https://github.com/Pedra12/-pokemon-rpg-android.git
```

Se já clonou sem os recursos:

```bash
git submodule update --init --recursive
```

## Gerar APK

O GitHub Actions compila a versão Android Debug e publica o APK como artefato:

1. Abra a aba **Actions**.
2. Selecione **Build Guardian Monsters Android APK**.
3. Abra uma execução concluída com sucesso.
4. Baixe **guardian-monsters-android-debug**.

Workflow: [Android APK](https://github.com/Pedra12/-pokemon-rpg-android/actions/workflows/android.yml).

## Licenças e créditos

A base Guardian Monsters declara código sob Apache-2.0 e arte sob CC-BY-3.0. Dependências, fontes, áudio e arte de terceiros têm licenças próprias. Consulte [CREDITOS-E-LICENCAS.md](CREDITOS-E-LICENCAS.md) e `GuardianMonsters/third-party-notes/THIRD-PARTY-NOTES.md` antes de redistribuir ou publicar.

## Estado do projeto

A base e o submódulo estão integrados ao repositório, e a compilação Android está em validação. A base original ainda precisa ser personalizada para virar um jogo independente, com identidade visual, nomes, diálogos e criaturas próprias em português brasileiro. A configuração Android herdada está em orientação paisagem; a adaptação para vertical 9:16, controles móveis e revisão de telas ainda precisa ser implementada e testada. O APK Debug não deve ser tratado como versão final de lançamento.
