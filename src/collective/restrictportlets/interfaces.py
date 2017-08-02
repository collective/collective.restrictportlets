# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from collective.restrictportlets import _
from plone import api
from plone.portlets.interfaces import IPortletType
from zope import schema
from zope.component import getUtilitiesFor
from zope.interface import implementer
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ICollectiveRestrictportletsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


@implementer(schema.interfaces.IVocabularyFactory)
class PortletTypesVocabulary(object):

    def __call__(self, context):
        # Get all portlets, for all portlet manager interfaces.
        portlets = [
            schema.vocabulary.SimpleVocabulary.createTerm(
                portlet.addview,  # value
                portlet.addview,  # token
                api.portal.translate(portlet.title)  # title
            ) for (name, portlet)
            in getUtilitiesFor(IPortletType)]
        return schema.vocabulary.SimpleVocabulary(portlets)


PortletTypesVocabularyFactory = PortletTypesVocabulary()


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
        default=['portlets.Classic', 'portlets.Login'],
    )
