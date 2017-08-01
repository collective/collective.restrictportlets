# -*- coding: utf-8 -*-
from plone import api


def getAddablePortletTypes(self):
    result = self._old_getAddablePortletTypes()
    if 'Manager' not in api.user.get_roles():
        # Hardcoded for now.
        result = [p for p in result if p.addview not in (
            'portlets.Login', 'portlets.Classic')]
    return result
