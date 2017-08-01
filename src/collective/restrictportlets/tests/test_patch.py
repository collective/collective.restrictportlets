# -*- coding: utf-8 -*-
from collective.restrictportlets.interfaces import ISettings
from collective.restrictportlets.testing import COLLECTIVE_RESTRICTPORTLETS_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.portlets.interfaces import IPortletManager
from zope.component import getUtility

import unittest


class TestPatch(unittest.TestCase):
    """Test that our patch works."""

    layer = COLLECTIVE_RESTRICTPORTLETS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.manager = getUtility(IPortletManager, name='plone.leftcolumn')

    def test_manager_sees_all_portlets(self):
        # Portlets should remain addable if nothing has been changed.
        # We do not check them all, because the list may be different in
        # Plone 4 and 5.
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        addable = self.manager.getAddablePortletTypes()
        add_views = [p.addview for p in addable]
        self.assertIn('portlets.News', add_views)
        self.assertIn('portlets.Classic', add_views)
        self.assertIn('portlets.Login', add_views)
        self.assertIn('plone.portlet.static.Static', add_views)

    def test_member_sees_some_portlets(self):
        # Some portlets are no longer addable for non-managers.
        addable = self.manager.getAddablePortletTypes()
        add_views = [p.addview for p in addable]
        self.assertIn('portlets.News', add_views)
        self.assertNotIn('portlets.Classic', add_views)
        self.assertNotIn('portlets.Login', add_views)
        self.assertIn('plone.portlet.static.Static', add_views)

    def test_member_sees_different_portlets(self):
        # Test restricting different portlets than the default.
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.portal.set_registry_record(
            name='restricted', value=['portlets.News'],
            interface=ISettings
        )
        setRoles(self.portal, TEST_USER_ID, ['Member'])
        addable = self.manager.getAddablePortletTypes()
        add_views = [p.addview for p in addable]
        self.assertNotIn('portlets.News', add_views)
        self.assertIn('portlets.Classic', add_views)
        self.assertIn('portlets.Login', add_views)
        self.assertIn('plone.portlet.static.Static', add_views)
