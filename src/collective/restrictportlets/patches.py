# -*- coding: utf-8 -*-
from collective.restrictportlets.interfaces import ISettings
from plone import api


def getAddablePortletTypes(self):
    result = self._old_getAddablePortletTypes()
    if 'Manager' not in api.user.get_roles():
        restricted = api.portal.get_registry_record(
            name='restricted', interface=ISettings
        )
        result = [p for p in result if p.addview not in restricted]
    return result
