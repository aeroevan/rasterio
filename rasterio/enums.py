
from enum import Enum, IntEnum


class ColorInterp(IntEnum):
    undefined=0
    grey=1
    gray=1
    palette=2
    red=3
    green=4
    blue=5
    alpha=6
    hue=7
    saturation=8
    lightness=9
    cyan=10
    magenta=11
    yellow=12
    black=13


class Resampling(Enum):
    nearest='NEAREST'
    gauss='GAUSS'
    cubic='CUBIC'
    average='AVERAGE',
    mode='MODE'
    average_magphase='AVERAGE_MAGPHASE'
    none='NONE'
