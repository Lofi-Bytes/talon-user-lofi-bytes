from talon.voice import Context, Key
from talon import macos

ctx = Context('mkdocs')

ctx.keymap({
    'make docs': 'mkdocs ',
    'make docs serve': ['mkdocs serve', Key('enter')],
    'make docs build': ['mkdocs build', Key('enter')],
    'make docs new': ['mkdocs new ',],
    'make docs help': ['mkdocs help', Key('enter')],
})
