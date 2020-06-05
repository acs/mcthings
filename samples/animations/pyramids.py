# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import sys
import time

import mcpi
import mcpi.block
from mcpi.vec3 import Vec3

from mcthings.pyramid import Pyramid
from mcthings.server import Server
from mcthings.world import World

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711

MAX_HEIGHT = 10
WAIT_TIME = 1
MAX_FAR = 40
MOVE_STEP = 5


def clean_and_build(pyr):
    # Quicker remove of the Thing based on its bounding box
    # box_min, box_max = pyr.find_bounding_box()
    # if box_min and box_max:
    #     World.server.setBlocks(box_min.x, box_min.y, box_min.z,
    #                            box_max.x, box_max.y, box_max.z,
    #                            mcpi.block.AIR)
    # unbuild is slower but more accurate
    pyr.unbuild()

    World.server.postToChat("Pyramid height " + str(pyr.height) + str(pyr.position))
    pyr.build()


def grow_reduce(pyr):

    while pyr.height < MAX_HEIGHT:
        time.sleep(WAIT_TIME)
        pyr.height += 1
        clean_and_build(pyr)

    while pyr.height > 0:
        time.sleep(WAIT_TIME)
        pyr.height -= 1
        clean_and_build(pyr)


def far_near(pyr):

    init_pos = Vec3(pyr.position.x, pyr.position.y, pyr.position.z)

    while pyr.position.x < init_pos.x + MAX_FAR:
        time.sleep(WAIT_TIME)
        pyr.move(Vec3(pyr.position.x + MOVE_STEP, init_pos.y, init_pos.z))

    while pyr.position.x > init_pos.x:
        time.sleep(WAIT_TIME)
        pyr.move(Vec3(pyr.position.x - MOVE_STEP, init_pos.y, init_pos.z))


def rotate(pyr):

    pyr.build()
    for rotation in [90, 180, 270]:
        pyr.rotate(rotation)
        time.sleep(WAIT_TIME)


def main():
    try:
        World.connect(Server(MC_SEVER_HOST, MC_SEVER_PORT))
        pos = World.server.entity.getTilePos(World.server.getPlayerEntityId(BUILDER_NAME))
        World.server.postToChat("Animating a Pyramid")
        pos.x += 20

        pyr = Pyramid(pos)
        pyr.height = 5

        # grow_reduce(pyr)
        # far_near(pyr)
        rotate(pyr)

    except mcpi.connection.RequestError:
        logging.error("Can't connect to Minecraft server " + MC_SEVER_HOST)
        sys.exit(1)


if __name__ == "__main__":
    main()
