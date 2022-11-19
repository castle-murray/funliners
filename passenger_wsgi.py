import sys, os
INTERP = "/bin/python3"
#INTERP is present twice so that the new python interpreter 
#knows the actual executable path 
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/funliners')  #You must add your project here

sys.path.insert(0,cwd+'/venv/bin')
sys.path.insert(0,cwd+'/venv/lib/python3.6.8/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "funliners.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
