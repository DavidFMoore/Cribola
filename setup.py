import glob

__version__='0.1.0'

setup_args = {
        'name': 'Cribola',
        'author': 'David F. Moore',
        'author_email': 'damo@sas.upenn.edu',
        'license': 'GPL',
        'packages': ['Cribola'],
        'package_dir': {'Cribola': 'src'},
        'scripts': glob.glob('scripts/*'),
        'version': __version__,
        }

if __name__ == "__main__":
    from distutils.core import setup
    apply(setup, (), setup_args)
