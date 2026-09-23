from pathlib import Path

from setuptools import find_packages, setup

long_description = (Path(__file__).parent / "README.md").read_text(encoding="utf-8")

setup(
    name="django-svg-icons",
    version="0.1.0",
    author="buswedg",
    author_email="buswedg@djangomango.com",
    url="https://github.com/djangomango/django-svg-icons/",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "django_svg_icons": ["data/*.zip"],
    },
    install_requires=[
        "Django>=4.2",
    ],
    license="GNU Lesser General Public License v3 (LGPLv3)",
    description="Django template tag library for rendering inline SVG icons from 150+ pre-packaged icon sets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Framework :: Django",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1",
        "Framework :: Django :: 5.2",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.10",
)
