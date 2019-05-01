#!/usr/bin/env python2
import glob
import os
import optparse
import subprocess
import sys

AUTO_CONF_PATH = 'include/config/auto.conf'

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

def do_defconfig(defconfig):
    """Run 'make <board>_defconfig' to create the .config file."""

    cmd = ['make']
    cmd += [defconfig]
    print 'run cmd %s' %  cmd
    exit_code = subprocess.call(cmd)
    if exit_code != 0:
        print >> sys.stderr, "Error #%d when calling: %s" % (exit_code, " ".join(cmd))

    ccmd = ['make CROSS_COMPILE=powerpc-linux-gnu- KCONFIG_IGNORE_DUPLICATES=1 include/config/auto.conf']
    #cmd += ['KCONFIG_IGNORE_DUPLICATES=1']
    #cmd += ['include/config/auto.conf']
    print 'run cmd %s' %  ccmd
    #exit_code = subprocess.call(ccmd)
    #if exit_code != 0:
     #   print >> sys.stderr, "Error #%d when calling: %s" % (exit_code, " ".join(ccmd))
    os.system('make CROSS_COMPILE=powerpc-linux-gnu- KCONFIG_IGNORE_DUPLICATES=1 include/config/auto.conf')
    os.system('rg SPL_RELOC_TEXT_BASE spl/')

def main():
    parser = optparse.OptionParser()
    parser.add_option('-d', '--defconfigs', type='string',
                      help='a file containing a list of defconfigs to move, '
                      "one per line (for example 'snow_defconfig') "
                      "or '-' to read from stdin")


    (options, configs) = parser.parse_args()

    # prefix the option name with CONFIG_ if missing
    configs = [ config if config.startswith('CONFIG_') else 'CONFIG_' + config
                for config in configs ]

    defconfigs = get_matched_defconfigs(options.defconfigs)
    for defconfig in defconfigs:
        do_defconfig(defconfig)

if __name__ == '__main__':
    main()
