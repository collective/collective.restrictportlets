# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from collective.restrictportlets import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveRestrictportletsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ISettings(Interface):
    """Settings for restricted portlets"""

    restricted = schema.List(
        title=_(u'Restricted portlets'),
        description=_(
            u'description_restricted_portlets',
            default=u'Select portlets that should only be '
                    u'available for Managers.'),
        value_type=schema.ASCIILine(title=u'Portlet name'),
        default=['portlets.Login', 'portlets.Classic'],
    )
