# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from collective.restrictportlets.testing import COLLECTIVE_RESTRICTPORTLETS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.restrictportlets is properly installed."""

    layer = COLLECTIVE_RESTRICTPORTLETS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.restrictportlets is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.restrictportlets'))

    def test_browserlayer(self):
        """Test that ICollectiveRestrictportletsLayer is registered."""
        from collective.restrictportlets.interfaces import (
            ICollectiveRestrictportletsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveRestrictportletsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_RESTRICTPORTLETS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.restrictportlets'])

    def test_product_uninstalled(self):
        """Test if collective.restrictportlets is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.restrictportlets'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveRestrictportletsLayer is removed."""
        from collective.restrictportlets.interfaces import \
            ICollectiveRestrictportletsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
           ICollectiveRestrictportletsLayer,
           utils.registered_layers())
