from setuptools import setup

setup(
    name = 'jiongtu',
    packages = ['jiongtu'],
    version = '0.1.0',
    description = '囧',
    author = 'peluche',
    author_email = '',
    url = 'https://github.com/peluche/jiongtu',
    download_url = 'https://github.com/peluche/jiongtu/tarball/0.1',
    install_requires = ['flask'],
    data_files = [
        ('jiongtu/static', [
            'jiongtu/static/favicon.ico',
            'jiongtu/static/index.html',
            'jiongtu/static/main.js'
        ])
    ]
    keywords = [],
    classifiers = [])
