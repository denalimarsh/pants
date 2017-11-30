# coding=utf-8
# Copyright 2017 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

from pants.task.console_task import ConsoleTask
from pants.contrib.buildrefactor.buildozer import Buildozer


class PrintTarget(ConsoleTask):
  """Print's a specified target if found in the associated build file

    line-number: optional flag to print the starting and ending line numbers of the target

    Example:
      $./pants print-target --line-number testprojects/tests/java/org/pantsbuild/testproject/dummies:passing_target
  """

  @classmethod
  def register_options(cls, register):
    super(PrintTarget, cls).register_options(register)

    register('--line-number', help='Prints the starting line number of the named target.', type=bool, default=False)

  def __init__(self, *args, **kwargs):
    super(PrintTarget, self).__init__(*args, **kwargs)

    self.options = self.get_options()

  def console_output(self, targets):
    result = ''

    root = self.context.target_roots.pop()
    root_name = root.name
    address_spec = root.address.spec

    print('\'{}\' found in BUILD file.\n'.format(root_name))

    if self.options.line_number:
      print('Starts on line:'.format(root_name))
      Buildozer.execute_binary('print startline', address_spec, suppress_warnings=True)
      print('\nEnds on line:')
      Buildozer.execute_binary('print endline', address_spec, suppress_warnings=True)
      print()

    print('Target definiton:\n')
    Buildozer.execute_binary('print rule', address_spec, suppress_warnings=True)

    return result
