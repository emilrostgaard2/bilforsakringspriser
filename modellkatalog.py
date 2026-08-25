# -*- coding: utf-8 -*-
"""Sammanslagen modellkatalog — enda källan för både generatorerna.

modellsidor.py bygger sidorna, generators.py bygger länkarna från
märkessidan. Båda måste se samma katalog, annars finns det sidor ingen
länkar till. Lägg nya märken i en egen fil och koppla in den här.
"""
from modeller import MODELLER as _M1
from modeller_2 import MODELLER_2 as _M2
from modeller_skoda import MODELLER_SKODA as _M3
from modeller_vw import MODELLER_VW as _M4
from modeller_4 import MODELLER_3 as _M5
from modeller_audi import MODELLER_AUDI as _M6

MODELLER = {**_M1, **_M2, **_M3, **_M4, **_M5, **_M6}
