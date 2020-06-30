import setuptools

setuptools.setup(
    name='travis-cron',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
