# -*- coding: utf-8 -*-
import plone_self_contained


def register():
    """Register this generator.
    """
    import agx.generator.buildout
    from agx.core.config import register_generator
    register_generator(agx.generator.buildout)
