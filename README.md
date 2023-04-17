# 3D Procedural World Generation (2D View)

## Info:

While the view is a 2D birds eye view, all of the logic incorporates 3D.
Some tweaking of the code will allow you to break blocks, letting you to see the layers underneath.
The current code draws the top layer of the chunks.

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

Then run `main.py` and use the arrow keys to move the camera around.
You should see the chunks around you being randomly genereated, then unloaded once you go far enough away.

![Preview](https://user-images.githubusercontent.com/60083582/232429063-61203138-09ec-405c-9c43-ca257e86f094.png)
![Preview2](https://user-images.githubusercontent.com/60083582/232429324-36722c9d-e182-4e7f-8f4a-102a259a0183.png)
