# -*- coding: utf-8 -*-
import logging
from collections import deque

from pixsort.common import *
from pixsort.pixstamp import PixStamp


# ===========================================================
# GLOBAL VARIABLES
# ===========================================================
logger = logging.getLogger(ENV)


# ===========================================================
# CLASS IMPLEMENTATIONS
# ===========================================================
class PixStampGroup:
    """
    Pix stamp gorup
    """
    def __init__(self, fmt, stamp):
        self.fmt = fmt
        self.stamp = stamp
        self.paths = []

    def key(self):
        """
        Return stamp group key
        """
        return f"{self.fmt}/{self.stamp}"

    def __str__(self):
        return f"{self.fmt}/{self.stamp}: {self.paths}"


class PixStampGroupManager:
    """
    Manages pix stamp groups
    """
    def __init__(self):
        """
        Initialization
        """
        self.stamps = deque()
        self.map = {}

    def empty(self):
        """
        Check if list is empty or not
        """
        return True if (not self.stamps) else False

    def add(self, stamp, path) -> object:
        """
        add a stamp with path to the map. If duplicated, they are merged.
        """
        key = str(stamp)  # stamp key format is "fmt/stamp"

        if key not in self.map:
            logger.debug(f"Create a new stamp group: {key}")
            self.map[key] = PixStampGroup(stamp.fmt, stamp.stamp)
            self.stamps.append(self.map[key])

        self.map[key].paths.append(path)

    def pop(self):
        """
        Pop an pix stamp group.
        """
        psg = None

        if self.stamps:
            psg = self.stamps.popleft()
            self.map.pop(psg.key())

        return psg