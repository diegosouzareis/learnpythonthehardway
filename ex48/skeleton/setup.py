try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'descricao': 'Meu projeto',
    'autor': 'Meu Nome',
    'url': 'URL',
    'download_url': 'Onde faco o download',
    'autor_email': 'Meu email.',
    'versao': '0.1',
    'install_requires': ['nose'],
    'pacotes': ['NOME'],
    'scripts': [],
    'name': 'nomedoprojeto'
}

setup(**config)