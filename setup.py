from setuptools import setup, find_packages

setup(
    name='loadercs2',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'pyqt5',
    ],
    entry_points={
        'console_scripts': [
            'my_python_project = my_python_project.main:main',
        ],
    },
    author='dark666',
    author_email='your.email@example.com',
    description='A description of your project',
    license='MIT',
    keywords='python project example',
    url='http://github.com/yourusername/my_python_project'
)
