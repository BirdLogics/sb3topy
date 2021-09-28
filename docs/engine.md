# engine

This is a quickly written description of many of the classes and functions
contained within the engine package. For additional documation, try using
`help(engine)` or `help(engine.events)` on any submodule.

Call engine.start_program to begin execution of a project.

## config

See `help(engine.config)` for information about config values.


## events

| decorator                   | description                                                                            |
| --------------------------- | -------------------------------------------------------------------------------------- |
| @sprite(sprite_name)        | Registers a subclass of Target as a sprite which should be run.                        |
| @on_green_flag              | Runs the function when the program starts.                                             |
| @on_pressed(key)            | Runs when the given key is pressed.                                                    |
| @on_clicked                 | Runs when the sprite is clicked.                                                       |
| @on_backdrop(backdrop_name) | Runs when the given backdrop is switched to.                                           |
| @on_greater(source, value)  | Runs when the value becomes greater than source. The only supported source is "timer". |
| @on_broadcast(broadcast)    | Runs when the given broadcast is broadcasted.                                          |
| @on_clone_start             | Runs in a newly created clone when it is created.                                      |


## operators

| function                    | description                                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------- |
| tonum(value)                | Attempts to cast a value to a float or int, defaulting to 0.                                            |
| toint(value)                | Attempts to cast a value to a int, defaulting to 0.                                                     |
| letter_of(text, index)      | Attempts to return a letter of text, starting at 1 and defaulting to "".                                |
| pick_rand(number1, number2) | Returns a random number between the two number. If one of the values is a float, the will be a decimal. |
| gt, lt, eq(value1, value2)  | Attempts to compare two values as a number, and failing that, compares them as a lowercased string.     |
| div(value1, value2)         | Attempts to divide two values and returns float('inf') in case of a ZeroDivisionError.                  |
| sqrt(value)                 | Attempts to find the sqrt of a value and returns float('nan') in case of a ValueError.                  |


## types

### Target

| property       | sets dirty | description                                       |
| -------------- | ---------- | ------------------------------------------------- |
| xpos           | rect       | Sets target._xpos and moves the pen.              |
| ypos           | rect       | Sets target._ypos and moves the pen.              |
| direction      | image      | Sets and wraps target._direction.                 |
| rotation_style | image      | Validates and sets target.costume.rotation_style. |
| size           | image      | Calls target.costume.set_size.                    |
| shown          | sprite     | Sets visibility of the target.                    |

| function                               | sets dirty | description                                                                         |
| -------------------------------------- | ---------- | ----------------------------------------------------------------------------------- |
| `move(steps)`                          | rect       | Moves a certain number of steps in the target's current direction.                  |
| `gotoxy(xpos, ypos)`                   | rect       | Sets `target._xpos` and `target._ypos` simultaneously, and moves the pen.           |
| `point_towards(util, other)`           | image      | Sets `target._direction` to point towards the sprite of name `other`.               |
| `async glide(duration, endx, endy)`    | rect       | Moves slowly to (`endx`, `endy`) over `duration` seconds.                           |
| `async glideto(util, duration, other)` | rect       | Moves slowly to the sprite of name `other` over `duration` seconds.                 |
| `bounce_on_edge()`                     |            | Not implemented.                                                                    |
| `distance_to(util, other)`             |            | Gives the distance from target to the sprite of name `other` or to the `"_mouse_"`. |
| `stop_other()`                         |            | Stops all scripts running in the sprite except for the current one.                 |
| `async yield_()`                       |            | Allows other scripts to run for a tick. There may be multiple ticks per frame.      |
| `async sleep(delay)`                   | screen     | Allows other scripts to run for a certain duration of time.                         |
| `get_touching(util, other)`            | clears     | Checks if the target is touching the sprite of name `other` or the `"_mouse_"`.     |
| `change_layer(util, value)`            | sprite     | Moves `value` layers fowards or backwards, depending on if the number is negative.  |
| `front_layer(util)`                    | sprite     | Moves to the frontmost layer.                                                       |
| `back_layer(util)`                     | sprite     | Moves the the backmost layer, excepting the stage.                                  |
| `create_clone_of(util, name)`          |            | Creates a clone of the sprite named `name`.                                         |
| `delete_clone(util)`                   |            | If this target is a clone, deletes it.                                              |

| internal function                       | sets dirty | description                                                                                                              |
| --------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------ |
| `start_event(util, name, restart=True)` |            | Start all functions registered for an event within the target.                                                           |
| `update(display, create_mask=False)`    | clears     | Updates the sprite rect, costume image, or sprite mask depending on what is dirty.                                       |
| `_update_image(display)`                |            | Updates the current image. Applies transformations such as scale and rotation, and graphic effects like ghost and color. |
| `_update_rect(display)`                 |            | Update the sprite's rect and converts stage coordinates to display coordinates.                                          |
| `_move_layers(group, start, value)`     |            | Helper used when changing the current layer.                                                                             |


@warp

### Costumes

Handles costumes for a Target. Keeps track of the current costume and effects.


### Sounds

Handles sounds for a Target. Keeps track of playing sounds, the volume, and effects.


### Pen

Handles the pen for a Target.


### List

Represents a standard list. A couple functions have a compatibility version
which supports arguments such as `"last"`. The parser automatically decides
when to use the more compatible function calls.


### StaticList

Represents a list which cannot have its items changed. Because the items never
change, a dictionary is used when determining if an item is contained by the
list, and when determing the index of an item in the list.
