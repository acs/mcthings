import sys

import mcpi.block
import mcpi.minecraft
from mcpi.vec3 import Vec3

from mcthings.pyramid import Pyramid
from mcthings.server import Server

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        server = Server(MC_SEVER_HOST, MC_SEVER_PORT)

        server.mc.postToChat("Building a pyramid")
        pos = server.mc.entity.getTilePos(server.mc.getPlayerEntityId(BUILDER_NAME))

        pyramid = Pyramid(pos)
        pyramid.block = mcpi.block.SAND
        pyramid.build()

        pyramid = Pyramid(pyramid.end_position)
        pyramid.block = mcpi.block.BEDROCK
        pyramid.height = 2
        pyramid.build()

        # Let's move the last pyramid to the ground
        pyramid.move(Vec3(pyramid.position.x, 0, pyramid.position.z))

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
