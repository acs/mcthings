#!/usr/bin/env python3

# Licensed under the terms of http://www.apache.org/licenses/LICENSE-2.0
# Author (©): Alvaro del Castillo

import logging
import unittest

from mcthings.block import Block
from mcthings.world import World
from integration.base import TestBaseThing


class TestScene(TestBaseThing):
    """Test Scene Thing"""

    def test_build(self):
        World.renderer.post_to_chat("Building a scene")

        pos = self.pos

        pos.x += 1
        block = Block(pos)
        block.build()

        pos.x += 2
        block = Block(pos)
        block.build()

        pos.y += 1
        World.first_scene().move(pos)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    unittest.main(warnings='ignore')
