"""A Python Animation Library"""

# Rendering
from .rendering.render_config import RenderConfig
from .rendering.renderer import Renderer
from .rendering.cairo_renderer import CairoRenderer

# Writing
from .writing.writer import Writer
from .writing.ffmpeg_writer import FFMPEGWriter
from .writing.image_writer import ImageWriter, PNGWriter, JPEGWriter, ScreenshotWriter

# Animation
from .animation.animation import Animation
from .animation.timeline import Timeline
from .animation.easings import linear, smooth, smoothSteep, smoothSteeper, fastSmoothInSlowSmoothOut, slowSmoothInFastSmoothOut

# Animations
from .animation.animations import Wait

# Entities
from .entities.entity import Entity
from .entities.vector_entity import VectorEntity
from .entities.hacky_svg_base_entity import HackySvgBaseEntity

from .entities.scene import Scene
from .entities.primitive_entities import Arc, Circle, Text

# Constants
from .constants import *