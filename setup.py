from setuptools import setup, find_packages

setup(name="postcoder",
        version="1.0.0",
        description="Postcoder",
        lang_description="Get post code details",
        classifiers=[
            "Programming Language :: Python",
        ],
        author="Aaron Goldsmith",
        author_email="goldsmithaaron@gmail.com",
        url="",
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        entry_points={
            "console_scripts": [
                "postcoder = postcoder.__main__:main",
            ]
        },
        )
