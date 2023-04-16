import blocks
import camera

from vector import *

import GameMaker as gm
from GameMaker.Assets import Rectangle, Text

chunks = {}

window = gm.Window([1000,1000],"World Engine")

origin = Vector2(window.H_WIDTH,window.H_HEIGHT)

chunk_position = Vector2(camera.POSITION.x // camera.CHUNK_SIZE.x, camera.POSITION.z // camera.CHUNK_SIZE.z)

block_selected = Vector2(0,0)

player = Rectangle([0,0,10,10])

while window.RUNNING:

	camera.POSITION.x += round(int(window.get_key(gm.K_LEFT)) * (camera.POSITION.y * 1))
	camera.POSITION.x -= round(int(window.get_key(gm.K_RIGHT)) * (camera.POSITION.y * 1))

	camera.POSITION.y += round(int(window.get_key(gm.K_LSHIFT)) * (camera.POSITION.y * 0.01),2)
	camera.POSITION.y -= round(int(window.get_key(gm.K_SPACE)) * (camera.POSITION.y * 0.01),2)

	camera.POSITION.z -= round(int(window.get_key(gm.K_DOWN)) * (camera.POSITION.y * 1))
	camera.POSITION.z += round(int(window.get_key(gm.K_UP)) * (camera.POSITION.y * 1))

	rendered = []

	zoom = blocks.Block.scale(None,camera.POSITION.y)

	block_selected.x = (gm.Mouse.get_pos()[0] - window.H_WIDTH  - camera.POSITION.x) // zoom
	block_selected.y = (window.H_HEIGHT - gm.Mouse.get_pos()[1] + camera.POSITION.z) // zoom

	chunk_position.x = -int((camera.POSITION.x / zoom) // camera.CHUNK_SIZE.x) - 1
	chunk_position.y = -int((camera.POSITION.z / zoom) // camera.CHUNK_SIZE.z) - 1

	for x in range(chunk_position.x - camera.RENDER_DISTANCE, chunk_position.x + camera.RENDER_DISTANCE + 1):
		for y in range(chunk_position.y - camera.RENDER_DISTANCE, chunk_position.y + camera.RENDER_DISTANCE + 1):
			if str((x,y)) not in chunks.keys():
				chunks[str((x,y))] = blocks.Chunk(position = Vector2(x,y),default = blocks.Random)

	for chunk in chunks.values():
		if chunk_position.x + camera.UNLOAD_DISTANCE > chunk.position.x > chunk_position.x - camera.UNLOAD_DISTANCE:
			if chunk_position.y + camera.UNLOAD_DISTANCE > chunk.position.y > chunk_position.y - camera.UNLOAD_DISTANCE:
				rendered += [block.render(camera.POSITION + origin + chunk.position * camera.CHUNK_SIZE.x * zoom) for block in chunk.layer(0)]	

	player.w = zoom
	player.h = zoom

	player.x = origin.x - player.w / 2
	player.y = origin.y - player.h / 2

	optimised = [block for block in rendered if (block.x + block.w > 0 and block.x < window.WIDTH) and (block.y + block.h > 0 and block.y < window.HEIGHT)]

	window.draw(optimised,gm.BACKGROUND)

	window.draw([player],gm.FOREGROUND)

	window.draw([
		Text("Chunk Size: {}x{}".format(camera.CHUNK_SIZE.x, camera.CHUNK_SIZE.z), [10,10], font_size = 25),
		Text(f"Render Distance: {camera.RENDER_DISTANCE}", [10,40], font_size = 25),
		Text(f"Unload Distance: {camera.UNLOAD_DISTANCE}", [10,70], font_size = 25),
		Text(f"Chunks Loaded: {len(chunks)}", [10,100], font_size = 25),
		Text(f"Blocks Cached: {len(chunks) * camera.CHUNK_SIZE.x * camera.CHUNK_SIZE.z}", [10,130], font_size = 25),
		Text(f"Blocks Loaded: {len(rendered)}", [10,160], font_size = 25),
		Text(f"Blocks Drawn: {len(optimised)}", [10,190], font_size = 25),
		Text("Camera:   {}  {}  {}".format(*camera.POSITION.format()), [10,220], font_size = 25),
		Text("Chunk Position:   {}  {}".format(*chunk_position.format()), [10,250], font_size = 25),
		Text("Block Selected:   {}  {}".format(*block_selected.format()), [10,280], font_size = 25),
	],gm.GUI)

	window.update()