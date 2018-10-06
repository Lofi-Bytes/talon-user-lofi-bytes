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
    'shrink dragon': ['dgn',],
    'shrink dragon dictation': ['dgndictation',],
    'shrink constant': ['const',],
    'shrink variable': ['var',],
    'shrink degree': ['deg',],
    'shrink pixel': ['px',],
    'shrink accumulator': ['acc',],
    'shrink current': ['cur',],
    'shrink properties': ['props',],
    'shrink function': ['func',],
    'shrink boolean': ['bool',],
})
