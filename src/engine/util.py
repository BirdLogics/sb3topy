"""
util.py

Contains the several classes, such as Util, which contains helper
functions primarily used in project.py.
"""

import asyncio
import logging
import time


class Util:
    """
    Wrapper between runtime and project.py. Contains useful objects and
    functions to interface with project.py where needed.

    Attributes:
        timer: Handles the Timer.

        inputs: Handles keyboard/mouse input.

        sprites: Provides sprite lookup and stage.

        display: Used to get display info.

        events: Used to send events to sprites.

        runtime: The current Runtime instance.

        counter: Used for the hidden counter blocks.
    """

    def __init__(self, runtime):
        self.timer = Timer()
        self.inputs = runtime.inputs
        self.sprites = runtime.sprites
        self.display = runtime.display
        self.events = runtime.events
        self.runtime = runtime
        self.answer = ""
        self.counter = 0

    def send_event(self, event, restart=False):
        """Send an event"""
        self.events.send(self, self.sprites, event, restart)

    async def send_wait(self, event, restart=False):
        """Send an event"""
        await self.events.send_wait(self, self.sprites, event, restart)

    def send_broadcast(self, event):
        """Sends a broadcast"""
        return self.events.broadcast(self, self.sprites, event)

    async def send_broadcast_wait(self, event):
        """Sends a broadcast"""
        await self.events.broadcast_wait(self, self.sprites, event)

    def stop_all(self):
        """Ends execution of the main loop"""
        print("Stop")
        self.runtime.running = False

    def ask(self, prompt):
        """Asks for input on the console"""
        self.answer = input(prompt)


class Timer:
    """
    Handles a timer using time.monotonic

    TODO Make timer like a property with __get__
    """

    def __init__(self):
        self._timer = time.monotonic()

    def __call__(self):
        return time.monotonic() - self._timer

    def reset(self):
        """Reset the timer"""
        self._timer = time.monotonic()


class Events:
    """
    Contains useful functions for sending events

    Attributes:
        events: A dict containing a task representing the gathered
            tasks called by an event. See _send. {event_name: task}
    """

    def __init__(self):
        self.events = {}

    def _send(self, util, sprites, event, restart):
        """
        Creates a tasks for every couroutine tied to an event, and
        creates a parent task waiting for each of the child tasks to
        finish.

        When an event is restarted, both the child tasks and the parent
        tasks are cancelled. Although the parent task would eventually
        return if just the children were cancelled, there is a delay
        which makes it necesary to cancel the parent as well.

        Because the parent task can be cancelled, it is necesary to
        wrap awaits for the parent in a try except block to catch the
        cancellation.
        """
        if restart:
            # If a parent is in self.events, cancel it
            task = self.events.pop(event, None)
            if task is not None:
                task.cancel()

                # Backwards compatibility hack
                # Used instead of the Python 3.9 cancel msg
                task.was_restarted = True

        # Get a list of child tasks to runs
        tasks = []
        for sprite in sprites.sprites():
            tasks.extend(sprite.target.start_event(util, event, restart))
        tasks.extend(sprites.stage.start_event(util, event, restart))

        # Save and return the parent task
        task = asyncio.create_task(self._handle_tasks(tasks))
        self.events[event] = task
        return task

    def send(self, util, sprites, event, restart=False):
        """Starts an event for all sprites. Cannot be awaited."""
        self._send(util, sprites, event, restart)

    async def send_wait(self, util, sprites, event, restart):
        """Starts an event for all sprites. Should be awaited."""
        # Get the task
        task = self._send(util, sprites, event, restart)

        # Wait for it, but catch if it is cancelled
        try:
            await task
        except asyncio.CancelledError:
            # Verify the task was cancelled and not this function
            if not hasattr(task, "was_restarted"):
                raise

    def send_to(self, util, target, event):
        """Starts an event for a single target"""
        tasks = target.start_event(util, event)
        return asyncio.create_task(self._handle_tasks(tasks))

    async def _handle_tasks(self, tasks):
        """Waits on a list of tasks and catches any errors"""
        # Handle an empty list
        if not tasks:
            return

        done, _ = await asyncio.wait(
            tasks, return_when=asyncio.FIRST_EXCEPTION)

        # Handle any errors
        for task in done:
            try:
                task.result()
            except asyncio.CancelledError:
                pass
            except Exception:  # pylint: disable=broad-except
                logging.exception("Error in gathered task '%s'", task)

    def broadcast(self, util, sprites, event):
        """Parses a broadcast name and sends it. Not awaitable."""
        event = 'broadcast_' + event.lower()
        self._send(util, sprites, event, True)

    async def broadcast_wait(self, util, sprites, event):
        """Parses a broadcast name and sends it. Awaitable."""
        event = 'broadcast_' + event.lower()
        await self.send_wait(util, sprites, event, True)
