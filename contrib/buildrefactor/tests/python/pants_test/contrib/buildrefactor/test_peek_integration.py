# coding=utf-8
# Copyright 2017 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

from pants_test.pants_run_integration_test import PantsRunIntegrationTest


class PeekIntegrationTest(PantsRunIntegrationTest):
  """Test Peek goal functionality

      $./pants test contrib/buildrefactor/tests/python/pants_test/contrib/buildrefactor:peek_integration
  """

  def test_print_name(self):
    peek_print_run = self.run_pants(['peek',
      'testprojects/tests/java/org/pantsbuild/testproject/buildrefactor/x:X'])

    self.assertIn('[peek]\n\nX\nTarget found in BUILD file.', peek_print_run.stdout_data)
    self.assertIn('SUCCESS', peek_print_run.stdout_data)

  def test_print_line_number(self):
    peek_line_number_run = self.run_pants(['peek',
      '--line-number',
      'testprojects/tests/java/org/pantsbuild/testproject/buildrefactor/x:X'])

    self.assertIn('[peek]\n\n\n\'X\' starts on line number:\n4', peek_line_number_run.stdout_data)
    self.assertIn('SUCCESS', peek_line_number_run.stdout_data)
