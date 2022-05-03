# specmap

The specmap contains the information needed to generate Python code for sb3 blocks.

## Blockmap

The data json stores the raw definitions for each block. Each definition is known as a `blockmap`.

| field    | description                                                                                                                         |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| type     | The type of block or the return type for a reporter.                                                                                |
| args     | A dictionary of arguments used by the block. The key is the input or field name, and the value is the type after casting.           |
| code     | The unformatted Python code for the block. Every format field should have a corresponding type in `args`.                           |
| switch   | A string can be formatted into a new opcode. May contain format fields which can be replaced with normalized fields from the block. |
| basename | The base function name for a hat. May contain format fields.                                                                        |

Note that this describes the `blockmap` format used in the json. The format used in code is a more processed version of json format.


### Reporter example

```json
"operator_mod": {
    "type": "float",
    "args": {
        "NUM1": "float",
        "NUM2": "float"
    },
    "code": "({NUM1} % {NUM2})"
}
```

### Stack example

Notice that `code` is a list rather than a string. A list may be used to represent multiple lines of code in a more concise manor.

Also notice how the `SUBSTACK` format field is indented. If an indent field is a multiline string, all of the lines in the string will be indented.

```json
"control_if": {
    "type": "stack",
    "args": {
        "CONDITION": "bool",
        "SUBSTACK": "stack"
    },
    "code": [
        "if {CONDITION}:",
        "    {SUBSTACK}"
    ]
}
```


### Hat example

Notice the `IDENT` format field. The hat mutation adds a field to the block using the block definition's `basename`. The `basename` may contain format fields using any input or field listed in `args`. Note that the name is generated using unparsed arguments, so usually only fields should be used. Also note that the final function name will be made unique and sanitized.

```json
"event_whenbroadcastreceived": {
    "type": "hat",
    "args": {
        "IDENT": "hat_ident",
        "SUBSTACK": "stack",
        "BROADCAST_OPTION": "field"
    },
    "code": [
        "@on_broadcast({BROADCAST_OPTION})",
        "async def {IDENT}(self, util):",
        "    {SUBSTACK}"
    ],
    "basename": "broadcast_{BROADCAST_OPTION}"
}
```


### Switch example

In addition to `code`, a block definition can have a `switch`. The `switch` may contain format fields representing field inputs of a block. The fields are normalized by lowering all letters and replacing spaces with underscores. After a `switch` has been formatted, it represents a new opcode. If no definition exists for a block with the new opcode, the original definition will be used as a default.

```json
"sensing_current": {
    "type": "int",
    "args": {
        "CURRENTMENU": "field"
    },
    "switch": "sensing_current_{CURRENTMENU}"
},
"sensing_current_year": {
    "type": "int",
    "args": {},
    "code": "time.localtime()['tm_year']"
},
```


## Types

### Literal types

Reporter return types and block input arguments should have one of the literal types listed below. Note that substack inputs may also use the `stack` type, which is listed below under block types.

| type  | description                     |
| ----- | ------------------------------- |
| bool  | A bool `True` or `False` value. |
| int   | An integer value.               |
| float | A float value.                  |
| str   | A string value.                 |
| any   | A value of unknown type.        |


### Field types

Block field arguments should have one of the field types listed below.

| type         | description                                                                      |
| ------------ | -------------------------------------------------------------------------------- |
| field        | A string field.                                                                  |
| variable     | A variable identifier, eg. `self.my_variable`.                                    |
| list         | A list identifier, eg. `self.my_list`.                                        |
| property     | A variable identifier, kept the same across all sprites, without a `sprite.`.    |
| hat_ident    | A parsed function identifier.                                                    |
| ex_hat_ident | An existing parsed function identifier, used by the solo broadcast optimization. |
| proc_arg     | A procedure argument reporter identifier, used by the proc_arg mutation.         |


### Block types

If a block is not a reporter, it should have one of the following types.

| type  | description    |
| ----- | -------------- |
| hat   | A hat block.   |
| stack | A stack block. |


# Mutations

Mutations are used to handle more complex blocks which need more parsing than a basic switch. The mutations are defined in `mutations.py`. Each mutation has the ability to modify the `block` object, the parent `target` of the block, and replace the `blockmap` of the block.


# Codemap

The codemap, stored in `codemap.py`, handles creation of generic pieces of the code. For example, the `__init__` function for each sprite, the costume initialization, and the file header with import statements.
