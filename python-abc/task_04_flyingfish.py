#!/usr/bin/env python3
"""Thid module define class and class with multiple inheritance"""


class Fish:
    """Create class fish"""

    def swim(self):
        """Fish can swim"""
        print("The fish is swimming")

    def habitat(self):
        """Fish habitat"""
        print("The fish lives in water")


class Bird:
    """Create class Bird"""

    def fly(self):
        """Bird can fly"""
        print("The bird is flying")

    def habitat(self):
        """Bird habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Create class Flyingfish inheritance from fish and bird"""

    def fly(self):
        """FlyingFish soaring"""
        print("The flying fish is soaring!")

    def swim(self):
        """FlyingFish can swim"""
        print("The flying fish is swimming!")

    def habitat(self):
        """FlyingFish habitat"""
        print("The flying fish lives both in water and the sky!")
