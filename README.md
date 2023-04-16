# 3D Procedural World Generation (2D View)

## Requirements:

Use [pip](https://pypi.org/project/pip/) to install the following modules:

`pip install pygame`

`pip install GameMaker`

## How to Use:
Edit `camera.py` to your desired config values: 
- `POSITION` *Vector3*    : Starting position of camera in x,y,z format
- `RENDER_DISTANCE` *int* : Distance from camera to render chunks
- `UNLOAD_DISTANCE` *int* : Distance from camera to unload chunks
- `CHUNK_SIZE` *Vector3*  : Size of each chunk in x,y,z format
- `SHOW_GRID` *bool*      : Show outlines of each block
