# Credits

SaveForge is an unofficial, free, non-commercial fan tool. It is not affiliated with or endorsed by Nintendo,
Game Freak or Creatures Inc. Pokémon and everything that belongs to it is theirs.

The pictures are not part of this code repository. They live in a separate repository,
[SaveHub-assets](https://github.com/Noxxionmurph/SaveHub-assets), and the site loads them from there, so the editor works
the same (without the pictures) if they are ever removed. This is who made them.

## Pokémon, item and type icons

From **PokéSprite** by msikma (https://github.com/msikma/pokesprite), copied unchanged except for renaming the
Pokémon files to their National Dex number (and Unown's other letters to `201-<letter>.png`). The shiny icons in `sprites/pokemon/shiny/` are PokéSprite's own shiny versions of the same icons. PokéSprite's own code is MIT licensed; the artwork is not covered by that
licence.

## The ??? type icon

`sprites/types/unknown.png` (the ??? type, Curse's in Gen 2) is drawn for this repository in the style of PokéSprite's
Gen 8 type icons, which have none for it: a circle in ???'s teal with a white question mark, in the Inter Display font.
`scripts/make-unknown-type.py` redraws it.

## Type labels

`sprites/type-labels/<type>.png` (each type's name in its coloured box, 32x16) are Pokémon Emerald's own summary screen
labels, from the pret/pokeemerald disassembly (https://github.com/pret/pokeemerald, `graphics/types/`), in the colours
the game gives them, with the background made transparent and renamed to the editor's type names (`fight` to `fighting`,
`mystery` to `unknown`). Gen 1 and Gen 2 have no coloured type labels of their own. `scripts/extract-type-labels.py`
redoes them.

## Shiny mark

`sprites/marks/shiny.svg` is the two-sparkle shiny mark from Pokémon Sword and Shield's summary screen (used by the
games since), traced by hand as a vector shape in the game's colour.

## Gym badges

The eight Kanto badges (`sprites/badges/1.png` to `8.png`) are cut from the Red/Blue "Trainer Card" sheet on The Spriters Resource
(https://www.spriters-resource.com/game_boy_gbc/pokemonredblue/asset/8733/, ripped by FrenchOrange), using the Super
Game Boy colour panel. `scripts/extract-badges.py` redoes the cut.

The eight Johto badges (`sprites/badges/johto/1.png` to `8.png`, Zephyr to Rising) are Gold and Silver's own trainer card
badges, from the pret/pokegold disassembly (https://github.com/pret/pokegold, `gfx/trainer_card/badges.png`), in the
colours the game gives them on a Game Boy Color (its badge palette). `scripts/extract-johto-badges.py` redoes them.

## Pikachu's reactions

`sprites/pikachu.png` (two 40x40 frames for each of the 18 ways your Pokémon Yellow starter reacts when you talk to it,
one reaction per row) holds Pokémon Yellow's own pictures in the Super Game Boy colours. They are cut from the
"Pikachu's moods" sheet on Serebii (https://www.serebii.net/yellow/pikachu.shtml), which is built from the game's
graphics. `scripts/extract-pikachu.py` redoes the cut. Frames that also exist in the pret/pokeyellow disassembly
(https://github.com/pret/pokeyellow, `gfx/pikachu/`) are pixel-identical to it, which is how each row was matched to
the game's name for it.

## Game data

Save layouts and tables were worked out with the help of the pret disassemblies
([pokered](https://github.com/pret/pokered), [pokeyellow](https://github.com/pret/pokeyellow)) and checked against
cartridge dumps the author owns (`scripts/verify-against-rom.mjs`; nothing from the ROMs is stored in this repository).

All the artwork is © Nintendo / Creatures Inc. / GAME FREAK Inc.
