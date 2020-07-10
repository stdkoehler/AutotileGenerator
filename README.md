# AutotileGenerator
Generates a tilemap usable for autotiles from subtiles (e.g. in Godot)

## Generating the subtiles
We start with a small tileset including all required subtiles (inner and outer borders as well as center tile
and variations)

![Original](.doc/Original.png)

We cut this tileset into according subtiles and save them with the given nomenclature as single files:

_tyx_.png -> t: Inner/Outer, y: Top/Center/Bottom, x: Left/Center/Right

    I: Inner
    T: Top
    B: Bottom
    C: Center
    L: Left
    R: Right
    
Special cases are OC**0**.png and OC**i**.png for variations of the center tiles.
In the current script it's assumed that OC0.png, OC1.png and OC2.png exist.
Additionally one tile NNN.png of full transparency with according size is required.

e.g.


|  |  |
| -------- | -------- |
| ![](.doc/ITL.png) | ![](.doc/ITR.png) |
| *ITL.png* |*ITR.png* |
| ![](.doc/IBL.png) | ![](.doc/IBR.png) |
| *IBL.png* |*IBR.png* |

|  |  | |
| -------- | -------- | -------- |
| ![](.doc/OTL.png) | ![](.doc/OTC.png) | ![](.doc/OTR.png) |
| *OTL.png* |*OTC.png* | *OTR.png* |
| ![](.doc/OCL.png) | ![](.doc/OC0.png) | ![](.doc/OCR.png) |
| *OCL.png* |*OC0.png* | *OCR.png* |
| ![](.doc/OBL.png) | ![](.doc/OBC.png) | ![](.doc/OBR.png) |
| *OBL.png* |*OBC.png* | *OBR.png* |

## Running the script AutotileGenerator.py

A png is created which can be used for autotiling: 

![](.doc/autotile_dirt_dark.png)

## Godot Example

The generated png can be e.g. used with Godot's *Autotile*:

![](.doc/godot.png)
