__all__ = ['add', 'clear', 'crons', 'delete']


import os
import travis_cron.api


def crons(repo):
    """return a list of crons"""
    ENDPOINT = os.getenv("TRAVIS_ENDPOINT", "https://api.travis-ci.org")
    url = "%s/repo/%s/crons" % (ENDPOINT, repo.replace("/", "%2F"))
    r = travis_cron.api.request("GET", url)
    crons = []
    for data in r.json()["crons"]:
        cron_id = data["id"]
        branch = data["branch"]["name"]
        interval = data["interval"]
        always = not data["dont_run_if_recent_build_exists"]
        cron = dict(id=cron_id, interval=interval,
                    branch=branch, always=always)
        crons.append(cron)
    return crons


def add(repo, branch="master", interval="monthly", always=True):
    """add cron job"""
    ENDPOINT = os.getenv("TRAVIS_ENDPOINT", "https://api.travis-ci.org")
    data = {
        "cron.interval": interval,
        "cron.branch": branch,
        "cron.dont_run_if_recent_build_exists": not always
    }
    url = "%s/repo/%s/branch/%s/cron" % (ENDPOINT,
                                         repo.replace("/", "%2F"), branch)
    r = travis_cron.api.request("POST", url, data)
    return r.json()


def delete(repo, cron_id):
    """delete cron by id"""
    ENDPOINT = os.getenv("TRAVIS_ENDPOINT", "https://api.travis-ci.org")
    url = "%s/cron/%s" % (ENDPOINT, cron_id)
    travis_cron.api.request("DELETE", url)


def clear(repo):
    """clear all crons"""
    for cron in crons(repo):
        delete(repo, cron["id"])
