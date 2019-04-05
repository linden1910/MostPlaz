from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="most_plaz",
    version="0.0.2",
    author="Linden",
    author_email="<Linden@actfast.net>",
    description="Most Plaz - A QtPyVCP based Virtual Control Panel for LinuxCNC plazma table",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/linden1910/MostPlaz",
    download_url="https://github.com/linden1910/MostPlaz.git",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'most_plaz=most_plaz:main',
        ],
        'qtpyvcp.vcp': [
            'most_plaz=most_plaz',
        ],
    },
)
