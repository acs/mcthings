import sys

import mcpi.block
import mcpi.minecraft


from mcthings.block import Block
from mcthings.server import Server

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    blocks_number = 5

    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building lines of blocks")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))

        # Creamos una línea en x crecientes
        block_pos = mcpi.vec3.Vec3(pos.x+1, pos.y, pos.z)
        for x in range(0, blocks_number):
            block_pos.x += 1
            Block(block_pos).build()

        # Creamos una línea en x decrecientes
        block_pos = mcpi.vec3.Vec3(pos.x+1, pos.y, pos.z)
        for x in range(1, blocks_number):
            block_pos.x -= 1
            Block(block_pos).build()

        # Creamos una línea en y crecientes
        block_pos = mcpi.vec3.Vec3(pos.x+1, pos.y, pos.z)
        for y in range(1, blocks_number):
            block_pos.y += 1
            Block(block_pos).build()

        # Creamos una línea en y decrecientes
        block_pos = mcpi.vec3.Vec3(pos.x+1, pos.y, pos.z)
        for y in range(1, blocks_number):
            block_pos.y -= 1
            Block(block_pos).build()

        # Creamos una línea en z crecientes
        block_pos = mcpi.vec3.Vec3(pos.x+1, pos.y, pos.z)
        for z in range(1, blocks_number):
            block_pos.z += 1
            Block(block_pos).build()

        # Creamos una línea en z decrecientes
        block_pos = mcpi.vec3.Vec3(pos.x+1, pos.y, pos.z)
        for z in range(1, blocks_number):
            block_pos.z -= 1
            Block(block_pos).build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
