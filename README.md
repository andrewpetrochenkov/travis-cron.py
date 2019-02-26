[![](https://img.shields.io/pypi/pyversions/travis-cron.svg?longCache=True)](https://pypi.org/project/travis-cron/)
[![](https://img.shields.io/pypi/v/travis-cron.svg?maxAge=3600)](https://pypi.org/project/travis-cron/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/travis-cron.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/travis-cron.py/)

#### Install
```bash
$ [sudo] pip install travis-cron
```

#### Functions
function|`__doc__`
-|-
`travis_cron.add(repo, branch='master', interval='monthly', always=True)`|add cron job
`travis_cron.clear(repo)`|clear all crons
`travis_cron.crons(repo)`|return list of crons
`travis_cron.delete(repo, cron_id)`|delete cron by id

#### CLI
usage|`__doc__`
-|-
`python -m travis_cron.add repo [branch] [interval] [always]`|add travis cron
`python -m travis_cron.clear repo`|clear all travis cron jobs
`python -m travis_cron.crons repo`|print travis crons
`python -m travis_cron.delete repo cron_id ...`|delete travis crons by id

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>