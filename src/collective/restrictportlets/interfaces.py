# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from collective.restrictportlets import _
from plone.portlets.interfaces import IPortletType
from zope import schema
from zope.component import getUtilitiesFor
from zope.interface import Interface, implementer, provider
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveRestrictportletsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


@provider(schema.interfaces.IBaseVocabulary)
def portlet_types_vocabulary(context):
    # The standard portlet managers check if a portlet is registered
    # for the manager interface.  For the vocabulary we do not want
    # this restriction.
    addable = [p.addview for p in getUtilitiesFor(IPortletType)]
    return schema.vocabulary.SimpleVocabulary.fromValues(addable)


class ISettings(Interface):
    """Settings for restricted portlets"""

    restricted = schema.List(
        title=_(u'Restricted portlets'),
        description=_(
            u'description_restricted_portlets',
            default=u'Select portlets that should only be '
                    u'available for Managers.'),
        value_type=schema.Choice(
            title=u'Portlet name',
            vocabulary='collective.restrictportlets.portlet_types',
        ),
        default=['portlets.Login', 'portlets.Classic'],
    )
