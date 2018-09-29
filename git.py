from talon.voice import Context, Key
from talon import macos

ctx = Context('git')

ctx.keymap({
    'jet': 'git ',
    'jet (R M | remove)': 'git rm ',
    'jet add': 'git add ',
    'jet add all': ['git add --all', Key('enter')],
    'jet bisect': 'git bisect ',
    'jet branch': 'git branch ',
    'jet checkout': 'git checkout ',
    'jet clone': 'git clone ',
    'jet commit': ['git commit -a -m ""', Key('left')],
    'jet diff': 'git diff ',
    'jet fetch': 'git fetch ',
    'jet grep': 'git grep ',
    'jet in it': 'git init ',
    'jet log': 'git log ',
    'jet merge': 'git merge ',
    'jet move': 'git mv ',
    'jet pull': 'git pull ',
    'jet push': 'git push ',
    'jet rebase': 'git rebase ',
    'jet reset': 'git reset ',
    'jet show': 'git show ',
    'jet status': ['git status ', Key('enter')],
    'jet tag': 'git tag ',
    'jet ignore': '.gitignore',
})