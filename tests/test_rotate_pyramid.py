#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcpi.vec3 import Vec3
import mcpi.block

from mcthings.blocks import Blocks
from mcthings.collage import Collage
from mcthings.pyramid import Pyramid
from mcthings.world import World
from tests.base import TestBaseThing


class TestRotateBlock(TestBaseThing):
    """ Test to rotate Pyramids """

    def test_build(self):
        World.server.postToChat("Rotating pyramids")

        pos = self.pos

        pos.x += 3
        pyr = Pyramid(pos)
        pyr.height = 3
        pyr.build()
        pyr._block_empty = mcpi.block.BEDROCK  # For debugging
        pyr.rotate(90)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
