#!/usr/bin/env python
"""print travis crons"""
import columnate
import travis_cron
import click

MODULE_NAME = "travis_cron.crons"
PROG_NAME = 'python -m %s' % MODULE_NAME
USAGE = 'python -m %s repo' % MODULE_NAME


@click.command()
@click.argument('repo', required=True)
def _cli(repo):
    crons = travis_cron.crons(repo)
    matrix = []
    if crons:
        for cron in crons:
            always = "always" if cron["always"] else ""
            row = [cron["id"], cron["branch"], cron["interval"], always]
            matrix.append(row)
        print(columnate.lists(matrix))


if __name__ == '__main__':
    _cli(prog_name=PROG_NAME)
