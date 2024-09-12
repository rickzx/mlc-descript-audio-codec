from setuptools import setup, find_packages

setup(
    name='mlc_dac',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='Descript Audio Codec with ML Compilation',
    author='Rick Zhou',
    author_email='rickzhoucmu@gmail.com',
    url='https://github.com/rickzx/mlc-descript-audio-codec',  # Optional, if you have a repo
    install_requires=[
        "torch",
        "torchaudio",
        "numpy",
    ],
)