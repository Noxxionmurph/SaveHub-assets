# Credits

SaveForge is an unofficial, free, non-commercial fan tool. It is not affiliated with or endorsed by Nintendo,
Game Freak or Creatures Inc. Pokémon and everything that belongs to it is theirs.

The pictures are not part of this code repository. They live in a separate repository,
[SaveHub-assets](https://github.com/Noxxionmurph/SaveHub-assets), and the site loads them from there, so the editor works
the same (without the pictures) if they are ever removed. This is who made them.

## Pokémon, item and type icons

From **PokéSprite** by msikma (https://github.com/msikma/pokesprite), copied unchanged except for renaming the
Pokémon files to their National Dex number (and Unown's other letters to `201-<letter>.png`, with `!` and `?` as
`201-exclamation.png` and `201-question.png`). The shiny icons in `sprites/pokemon/shiny/` are PokéSprite's own shiny versions of the same icons. PokéSprite's own code is MIT licensed; the artwork is not covered by that
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

The eight Hoenn badges (`sprites/badges/hoenn/1.png` to `8.png`, Stone to Rain) are Ruby, Sapphire and Emerald's own
trainer card badges, from the pret/pokeemerald disassembly (https://github.com/pret/pokeemerald,
`graphics/trainer_card/badges.png`), in the sheet's own colours (the games show them in silver), with the background
made transparent. SaveHub's `scripts/extract-hoenn-badges.py` redoes them.

## Battle Frontier symbols

Emerald's seven Battle Frontier symbols (`sprites/frontier/silver-1.png` to `silver-7.png` and `gold-1.png` to
`gold-7.png`, Tower to Pyramid) are the Frontier Pass's own symbols, from the pret/pokeemerald disassembly
(`graphics/frontier_pass/medals.png`), in the silver and gold palettes the game loads for them (`silver.pal`,
`gold.pal`), with the background made transparent. SaveHub's `scripts/extract-frontier-symbols.py` redoes them.

## Gen 3 ribbons

The 32 Gen 3 ribbons (`sprites/ribbons/gen3/0.png` to `31.png`, numbered like the games' ribbon ids: 0 Champion,
1-20 the Cool, Beauty, Cute, Smart and Tough contest ribbons from Normal to Master Rank, 21-24 Winning, Victory, Artist
and Effort, 25-31 Marine to World) are the PokéNav's own 32x32 ribbon pictures, from the pret/pokeemerald disassembly
(`graphics/pokenav/ribbons/icons_big.png`), each in the palette the game gives it (`icons1.pal` to `icons5.pal`), with
the background made transparent. SaveHub's `scripts/extract-gen3-ribbons.py` redoes them.

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

## Gen 3 Pokéblocks

The 14 Pokéblock colours (`sprites/pokeblocks/1.png` to `14.png`, numbered like the colour a save stores: 1 Red ...
14 Gold) are the 8x8 Pokéblock from the pret/pokeemerald disassembly (`graphics/pokeblock/pokeblock.png`), in each of
the palettes the game uses for it (`red.pal` to `gold.pal`), with the background made transparent. SaveHub's
`scripts/extract-pokeblocks.py` redoes them.

## Window frames

The frames the games' OPTION menu offers under FRAME (`sprites/frames/`, numbered like the menu's TYPE 1, TYPE 2 ...)
are each laid out as 3x3 tiles of 8x8 (corners, edges and a middle the games never draw). Gold, Silver and Crystal
share eight: the six 1bpp tiles of the pret/pokecrystal disassembly's `gfx/frames/1.png` to `8.png` (identical in
pret/pokegold), with the top and bottom edge both the game's ─ tile and both sides its │ tile, as the game draws them,
in black on transparent so the editor can draw them in the window's own colours. Ruby and Sapphire's twenty are
pret/pokeruby's `graphics/text_window/1.png` to `20.png`, and Emerald's (nine of them redrawn) pret/pokeemerald's, in
the colours the GBA shows, with colour 0 (which the game leaves see-through) made transparent. SaveHub's
`scripts/extract-frames.py` redoes them.

## Secret bases

The secret base pictures (`sprites/secret-bases/`) come from the pret/pokeemerald disassembly. `red_cave.png`,
`brown_cave.png`, `blue_cave.png`, `yellow_cave.png`, `tree.png` and `shrub.png` are every metatile of the secret base
tileset (`data/tilesets/secondary/secret_base/metatiles.bin`, which the rooms and the decorations share), drawn from the
primary secret base tiles and that kind's own tiles and palettes, 16 to a row. `dolls/<decoration id>.png` are the
dolls and cushions, which the game shows as sprites: the first frame of each one's picture in
`graphics/object_events/pics/` in its object palette, with colour 0 made transparent. SaveHub's
`scripts/extract-secret-bases.py` redoes them.
