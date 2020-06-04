# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import sys
import time

import mcpi
import mcpi.block

from mcthings.server import Server
from mcthings.sphere import Sphere
from mcthings.world import World

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711

MAX_RADIUS = 10  # 9 and 10 show flickering during building


def main():
    try:
        World.connect(Server(MC_SEVER_HOST, MC_SEVER_PORT))
        pos = World.server.entity.getTilePos(World.server.getPlayerEntityId(BUILDER_NAME))
        World.server.postToChat("Animating a Sphere")
        pos.x += 20

        s = Sphere(pos)
        s.radius = 0

        while s.radius < MAX_RADIUS:
            time.sleep(1)

            # Quicker remove of the Sphere based on its bounding box
            box_min, box_max = s.find_bounding_box()
            if box_min and box_max:
                World.server.setBlocks(box_min.x, box_min.y, box_min.z,
                                       box_max.x, box_max.y, box_max.z,
                                       mcpi.block.AIR)
            # unbuild is slower but more accurate
            # s.unbuild()

            s.radius += 1
            World.server.postToChat("Sphere radius " + str(s.radius))
            s.build()

    except mcpi.connection.RequestError:
        logging.error("Can't connect to Minecraft server " + MC_SEVER_HOST)
        sys.exit(1)


if __name__ == "__main__":
    main()
