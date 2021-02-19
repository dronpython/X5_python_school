import argparse
import sys

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import get_formatter_by_name

from pytz import timezone
from datetime import datetime

from cowpy import cow


lexer = get_lexer_by_name('python', stripall=True)
formatter = get_formatter_by_name('terminal')


def create_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', title='Возможные команды',
                                       description='Команды, которые выступают в качестве первого аргумента')

    highlight_parser = subparsers.add_parser('highlight',
                                             help='Use this for highlight your code', add_help=True)
    highlight_parser.add_argument('code', help='Usage: highlight "code"')

    cowsay_parser = subparsers.add_parser('cowsay', help='Makes cow talk')
    cowsay_parser.add_argument('text', help='Usage: cowsay "text"')

    time_parser = subparsers.add_parser('time', help='To know how much time in some timezone')
    time_parser.add_argument('timezone', help='Usage: time "Europe/Amsterdam"')

    return parser


def run_highlight(namespace):

    print(highlight(namespace.code, lexer, formatter))


def run_cowsay(namespace):
    cheese = cow.Moose()
    msg = cheese.milk(namespace.text)
    print(msg)


def run_timezone(namespace):
    tz = timezone(namespace.timezone)
    loc_dt = datetime.now(tz).strftime('%H:%M:%S')
    print(loc_dt)


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.command == 'highlight':
        run_highlight(namespace)
    elif namespace.command == 'cowsay':
        run_cowsay(namespace)
    elif namespace.command == 'time':
        run_timezone(namespace)
    else:
        print('Empty input args')


if __name__ == '__main__':
    main()
