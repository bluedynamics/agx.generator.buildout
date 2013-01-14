import agx.generator.buildout
from zope.interface import implementer
from agx.core.interfaces import IProfileLocation


@implementer(IProfileLocation)
class ProfileLocation(object):
    name = u'buildout.profile.uml'
    package = agx.generator.buildout
