from setuptools import setup, find_packages

setup(
    name='split_downloader_peta',
    version='0.1.3',
    packages=find_packages(),
    description='A simple multi-threaded download manager',
    author='Manoj Kumar Reddy Peta',
    author_email='manojpeta30@gmail.com',
    entry_points={
        'console_scripts': [
            'split_downloader_peta=split_downloader.code:main',
        ],
    },
    install_requires=[
        'requests', 
        'tqdm',
        'rich',
    ],
    python_requires='>=3.6',
)
