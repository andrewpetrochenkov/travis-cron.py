#!/usr/bin/env python
"""delete travis crons by id"""
import travis_cron
import click

MODULE_NAME = "travis_cron.delete"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s repo cron_id ...' % MODULE_NAME


@click.command()
@click.argument('repo', required=True)
@click.argument('cron_id', nargs=-1, required=True)
def _cli(repo, cron_ids):
    for cron_id in cron_ids:
        travis_cron.delete(cron_id)


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
