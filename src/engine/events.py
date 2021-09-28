"""
block_events.py

Contains decorators used to bind functions to events

TODO Clean up event names
"""
from functools import wraps

from .types import Target

__all__ = [
    'on_green_flag', 'on_pressed', 'on_clicked',
    'on_backdrop', 'on_greater', 'on_broadcast',
    'on_clone_start', 'sprite'
]

SPRITES = {}


def sprite(name):
    """Registers a class as a sprite which should be run"""
    def decorator(cls):
        if not issubclass(cls, Target):
            raise ValueError("@sprite expects a subclass of Target.")

        cls.name = name
        SPRITES[name] = cls
        return cls
    return decorator


def on_green_flag(func):
    """Binds a function to the green flag event"""
    func.event = 'green_flag'
    return func


def on_pressed(key):
    """Binds a function to a key press event"""
    def decorator(func):
        func.event = f"key_{key}_pressed"
        return func
    return decorator


def on_clicked(func):
    """Binds a function to the sprite clicked event"""
    func.event = 'sprite_clicked'
    return func


def on_backdrop(backdrop):
    """Binds a function to a backdrop changed event"""
    def decorator(func):
        func.event = "backdrop_" + backdrop
        return func
    return decorator


# TODO Proper when timer greater behavior
def on_greater(source, value=None):
    """Binds a function the the timer greater than event"""
    def decorator(func):
        @wraps(func)
        async def wrapper(self, util):
            # Run func when the timer is greater
            while True:
                if value is None or util.timer() > value:
                    func(self, util)
                await self.yield_()

        # Return the timer wrapper
        if source == 'timer':
            wrapper.event = 'green_flag'
            return wrapper

        # Default to the unmodified function
        return func
    return decorator


def on_broadcast(broadcast):
    """Binds a function to a broadcast event"""
    def decorator(func):
        func.event = 'broadcast_' + broadcast.lower()
        return func
    return decorator


def on_clone_start(func):
    """Binds a function to the clone started event"""
    func.event = 'clone_start'
    return func
