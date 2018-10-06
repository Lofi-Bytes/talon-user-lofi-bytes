from talon.voice import Word, Key, Context, Str
import string

terminals = ('com.apple.Terminal', 'com.googlecode.iterm2')
ctx = Context('terminal', func=lambda app, win: any(
    t in app.bundle for t in terminals))

mapping = {
    'semicolon': ';',
    r'new-line': '\n',
    r'new-paragraph': '\n\n',
}

def parse_word(word):
    word = word.lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word

# Ask for forgiveness not permission in failure scenario.
# https://stackoverflow.com/questions/610883/how-to-know-if-an-object-has-an-attribute-in-python
def text(m):
    try:
        tmp = [str(s).lower() for s in m.dgndictation[0]._words]
        words = [parse_word(word) for word in tmp]
        Str(' '.join(words))(None)
    except AttributeError:
        return

keymap = {
    'cd': ['cd ; ll', Key('left'), Key('left'), Key('left'), Key('left')],
    '(ls | run ellis | run alice)': 'ls\n',
    '(la | run la)': 'ls -la\n',
    'durrup': 'cd ..; ls\n',
    'go back': 'cd -\n',
    'direct desktop': ['cd ~/Desktop; ll', Key('enter')],
    'direct projects': ['cd ~/Desktop/projects; ll', Key('enter')],

    'pseudo': 'sudo ',
    'shell clear': [Key('ctrl-c'), 'clear\n'],
    'shell copy [<dgndictation>]': ['cp ', text],
    'shell copy curse [<dgndictation>]': ['cp -r', text],
    'shell exit': [Key('ctrl-c'), 'exit\n'],
    'shell kill': Key('ctrl-c'),
    # 'shell list [<dgndictation>]': ['ls ', text],
    # 'shell list all [<dgndictation>]': ['ls -la ', text],
    'shell list [<dgndictation>]': ['ls -la ', Key('return')],
    'shell make (durr | dear) [<dgndictation>]': ['mkdir ', text],
    'shell mipple [<dgndictation>]': ['mkdir -p ', text],
    'shell move [<dgndictation>]': ['mv ', text],
    'shell remove [<dgndictation>]': ['rm ', text],
    'shell remove curse [<dgndictation>]': ['rm -rf ', text],

    # dep
    'dip ensure': 'dep ensure\n',
    'dip ensure add': 'dep ensure -add ',
    'dip ensure update': 'dep ensure -update\n',

    # make
    'make': 'make\n',
    'make test': 'make test\n',
    'make build': 'make build\n',

    # git
    'jet [<dgndictation>]': ['git ', text],
    'jet add [<dgndictation>]': ['git add ', text],
    'jet branch': 'git br\n',
    'jet branch delete [<dgndictation>]': ['git br -D max/', text],
    'jet clone [<dgndictation>]': ['git clone ', text],
    'jet checkout master': 'git checkout master\n',
    'jet checkout max [<dgndictation>]': ['git checkout max/', text],
    'jet checkout [<dgndictation>]': ['git checkout ', text],
    'jet checkout branch [<dgndictation>]': ['git checkout -B max/', text],
    'jet commit [<dgndictation>]': ['git commit -a -m ""', Key('left'), text],
    'jet diff': 'git diff\n',
    'jet history': 'git hist\n',
    'jet merge [<dgndictation>]': ['git merge ', text],
    'jet pull [<dgndictation>]': ['git pull ', text],
    'jet pull base [<dgndictation>]': ['git pull --rebase ', text],
    'jet push [<dgndictation>]': ['git push ', text],
    'jet rebase': 'git rebase -i HEAD~',
    'jet stash': 'git stash\n',
    'jet status': 'git status\n',

    # Tools
    'grip': ['grep  .', Key('left left')],
    'gripper': ['grep -r  .', Key('left left')],
    'pee socks': 'ps aux ',
    'vi': 'vi ',

    'print environment': ['printenv', Key('return')],
    'finger [<dgndictation>]': ['touch ', text],
    'code [<dgndictation>]': ['code ', text],
    'pip environment [<dgndictation>]': ['pipenv ', text],
    'pip [<dgndictation>]': ['pip ', text],
    'open [<dgndictation>]': ['open', text],
}

ctx.keymap(keymap)
