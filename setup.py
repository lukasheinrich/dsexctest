from setuptools import setup, find_packages

setup(
    name='test2',
    version='0.0.0',    
    description='A example Python package',
    url='https://github.com/RasmusOrsoe/test2',
    author='Rasmus',
    author_email='none',
    license='BSD 2-clause',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=['pandas',
                      'numpy',
                      'matplotlib'                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)