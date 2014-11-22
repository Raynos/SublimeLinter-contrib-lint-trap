#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# regex below borrowed from https://github.com/roadhump/SublimeLinter-eslint
# and is MIT-licensed from roadhump.
# 
# Written by andrewdeandrade
# Copyright (c) 2014 andrewdeandrade
# 
# License: MIT
#

"""This module exports the LintTrap plugin class."""

from SublimeLinter.lint import Linter, util


class LintTrap(Linter):

    """Provides an interface to the lint-trap executable."""

    syntax = ('javascript', 'javascriptnext')
    cmd = ('lint-trap', '--reporter=compact', '-')
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.4.0'
    regex = (
        r'^.+?: line (?P<line>\d+), col (?P<col>\d+), '
        r'(?:(?P<error>Error)|(?P<warning>Warning)) - '
        r'(?P<message>.+)'
    )
    multiline = False
    line_col_base = (1, 0)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'
