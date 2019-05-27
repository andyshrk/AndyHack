#!/usr/bin/env python2
import glob
import os
import optparse
import subprocess
import sys

AUTO_CONF_PATH = 'include/config/auto.conf'
SPL_CONF_PATH = 'spl/include/autoconf.mk'

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

def add_one_config(defconfig, val):
    defconfig_file = 'configs/' + defconfig
    text_config = 'CONFIG_SPL_RELOC_TEXT_BASE=' + val + '\n'
    with open(defconfig_file, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write('# CONFIG_SPL_SKIP_RELOCATE is not set\n' + text_config + content)

def calculate_ref_plus_value(line):
    """calculate CONFIG_SYS_INIT_L2_END="(CONFIG_SYS_INIT_L2_ADDR + CONFIG_SYS_L2_SIZE)"
       line = "(CONFIG_SYS_INIT_L2_ADDR + CONFIG_SYS_L2_SIZE)"
    """
    config, ref = line.split('=')
    ref = ref.rstrip()
    ref = ref.strip('"()"')
    value1, value2 = ref.split('+')
    cmd = 'rg ' + value1 + ' ' + SPL_CONF_PATH
    os.system(cmd)
    cmd = 'rg ' + value2 + ' ' + SPL_CONF_PATH
    os.system(cmd)
    value1 = value1.strip()
    value2 = value2.strip()
    with open(SPL_CONF_PATH) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line.startswith(value1 + '='):
            value1 = line.split('=')[1]
            value1 = value1.strip()
    for i, line in enumerate(lines):
        if line.startswith(value2 + '='):
            value2 = line.split('=')[1]
            value2 = value2.strip()
            value2 = value2.strip('"()"')
    print "value1 + value2 = %s + %s" % (value1, value2)
    print '--0x%x--' % (eval(value1) + eval(value2))
    return (eval(value1) + eval(value2))

def calculate_ref_config_value(config):
    """config = CONFIG_SYS_INIT_L2_END - 0x2000
    """
    value1, value2 = config.split('-')
    value1 = value1.strip()
    value2 = value2.strip()
    key_words = value1 + '='
    cmd = 'rg ' + key_words + ' ' + SPL_CONF_PATH
    os.system(cmd)
    with open(SPL_CONF_PATH) as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith(key_words):
            value1 = calculate_ref_plus_value(line)
            #add_one_config(defconfig)
            break
    else:
        print '%s not used' % config
    return value1 - eval(value2)

def calculate_config_value(config_line):
    print 'calculate %s' % config_line
    config, value = config_line.split('=')
    value = value.strip()

    if value.startswith('"'):
        value = calculate_ref_config_value(value.strip('"()'))
    else:
        value = eval(value)
    return    str(hex(value))

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

    config = 'CONFIG_SPL_RELOC_TEXT_BASE'
    start = config + '='
    with open(SPL_CONF_PATH) as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith(start):
            val = calculate_config_value(line)
            add_one_config(defconfig, val)
            break
    else:
        print '%s not used' % config


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
