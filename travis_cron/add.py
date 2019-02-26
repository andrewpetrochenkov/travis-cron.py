#!/usr/bin/env python
"""add travis cron"""
import travis_cron
import click

MODULE_NAME = "travis_cron.add"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s repo [branch] [interval] [always]' % MODULE_NAME


@click.command()
@click.argument('repo', required=True)
@click.argument('branch', default="master", required=False)
@click.argument('interval', default="monthly", required=False)
@click.argument('always', default=True, required=False)
def _cli(repo, branch, interval, always):
    always = True
    if always == ["false", "skip", "no", "0"]:
        always = False
    travis_cron.add(repo, branch, interval, always)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
