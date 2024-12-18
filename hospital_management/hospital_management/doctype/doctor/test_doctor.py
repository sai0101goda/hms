# Copyright (c) 2024, gopichand and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record depdendencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestDoctor(UnitTestCase):
	"""
	Unit tests for Doctor.
	Use this class for testing individual functions and methods.
	"""

	pass


class IntegrationTestDoctor(IntegrationTestCase):
	"""
	Integration tests for Doctor.
	Use this class for testing interactions between multiple components.
	"""

	pass
