#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Create Animal Class"""
    @abstractmethod
    def sound(self):
        """Create abstract method sound for all other class"""
        pass


class Dog(Animal):
    """Create Dog class"""

    def sound(self):
        """Create method sound for dog"""
        return "Bark"


class Cat(Animal):
    """Create cat class"""

    def sound(self):
        """Create method sound for cat"""
        return "Meow"
