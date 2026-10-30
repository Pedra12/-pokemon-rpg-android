# Base do RPG Android e créditos

Este repositório está preparando uma compilação Android a partir do projeto aberto **Guardian Monsters**.

## Projeto-base

- Repositório original: https://github.com/lucidtanooki/guardian_monsters
- Autor do projeto: Georg Eckert (lucidtanooki)
- Tecnologia: libGDX, Kotlin, Java, Tiled e Android Gradle Plugin.
- O projeto original inclui exploração em mapas por tiles, movimento em quatro direções, domesticação de monstros, inventário, habilidades, batalhas animadas e sistema elemental.

## Licenças do projeto original

Conforme o README do projeto original:
- Código-fonte: Apache License 2.0.
- Artes do projeto: Creative Commons Attribution 3.0 (CC BY 3.0).
- Componentes e recursos de terceiros: consultar obrigatoriamente `third-party-notes/THIRD-PARTY-NOTES.md` no repositório original e manter as atribuições exigidas.

## Adaptações planejadas para este jogo

O projeto será adaptado com identidade própria, sem personagens, nomes, marcas, mapas ou criaturas de Pokémon:
- Textos em Português do Brasil e opção de inglês.
- Personagens e criaturas originais.
- Interface e controles móveis.
- Ajustes de proporção e apresentação para celular.
- História, mapas e progressão próprios.

## Estado atual

O workflow em `.github/workflows/android.yml` baixa o projeto-base durante a compilação e tenta gerar um APK Android de depuração. Isso ainda não significa que o jogo esteja adaptado ou pronto para distribuição. A compilação precisa terminar e ser validada; depois serão feitas as adaptações e testes.

Créditos e avisos de licença devem acompanhar qualquer redistribuição dos arquivos originais.
