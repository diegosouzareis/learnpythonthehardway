try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'descricao': 'Meu Projeto',
    'autor': 'seuNome',
    'url': 'URL',
    'download_url': 'Onde faco o download',
    'autor_email': 'meuemail@gmail.com',
    'versao': '0.1',
    'install_requires': ['nose'],
    'pacotes': ['ex49'],
    'scripts': [],
    'nome': 'ex49'
}

setup(**config)
