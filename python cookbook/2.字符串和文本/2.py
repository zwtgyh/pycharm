line = 'asdf fjdk;  dsjk,dsad,             foo'
import re
re.split(r'[,;\s]\s*', line)
import os
filenames = os.listdir('.')
filenames
[name for name in filenames if name.endswith(('py', 'pdf'))]
any(name.endswith('.py') for name in filenames)
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3年\1月\2日', text)