# coding=utf-8
# Copyright 2017 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

from pants.task.task import Task
from pants.contrib.buildrefactor.buildozer import Buildozer


class Peek(Task):
  """Peek a build file for a specified target

    line-number: optional flag to print the starting and ending line numbers of the target

    Example:
      $./pants peek --line-number testprojects/tests/java/org/pantsbuild/testproject/dummies:passing_target
  """

  @classmethod
  def register_options(cls, register):
    super(Peek, cls).register_options(register)

    register('--line-number', help='Prints the starting line number of the named target.', type=bool, default=False)

  def __init__(self, *args, **kwargs):
    super(Peek, self).__init__(*args, **kwargs)

    self.options = self.get_options()

  def execute(self):
    self.print_name()

  def print_name(self):
    for root in self.context.target_roots:
      address_spec = root.address.spec

    print('\n')
    if self.options.line_number:
      print('\n\'{}\' starts on line number:'.format(root.name))
      Buildozer.execute_binary('print startline', address_spec, suppress_warnings=True)
      print('\n\'{}\' ends on line number:'.format(root.name))
      Buildozer.execute_binary('print endline', address_spec, suppress_warnings=True)
    else:
      Buildozer.execute_binary('print name', address_spec, suppress_warnings=True)
      print('Target found in BUILD file.')
