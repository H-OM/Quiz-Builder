import os

# Create the root directory
root_dir = 'webapp'
os.mkdir(root_dir)

# Create subdirectories for each app
app1_dir = os.path.join(root_dir, 'app1')
os.mkdir(app1_dir)
app2_dir = os.path.join(root_dir, 'app2')
os.mkdir(app2_dir)

# Create subdirectories for static files and templates
static_dir = os.path.join(root_dir, 'static')
os.mkdir(static_dir)
templates_dir = os.path.join(root_dir, 'templates')
os.mkdir(templates_dir)

# Create subdirectories for static files within each app
app1_static_dir = os.path.join(static_dir, 'app1')
os.mkdir(app1_static_dir)
app1_css_dir = os.path.join(app1_static_dir, 'css')
os.mkdir(app1_css_dir)
app1_js_dir = os.path.join(app1_static_dir, 'js')
os.mkdir(app1_js_dir)
app2_static_dir = os.path.join(static_dir, 'app2')
os.mkdir(app2_static_dir)
app2_css_dir = os.path.join(app2_static_dir, 'css')
# Create subdirectories for templates within each app
app1_templates_dir = os.path.join(templates_dir, 'app1')
os.mkdir(app1_templates_dir)
app2_templates_dir = os.path.join(templates_dir, 'app2')
os.mkdir(app2_templates_dir)

# Create subdirectories for media files and documentation
media_dir = os.path.join(root_dir, 'media')
os.mkdir(media_dir)
docs_dir = os.path.join(root_dir, 'docs')
os.mkdir(docs_dir)

# Create Django app files
os.mkdir(os.path.join(app1_dir, 'views'))
open(os.path.join(app1_dir, '__init__.py'), 'a').close()
open(os.path.join(app1_dir, 'admin.py'), 'a').close()
open(os.path.join(app1_dir, 'apps.py'), 'a').close()
open(os.path.join(app1_dir, 'models.py'), 'a').close()
open(os.path.join(app1_dir, 'tests.py'), 'a').close()
open(os.path.join(app1_dir, 'views.py'), 'a').close()
open(os.path.join(app1_dir, 'urls.py'), 'a').close()
open(os.path.join(app1_dir, 'forms.py'), 'a').close()
open(os.path.join(app1_dir, 'views', 'login.py'), 'a').close()
open(os.path.join(app1_dir, 'views', 'quiz.py'), 'a').close()
open(os.path.join(app1_dir, 'views', 'progress.py'), 'a').close()
open(os.path.join(app1_dir, 'views', 'study_plan.py'), 'a').close()
open(os.path.join(app1_dir, 'views', 'resources.py'), 'a').close()
open(os.path.join(app1_dir, 'views', 'collaboration.py'),'a').close()
# Create Django app files (continued)
os.mkdir(os.path.join(app2_dir, 'views'))

open(os.path.join(app2_dir, '__init__.py'), 'a').close()
open(os.path.join(app2_dir, 'admin.py'), 'a').close()
open(os.path.join(app2_dir, 'apps.py'), 'a').close()
open(os.path.join(app2_dir, 'models.py'), 'a').close()
open(os.path.join(app2_dir, 'tests.py'), 'a').close()
open(os.path.join(app2_dir, 'views.py'), 'a').close()
open(os.path.join(app2_dir, 'urls.py'), 'a').close()
open(os.path.join(app2_dir, 'forms.py'), 'a').close()
open(os.path.join(app2_dir, 'views', 'base.html'), 'a').close()
open(os.path.join(app2_dir, 'views', 'questions.html'), 'a').close()
open(os.path.join(app2_dir, 'views', 'schedules.html'), 'a').close()
open(os.path.join(app2_dir, 'views', 'performance.html'), 'a').close()
open(os.path.join(app2_dir, 'views', 'accounts.html'), 'a').close()
open(os.path.join(app2_dir, 'views', 'settings.html'), 'a').close()
open(os.path.join(app2_dir, 'views', 'maintenance.html'), 'a').close()

# Create files for documentation
open(os.path.join(docs_dir, 'README.md'), 'a').close()
open(os.path.join(docs_dir, 'CONTRIBUTING.md'), 'a').close()


