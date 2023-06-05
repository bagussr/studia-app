import random
from app.module import BaseModel, BaseSettings, Any


class Base(BaseSettings):
    default_bg_class: str


class DesignSchema(BaseModel):
    name: str
    color_hex: str
    image: Any


design_list = [
    DesignSchema(color_hex="#77BBE2", image=Base().default_bg_class, name="malibu"),
    DesignSchema(color_hex="#43A6C3", image=Base().default_bg_class, name="mistyc blue"),
    DesignSchema(color_hex="#D3E277", image=Base().default_bg_class, name="mindaro"),
    DesignSchema(color_hex="#9977E2", image=Base().default_bg_class, name="matt purple"),
    DesignSchema(color_hex="#E277B1", image=Base().default_bg_class, name="mangala pink"),
    DesignSchema(color_hex="#E29E77", image=Base().default_bg_class, name="les demoiselles d'avignon"),
    DesignSchema(color_hex="#FCC2D0", image=Base().default_bg_class, name="pink"),
    DesignSchema(color_hex="#FF4031", image=Base().default_bg_class, name="hotspot"),
]


def get_design() -> DesignSchema:
    return random.choice(design_list)
