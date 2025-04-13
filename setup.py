from setuptools import setup, find_packages

setup(
    name='igprint',
    version='0.1.0',
    description='Captura screenshots do feed do Instagram via browser automatizado.',
    author='Júlia Almeida',
    author_email='julia.almeida13k@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pyppeteer',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'igprint=igprint.cli:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ]
)
