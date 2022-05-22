#!/usr/bin/env python

# -*- coding: UTF-8 -*-
import setuptools

setuptools.setup(
    name = 'challange-rest-api',
    version='0.0.1',
    license='GNU General Public License v3',
    author='Er5bus',
    description='REST API CHALLANGE',
    packages=setuptools.find_packages(),
    platforms='any',
    install_requires=[
        'asyncpg==0.24.0',
        'psycopg2-binary==2.9.2',
        'fastapi==0.70.*',
        'pydantic[dotenv]==1.8.2',
        'uvicorn==0.15.*',
        'pytest==6.2.*',
        'asyncio==3.4.3',
        'python-jose[cryptography]==3.3.0',
        'passlib[bcrypt]==1.7.4',
        'python-multipart==0.0.5',
        'wheel',
        'uvicorn',
        'gunicorn',
        'uvloop',
        'httptools'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
