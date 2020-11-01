"""A Python Animation Library"""

# Rendering
from .rendering.render_config import RenderConfig
from .rendering.renderer import Renderer
from .rendering.cairo_renderer import CairoRenderer

# Writing
from .writing.writer import Writer
from .writing.ffmpeg_writer import FFMPEGWriter

# Animation
from .animation.animation import Animation
from .animation.timeline import Timeline
from .animation.easings import Linear, linear, Exponential, exponential, Quadratic, Cubic, Quartic, Quintic

# Entities
from .entities.entity import Entity
from .entities.scene import Scene
from .entities.primitive_entities import Rectangle