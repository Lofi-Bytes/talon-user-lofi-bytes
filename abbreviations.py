from talon.voice import Context, Key
from talon import macos

ctx = Context('abbreviations')

ctx.keymap({
    'shrink directory': ['dir ',],
    'shrink make directory': ['mkdir ',],
    'shrink require': ['req ',],
    'shrink request': ['req ',],
    'shrink response': ['res',],
    'shrink error': ['err',],
    'shrink avenue': ['ave ',],
    'shrink expire': ['exp ',],
    'shrink control': ['ctrl ',],
    'shrink client': ['cli ',],
    'shrink environment': ['env ',],
})
