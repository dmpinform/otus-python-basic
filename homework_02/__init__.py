"""
Домашнее задание №2
Классы и модули
"""
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from homework_02 import base, car, engine, exceptions, plane


__all__ = [
    "base",
    "car",
    "engine",
    "exceptions",
    "plane"
]
