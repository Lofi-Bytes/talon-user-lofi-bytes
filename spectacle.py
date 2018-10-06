from talon.voice import Key, press, Str, Context

# Move and resize windows with Spectacle.app

ctx = Context('spectacle')


keymap = {
    'windy center': Key('cmd-ctrl-alt-c'),
    'windy max': Key('cmd-ctrl-alt-f'),

    'windy left': Key('cmd-ctrl-alt-left'),
    'windy right': Key('cmd-ctrl-alt-right'),
    'windy top': Key('cmd-ctrl-alt-up'),
    'windy bottom': Key('cmd-ctrl-alt-down'),

    'windy upper left': Key('cmd-ctrl-left'),
    'windy lower left': Key('cmd-ctrl-shift-left'),
    'windy upper right': Key('cmd-ctrl-right'),
    'windy lower right': Key('cmd-ctrl-shift-right'),

    'windy next display': Key('ctrl-right'),
    'windy previous display': Key('ctrl-left'),

    'windy next third': Key('ctrl-alt-right'),
    'windy previous third': Key('ctrl-alt-left'),

    'windy larger': Key('shift-ctrl-alt-right'),
    'windy smaller': Key('shift-ctrl-alt-left'),

    'windy undo': Key('cmd-ctrl-alt-z'),
    'windy redo': Key('cmd-ctrl-alt-shift-z'),

}

ctx.keymap(keymap)
