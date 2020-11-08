"""Some default animation shorthands"""

from .animation import Animation

from ..entities.vector_entity import VectorEntity

class Wait(Animation):
    def __init__(self, duration=1000):
        super().__init__(duration=duration)

class Morph(Animation):
    def __init__(self, from_entity : VectorEntity, to_entity : VectorEntity, *args, **kwargs):
        if not issubclass(from_entity.__class__, VectorEntity):
            raise NotImplementedError(f"Cannot morph from '{from_entity.__class__.__name__}' (A non-vector-entity).")

        if not issubclass(to_entity.__class__, VectorEntity):
            raise NotImplementedError(f"Cannot morph to '{to_entity.__class__.__name__}' (A non-vector-entity).")

        kwargs["target"] = from_entity
        kwargs["x"] = to_entity.x
        kwargs["y"] = to_entity.y
        kwargs["scale"] = to_entity.scale
        kwargs["rotation"] = to_entity.rotation
        kwargs["color"] = to_entity.color
        kwargs["points"] = to_entity.points
        super().__init__(*args, **kwargs)

        self.from_entity = from_entity
        self.to_entity = to_entity