# -*- coding: utf-8 -*-
def getAddablePortletTypes(self):
    # Show just a few portlets, to check that our patch works.
    return self._old_getAddablePortletTypes()[:4]
