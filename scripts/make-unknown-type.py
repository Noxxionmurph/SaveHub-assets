"""Draws sprites/types/unknown.png, the ??? type's icon (Curse in Gen 2). PokéSprite has no Gen 8 icon for it, since the
type was gone by then, so this one is drawn in the same style: a 128x128 circle in ???'s teal (Gen 4's colour for it)
with a white question mark. Needs Pillow and the Inter Display Bold font.

    python3 scripts/make-unknown-type.py
"""
from PIL import Image, ImageDraw, ImageFont

S = 8  # draw large, then shrink, for smooth edges like PokéSprite's icons
img = Image.new('RGBA', (128 * S, 128 * S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
d.ellipse((2 * S, 2 * S, 126 * S - 1, 126 * S - 1), fill=(0x68, 0xa0, 0x90, 255))
font = ImageFont.truetype('/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf', 88 * S)
d.text((64 * S, 66 * S), '?', font=font, fill=(255, 255, 255, 255), anchor='mm')
img.resize((128, 128), Image.LANCZOS).save('sprites/types/unknown.png', optimize=True)
