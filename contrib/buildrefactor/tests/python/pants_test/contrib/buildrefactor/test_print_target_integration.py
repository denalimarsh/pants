# coding=utf-8
# Copyright 2017 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

from pants_test.pants_run_integration_test import PantsRunIntegrationTest


class PrintTargetIntegrationTest(PantsRunIntegrationTest):
  """Test Peek goal functionality

      $./pants test contrib/buildrefactor/tests/python/pants_test/contrib/buildrefactor:print_target_integration
  """

  def test_print_name(self):
    print_target_print_run = self.run_pants(['print-target',
      'testprojects/tests/java/org/pantsbuild/testproject/buildrefactor/x:X'])

    self.assertIn('Target definiton:\n\njava_library(\n    name = "X",\n)\n', print_target_print_run.stdout_data)

  def test_print_line_number(self):
    print_target_line_number_run = self.run_pants(['print-target',
      '--line-number',
      'testprojects/tests/java/org/pantsbuild/testproject/buildrefactor/x:X'])

    self.assertIn('Starts on line:\n4\n\nEnds on line:\n6', print_target_line_number_run.stdout_data)
