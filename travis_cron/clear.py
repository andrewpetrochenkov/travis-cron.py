#!/usr/bin/env python
"""clear all travis cron jobs"""
import travis_env
import click

MODULE_NAME = "travis_cron.clear"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s repo' % MODULE_NAME


@click.command()
@click.argument('repo', required=True)
def _cli(repo):
    travis_env.clear(repo)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
