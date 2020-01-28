from pathlib import Path
from setuptools import setup

try:
    # pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # pip <= 9.0.3
    from pip.req import parse_requirements

def from_here(relative_path):
    return Path(__file__).resolve().parent.joinpath(relative_path)

install_requires = [
    'pywin32',
    'setuptools',
    'Pillow',
]

setup(
    name='win10toast',
    version='0.9',
    install_requires=install_requires,
    packages=['win10toast'],
    license='MIT',
    url='https://github.com/nuno-andre/Windows-10-Toast-Notifications',
    download_url='https://github.com/nuno-andre/Windows-10-Toast-Notifications/archive/master.zip',
    description=(
        'An easy-to-use Python library for displaying '
        'Windows 10 Toast Notifications'
    ),
    include_package_data=True,
    package_data={
        '': ['*.txt'],
        'win10toast': ['data/*.ico'],
    },
    long_description=from_here('README.md').read_text(),
    long_description_content_type='text/markdown',
    author='Jithu R Jacob',
    author_email='jithurjacob@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Operating System :: Microsoft',
        'Environment :: Win32 (MS Windows)',
        'License :: OSI Approved :: MIT License',
    ],
)
