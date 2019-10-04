from model_mommy.recipe import Recipe
from atelier.models import Fabric

fabric = Recipe(
    Fabric,
    name='Velvet',
    group='GR2',
    complexity_factor=3,
)
