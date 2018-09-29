from talon.voice import Context, Key
from talon import macos

ctx = Context('mission_control')

ctx.keymap({
    "(mission control | troll up)": lambda m: macos.dock_notify('com.apple.expose.awake'),
    "(front | troll down)": lambda m: macos.dock_notify('com.apple.expose.front.awake'),
    # "(next space | troll left)": Key('ctrl-alt-cmd-left'),
    # "(last space | troll right)": Key('ctrl-alt-cmd-right'),
    "(next space | troll left)": Key('ctrl-left'),
    "(last space | troll right)": Key('ctrl-right'),
    "launchpad": lambda m: macos.dock_notify('com.apple.launchpad.toggle'),
    "show desktop": lambda m: macos.dock_notify('com.apple.showdesktop.awake'),
})
