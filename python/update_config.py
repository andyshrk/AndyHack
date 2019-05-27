#!/usr/bin/env python2

import glob
import os
import optparse
import sys

def get_matched_defconfig(line):
    """Get the defconfig files that match a pattern

    Args:
        line: Path or filename to match, e.g. 'configs/snow_defconfig' or
            'k2*_defconfig'. If no directory is provided, 'configs/' is
            prepended

    Returns:
        a list of matching defconfig files
    """
    dirname = os.path.dirname(line)
    if dirname:
        pattern = line
    else:
        pattern = os.path.join('configs', line)
    return glob.glob(pattern) + glob.glob(pattern + '_defconfig')

def get_matched_defconfigs(defconfigs_file):
    """Get all the defconfig files that match the patterns in a file.

    Args:
        defconfigs_file: File containing a list of defconfigs to process, or
            '-' to read the list from stdin

    Returns:
        A list of paths to defconfig files, with no duplicates
    """
    defconfigs = []
    if defconfigs_file == '-':
        fd = sys.stdin
        defconfigs_file = 'stdin'
    else:
        fd = open(defconfigs_file)
    for i, line in enumerate(fd):
        line = line.strip()
        if not line:
            continue # skip blank lines silently
        if ' ' in line:
            line = line.split(' ')[0]  # handle 'git log' input
        matched = get_matched_defconfig(line)
        if not matched:
            print >> sys.stderr, "warning: %s:%d: no defconfig matched '%s'" % \
                                                 (defconfigs_file, i + 1, line)

        defconfigs += matched

    # use set() to drop multiple matching
    return [ defconfig[len('configs') + 1:]  for defconfig in set(defconfigs) ]

def update_defconfig(defconfig):
    cmd = 'make ' + defconfig
    os.system(cmd);
    os.system('make CROSS_COMPILE=powerpc-linux-gnu- savedefconfig')
    cmd = 'cp defconfig ' + 'configs/' + defconfig
    os.system(cmd)


def main():
    parser = optparse.OptionParser()
    parser.add_option('-d', '--defconfigs', type='string',
                      help='a file containing a list of defconfigs to move, '
                      "one per line (for example 'snow_defconfig') "
                      "or '-' to read from stdin")


    (options, configs) = parser.parse_args()

    defconfigs = get_matched_defconfigs(options.defconfigs)
    for defconfig in defconfigs:
        update_defconfig(defconfig)

if __name__ == '__main__':
        main()
