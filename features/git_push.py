__author__ = 'pioc'

import os

os.system('mkdir git_check_111')
os.chdir('git_check_111')
os.system('touch file_111.txt')
os.system('git init')
os.system('git add .')
os.system('git commit -m "First commit 111"')
os.system('git remote add origin git@github.com:pioccc/NowePioc6.git')
os.system('git remote -v')
os.system('git push origin master')


