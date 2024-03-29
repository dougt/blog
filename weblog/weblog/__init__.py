__author__ = u'Henry Pr\u00EAcheur <henry@precheur.org>'
__version__ = '2.5'
__license__ = 'ISCL'

def main(args=None):
    import logging
    from optparse import OptionParser, SUPPRESS_HELP

    from publish import command_publish
    from date import command_date

    _COMMANDS = ('publish', 'date')

    parser = OptionParser(usage=('%%prog [option] command\n\nCommands:\n  ' +
                                 '\n  '.join(_COMMANDS)))
    parser.add_option("-s", "--source_dir", dest="source_dir",
                      default='',
                      help='The source directory where the blog posts are '
                      'located. [default: \'%default\']',
                      metavar="DIR")
    parser.add_option("-o", "--output_dir", dest="output_dir",
                      default='',
                      help='The directory where all the generated files are '
                      'written. If it does not exist it is created.'
                      '[default: \'%default\']',
                      metavar="DIR")
    parser.add_option('-c', '--conf', dest='configuration_file',
                      help='The configuration file to use. If the file is not '
                      'present in the current directory, the source directory '
                      'is searched.'
                      ' [default: \'%default\']',
                      metavar='FILE',
                      default='config.py')
    parser.add_option('-q', '--quiet',
                      dest='quiet', default=False, action='store_true',
                      help='Do not output anything except critical error '
                      'messages')
    parser.add_option('--debug',
                      dest='debug', default=False, action='store_true',
                      help=SUPPRESS_HELP)
    (options, args) = parser.parse_args(args)

    if options.debug:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(levelname)s %(message)s')
    elif options.quiet:
        logging.basicConfig(level=logging.ERROR,
                            format='%(message)s')
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(message)s')
    if not args:
        command = 'publish'
    else:
        command = args.pop(0)

    if command not in _COMMANDS:
        parser.error('invalid command \'%s\'' % command)
    elif command == 'publish':
        command_publish(args, options)
    elif command == 'date':
        command_date(args)
