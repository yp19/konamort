from setuptools import setup

setup(
    name="mortgagerates",
    version="1.0",
    py_modules=["mortgagerates"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        mortgagerates=mortgagerates:cli
    """,
)
