# Authors: James Laidler <jlaidler@paypal.com>
# License: BSD 3 clause
import setuptools
from iguanas import __version__
# Get description from readme
with open('README.md', 'r') as fh:
    long_description = fh.read()
# Remove image at the top
long_description = f"#{long_description.split('#')[1]}"

setuptools.setup(
    name="iguanas",
    version=__version__,
    author="James Laidler",
    url="https://github.com/paypal/Iguanas",
    description="Rule generation, optimisation, filtering and scoring library",
    packages=setuptools.find_packages(exclude=['examples']),
    install_requires=['category-encoders==2.0.0', 'matplotlib==3.0.3',
                      'seaborn==0.9.0', 'numpy==1.19.4', 'pandas==1.1.4',
                      'hyperopt==0.2.5', 'joblib==0.16.0',
                      'scikit-learn==0.23.2', 'scipy==1.7.1'],
    extras_require={
        'dev': [
            'pytest==6.0.1', 'check-manifest==0.47', 'wheel==0.37.0',
            'twine==3.7.1', 'sphinx==4.3.1', 'numpydoc==1.1.0',
            'nbsphinx==0.8.7', 'pydata-sphinx-theme==0.7.2', 'nbmake==1.1',
            'pytest-cov==3.0.0'
        ],
        'spark': ['koalas==1.8.1', 'pyspark==3.1.2']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
