#! /usr/bin/env python

""" Install/uninstall/update current pylint and its dependencies """

from __future__ import absolute_import, print_function, unicode_literals
import sys
import os
import errno
import subprocess


def checkout_url(pkgname):
    """ Return checkout URL for the package """
    co_url = 'https://bitbucket.org/logilab/' + pkgname
    return co_url


class PylintMaint(object):

    """ Class to maintain pylint sources """

    srcdir = '~/src/pylint'
    pkgnames = ['astroid', 'pylint']
    python = 'python'

    @classmethod
    def expand_srcdir(cls):
        """ Expand tilde in srcdir """
        cls.srcdir = os.path.expanduser(cls.srcdir)

    def usage(self):
        """ Print usage information and exit """
        commands = sorted([d.replace('do_', '', 1)
                           for d in dir(self) if d.startswith('do_')])
        print(
            "Usage: pylintmaint [ -2 | -3 | --python PYTHON ] [ COMMAND ]...")
        print('  -2                Use "python2"')
        print('  -3                Use "python3"')
        print('  --python PYTHON   Use specified Python executable')
        print("Commands:")
        for cmd in commands:
            run_func = getattr(self, 'do_' + cmd)
            print("  {0:10s} {1}".format(cmd, run_func.__doc__.strip()))
        sys.exit(1)

    def walk_dirs(self, cmd):
        """ Run command in the given directories """
        for subdir in self.dirs:
            subprocess.check_call(cmd, cwd=subdir)

    def do_build(self):
        """ Build packages from sources """
        self.walk_dirs([self.python, 'setup.py', 'build'])

    def do_clean(self):
        """ Remove files not under version control """
        self.walk_dirs(['hg', '--config', 'extensions.purge=', 'purge',
                        '--all'])

    def do_update(self):
        """ Update sources from repositories """
        self.walk_dirs(['hg', 'pull', '-u'])

    def do_checkout(self):
        """ Check out sources from repositories """
        try:
            os.makedirs(self.srcdir)
        except OSError as exc:
            if exc.errno == errno.EEXIST:
                pass
        for subdir in self.dirs:
            if not os.path.exists(subdir):
                pkgname = os.path.basename(subdir)
                subprocess.check_call(['hg', 'clone', checkout_url(pkgname),
                                       pkgname], cwd=self.srcdir)
            else:
                print('Already exists:', subdir)

    def do_develop(self):
        """ Install egg-links to the sources """
        self.do_uninstall()
        cmd = [self.python, 'setup.py']
        for subdir in self.dirs:
            cmd.append('develop')
            if not self.is_homebrew:
                cmd.append('--user')
            subprocess.check_call(cmd, cwd=subdir)

    def do_install(self):
        """ Install built packages """
        self.do_uninstall()
        cmd = [self.python, 'setup.py', 'install']
        if not self.is_homebrew:
            cmd.append('--user')
        self.walk_dirs(cmd)

    def do_uninstall(self):
        """ Uninstall packages or egg-links """
        for pkgname in reversed(self.pkgnames):
            subprocess.call([self.python, '-m', 'pip',
                             'uninstall', '-y', pkgname])

    def run_command(self, cmd):
        """ Run named command """
        try:
            run_func = getattr(self, 'do_' + cmd)
        except AttributeError:
            print("No such command:", cmd)
            self.usage()

        try:
            run_func()
        except subprocess.CalledProcessError:
            print("Error running command:", cmd)
            sys.exit(1)

    def check_homebrew(self):
        """ Check if Python is part of HomeBrew """
        try:
            ret = subprocess.check_output([self.python, '-c',
                                           r'import sys; print("\n".join(sys.path))'])
        except (subprocess.CalledProcessError, OSError):
            print('Python does not appear to be properly installed:', self.python)
            sys.exit(1)
        for line in ret.split('\n'):
            if '/Cellar/' in line:
                return True
        return False

    def __init__(self):
        """ Main function """
        #if os.geteuid() == 0:
         #   print("pylintmaint should not be run as root")
          #  sys.exit(1)

        if len(sys.argv) < 2:
            self.usage()

        # Skip executable name
        sys.argv.pop(0)

        self.python = 'python'
        if sys.argv[0] == '-2':
            sys.argv.pop(0)
            self.python = 'python2'
        elif sys.argv[0] == '-3':
            sys.argv.pop(0)
            self.python = 'python3'
        elif sys.argv[0] == '--python':
            sys.argv.pop(0)
            self.python = sys.argv.pop(0)

        self.is_homebrew = self.check_homebrew()

        self.expand_srcdir()
        self.dirs = [os.path.join(self.srcdir, d) for d in self.pkgnames]

        for cmd in sys.argv:
            self.run_command(cmd)


if __name__ == '__main__':
    PylintMaint()