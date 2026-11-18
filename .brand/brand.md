# Passkey brand kit

Mark 1-2. Kit folder: `passkey/kit/`. Marks are letter-free; only the lockups and banners carry the name.

## Palette

| Role | HEX | RGB |
|---|---|---|
| Background | #1C1B1F | 28 27 31 |
| Orange | #D05A19 | 208 90 25 |
| Cream | #F2E0CC | 242 224 204 |
| Orange | #A94412 | 169 68 18 |
| Orange | #CB5414 | 203 84 20 |
| Orange | #E97929 | 233 121 41 |
| Cream | #D5AD88 | 213 173 136 |
| Orange | #DF681F | 223 104 31 |
| Cream | #BA9571 | 186 149 113 |
| Mono cream / charcoal / black / white | #F2E0CC / #1C1B1F / #000000 / #FFFFFF | 242 224 204 / 28 27 31 / 0 0 0 / 255 255 255 |

The vector master has 8 colour layer(s). This is above the 2 to 3 colour house guideline because the faceted artwork depends on its shaded tones; the actual colours are kept exactly (no posterising). Use the mono set where a strict 2 to 3 colour limit applies.

## Typeface

Space Grotesk (Google Fonts, SIL OFL 1.1): SemiBold for the name in lockups and banners, Regular for text and captions. A technical grotesk with trustworthy, distinctive letterforms, precise without being cold; shares DNA with the monospace family. Names are outlined in every SVG/PDF; install the TTFs in `fonts/` for new text. Licence: `fonts/OFL.txt`.

## Rules

- Clear space: x = 0.25 x mark height (tight bounding box) on all sides.
- Minimum size: 32 px tall (digital) / 10 mm (print). Below that use `png/favicon-16.png`.
- Do: use the supplied files; keep clear space; cream marks go on dark or mid backgrounds, use the light version (or mono charcoal) on light.
- Don't: stretch or skew, recolour, add shadows/glow/gradients, or place on busy backgrounds.

## Files

### `png/`
Raster set (avatars, logos, mark-transparent, favicons + .ico, apple-touch/PWA icons, maskable, social preview mark-only)

`apple-touch-icon-180.png`, `avatar-1024.png`, `avatar-500.png`, `favicon-16.png`, `favicon-32.png`, `favicon-48.png`, `favicon.ico`, `icon-192.png`, `icon-512.png`, `logo-rounded-160.png`, `logo-rounded.png`, `logo-square-2048.png`, `logo-square.png`, `mark-transparent-2048.png`, `mark-transparent.png`, `maskable-512.png`, `social-preview-1280x640.png`

### `svg/`
Vector masters: full colour on background, full colour transparent, one-colour versions. Palette-exact, one filled path per colour layer

`mark-color-on-bg.svg`, `mark-color.svg`, `mark-mono-black.svg`, `mark-mono-charcoal.svg`, `mark-mono-cream.svg`, `mark-mono-white.svg`

### `pdf/`
Vector PDFs generated from the SVGs

`mark-color-on-bg.pdf`, `mark-color.pdf`, `mark-mono-black.pdf`, `mark-mono-charcoal.pdf`, `mark-mono-cream.pdf`, `mark-mono-white.pdf`

### `mono/`
One-colour marks (cream #F2E0CC, charcoal #1C1B1F, black, white) as SVG and transparent PNG, with knockouts so the silhouette reads

`mono-black.png`, `mono-black.svg`, `mono-charcoal.png`, `mono-charcoal.svg`, `mono-cream.png`, `mono-cream.svg`, `mono-white.png`, `mono-white.svg`

### `lockups/`
Mark + name (set in the mark typeface, outlined). Horizontal and stacked x dark / light / transparent (for dark use) / transparent-onlight, as SVG, PDF and PNG

`passkey-horizontal-dark.pdf`, `passkey-horizontal-dark.png`, `passkey-horizontal-dark.svg`, `passkey-horizontal-light.pdf`, `passkey-horizontal-light.png`, `passkey-horizontal-light.svg`, `passkey-horizontal-transparent-onlight.pdf`, `passkey-horizontal-transparent-onlight.png`, `passkey-horizontal-transparent-onlight.svg`, `passkey-horizontal-transparent.pdf`, `passkey-horizontal-transparent.png`, `passkey-horizontal-transparent.svg`, `passkey-stacked-dark.pdf`, `passkey-stacked-dark.png`, `passkey-stacked-dark.svg`, `passkey-stacked-light.pdf`, `passkey-stacked-light.png`, `passkey-stacked-light.svg`, `passkey-stacked-transparent-onlight.pdf`, `passkey-stacked-transparent-onlight.png`, `passkey-stacked-transparent-onlight.svg`, `passkey-stacked-transparent.pdf`, `passkey-stacked-transparent.png`, `passkey-stacked-transparent.svg`

### `banners/`
README banner 1280x320 and social preview with name 1280x640, both on dark

`banner-readme-1280x320.png`, `banner-readme-1280x320.svg`, `social-preview-name-1280x640.png`, `social-preview-name-1280x640.svg`

### `fonts/`
Static TTFs for the mark's typeface (name and body weights) and the SIL OFL licence

`OFL.txt`, `SpaceGrotesk-Regular.ttf`, `SpaceGrotesk-SemiBold.ttf`

`brand-sheet.pdf`: one-page brand sheet (versions, palette, typeface, clear space, minimum size, dos and don'ts). `brand.md`: this file.

## Vector fidelity

SVG (rendered at 1024) vs the flat-palette raster: 0.0% of pixels differ by more than 40/255 away from colour edges (0.383% including the 1 px edge antialiasing); mean abs diff 0.29/255. Node counts: colour 3148, mono 391.
