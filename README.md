# SaveHub-assets

The pictures used by [SaveForge](https://github.com/Noxxionmurph/SaveHub), an unofficial, free, non-commercial fan
save editor: Pokémon, item and type icons, gym badges and Pikachu's reactions. The editor loads them from this
repository's site (`https://noxxionmurph.github.io/SaveHub-assets/sprites/...`). They are kept apart from the editor's
code so that either can change or be removed without touching the other. The editor still works without them.

All of it is © Nintendo / Creatures Inc. / GAME FREAK Inc. and is not covered by any licence of mine. See
[CREDITS.md](CREDITS.md) for where each set comes from. Not affiliated with or endorsed by Nintendo, Game Freak or
Creatures. If you own any of this artwork and want it removed, open an issue on
[SaveHub](https://github.com/Noxxionmurph/SaveHub/issues).

```
sprites/pokemon/<dex>.png          68x56 box icons, National Dex 1-251 (Unown's letters as 201-<letter>.png)
sprites/pokemon/shiny/<dex>.png    the same icons in their shiny colours
sprites/items/<category>/<name>.png  32x32 item icons
sprites/types/<type>.png           128x128 type icons
sprites/type-labels/<type>.png     32x16 in-game type labels (Emerald's), plus unknown.png for ???
sprites/badges/<1-8>.png           16x16 gym badges
sprites/marks/shiny.svg            the shiny mark (Sword and Shield onwards)
sprites/pikachu.png                80x720 sheet: 18 reactions, two 40x40 frames each
```

To use it with a local copy of the editor: `git clone https://github.com/Noxxionmurph/SaveHub-assets assets` inside the
editor's folder, then `npm run dev`.
