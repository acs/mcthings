from mcpi.vec3 import Vec3

import pandas as pd

from .thing import Thing


class CsvPoints(Thing):
    """
    The format of the CSV file must be:
    Level,X,Z,Y
    """
    file_path = None
    """ Path to the CSV file with the points to build"""
    level = "0"
    """ Which level to read """

    def find_next_blocks(self, points):
        """
        Find the next blocks that can be drawn together using setBlocks

        :param points: data for the next points to draw
        :return:
        """

    def build(self):
        # Read the CSV file
        if not self.file_path:
            RuntimeError("Missing file_path param")

        # First approach: put a block in each position. Try to detect blocks that are groups in order
        # to build them using setBlocks

        # In order to explore the data pandas helps with group by and others operations
        df = pd.read_csv(self.file_path, delimiter=",")
        # Work only with Level 0
        df0 = df[df['Level'].eq(0)]
        # Drop Level column
        df0.drop('Level', axis=1, inplace=True)
