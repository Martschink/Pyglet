
"""EXT_visual_info
http://oss.sgi.com/projects/ogl-sample/registry/EXT/visual_info.txt
"""

import ctypes as _ctypes
from pyglet.GL import get_function as _get_function
from pyglet.GL import c_ptrdiff_t as _c_ptrdiff_t
GLX_X_VISUAL_TYPE_EXT = 0x22
GLX_TRANSPARENT_TYPE_EXT = 0x23
GLX_TRANSPARENT_INDEX_VALUE_EXT = 0x24
GLX_TRANSPARENT_RED_VALUE_EXT = 0x25
GLX_TRANSPARENT_GREEN_VALUE_EXT = 0x26
GLX_TRANSPARENT_BLUE_VALUE_EXT = 0x27
GLX_TRANSPARENT_ALPHA_VALUE_EXT = 0x28
GLX_NONE_EXT = 0x8000
GLX_TRUE_COLOR_EXT = 0x8002
GLX_DIRECT_COLOR_EXT = 0x8003
GLX_PSEUDO_COLOR_EXT = 0x8004
GLX_STATIC_COLOR_EXT = 0x8005
GLX_GRAY_SCALE_EXT = 0x8006
GLX_STATIC_GRAY_EXT = 0x8007
GLX_TRANSPARENT_RGB_EXT = 0x8008
GLX_TRANSPARENT_INDEX_EXT = 0x8009