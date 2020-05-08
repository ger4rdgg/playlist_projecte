from behave import use_fixture
from django.core.management import call_command

from behave_fixtures import django_test_runner, django_test_case
import os

os.environ["DJANGO_SETTINGS_MODULE"] = "playlist_projecte.settings"

def before_all(context):
    use_fixture(django_test_runner, context)

def before_scenario(context, scenario):
    use_fixture(django_test_case, context)

def after_scenario(context, scenario):
        context.test.tearDownClass()
        del context.test
        call_command('flush', verbosity=0, interactive=False)

def after_all(context):
    context.test_runner.teardown_test_environment()
    context.browser.quit()
    context.browser = None