from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'streamlit==0.72.0',
    'spleeter==2.0.1']

setup(
    name='StreamlitApp',
    version='1.0',
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(include=['mixs']),
    include_package_data=True,
    description='Streamlit App'
    )
