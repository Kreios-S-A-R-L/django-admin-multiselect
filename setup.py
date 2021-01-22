import setuptools

setuptools.setup(
    name="django-admin-multiselect", 
    version="0.0.7",
    author="Kreios S.a r.l.",
    author_email="christian.hillerkus@kreios.lu",
    description="Alternative multiple select widget that works with mobile devices.",
    url="https://github.com/kreioslu/django-admin-multiselect",
    keywords=["django", "admin", "multiselect"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django"
    ]
)