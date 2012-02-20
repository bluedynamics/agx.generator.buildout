import agx.generator.buildout
from zope.interface import implements
from agx.core.interfaces import IProfileLocation


class ProfileLocation(object):
    implements(IProfileLocation)
    name = u'buildout.profile.uml'
    package = agx.generator.buildout