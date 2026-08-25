# -*- coding: utf-8 -*-
"""Sammanslagen modellkatalog — enda källan för både generatorerna.

modellsidor.py bygger sidorna, generators.py bygger länkarna från
märkessidan. Båda måste se samma katalog, annars finns det sidor ingen
länkar till. Lägg nya märken i en egen fil och koppla in den här.
"""
from modeller import MODELLER as _M1
from modeller_2 import MODELLER_2 as _M2

MODELLER = {**_M1, **_M2}
