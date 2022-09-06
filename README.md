# rhinopython scripts

## Introduction

This repository contains several [Rhino.Python](https://developer.rhino3d.com/guides/rhinopython/) custom scripts that can be used in the Rhinoceros 3D software. These scripts aim at automating simple repetitive tasks in the process of using Rhinoceros 3D to produce architectural models. The scripts' actions are described below.

### ApplyColorToElement.py

Applies a display color and a print color to the selected element(s).

### CopyAllLayouts.py

Copies the selected element(s) on all layouts.

### ZEAAllLayouts.py

Runs the command 'Zoom Extents' on all layouts.

## Complementary tools

In addition to these scripts, [@ejnaren](https://github.com/ejnaren)'s [Rhino Block Tools](https://github.com/ejnaren/rhinotools) contains useful scripts to handle blocks in Rhinoceros 3D. Scripts from this repository have been added here as simple python scripts (instead of a packaged plugin), in order to install them on both Mac and Windows Rhinoceros' versions.

### MakeUnique.py

Creates a new instance of the selected block(s).

### SelSameBlocks.py

Selects same instances of the selected block(s).

### ResetBlockScale.py

Resets the scale of the selected block(s), useful in the event of a non-uniform scaling action.