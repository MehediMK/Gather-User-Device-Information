Package: pip install django-user-agents
URL : https://pypi.org/project/django-user-agents/

Project description
Django User Agents
A django package that allows easy identification of visitor’s browser, OS and device information, including whether the visitor uses a mobile phone, tablet or a touch capable device. Under the hood, it uses user-agents.

Installation
=================
Install django-user-agents, you’ll have to make sure that user-agents is installed first:

pip install pyyaml ua-parser user-agents
pip install django-user-agents
Configure settings.py:

INSTALLED_APPS = (
    # Other apps...
    'django_user_agents',
)

# Cache backend is optional, but recommended to speed up user agent parsing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Name of cache backend to cache user agents. If it not specified default
# cache alias will be used. Set to `None` to disable caching.
USER_AGENTS_CACHE = 'default'
Usage
Middleware
=============
Add UserAgentMiddleware in settings.py:

MIDDLEWARE_CLASSES = (
    # other middlewares...
    'django_user_agents.middleware.UserAgentMiddleware',
)
A user_agent attribute will now be added to request, which you can use in views.py:


=====================
def my_view(request):

    # Let's assume that the visitor uses an iPhone...
    request.user_agent.is_mobile # returns True
    request.user_agent.is_tablet # returns False
    request.user_agent.is_touch_capable # returns True
    request.user_agent.is_pc # returns False
    request.user_agent.is_bot # returns False

    # Accessing user agent's browser attributes
    request.user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
    request.user_agent.browser.family  # returns 'Mobile Safari'
    request.user_agent.browser.version  # returns (5, 1)
    request.user_agent.browser.version_string   # returns '5.1'

    # Operating System properties
    request.user_agent.os  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
    request.user_agent.os.family  # returns 'iOS'
    request.user_agent.os.version  # returns (5, 1)
    request.user_agent.os.version_string  # returns '5.1'

    # Device properties
    request.user_agent.device  # returns Device(family='iPhone')
    request.user_agent.device.family  # returns 'iPhone'



If you have django.core.context_processors.request enabled, user_agent will also be available in template through request:

{% if request.user_agent.is_mobile %}
    Do stuff here...
{% endif %}

View Usage
===========
django-user_agents comes with get_user_agent which takes a single request argument and returns a UserAgent instance. Example usage:

from django_user_agents.utils import get_user_agent

def my_view(request):
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        # Do stuff here...
    elif user_agent.is_tablet:
        # Do other stuff...

Template Usage
================
django-user_agents comes with a few template filters:

is_mobile
is_tablet
is_touch_capable
is_pc
is_bot
You can use all of these like any other django template filters:

{% load user_agents %}

{% if request|is_mobile %}
    Mobile device stuff...
{% endif %}

{% if request|is_tablet %}
    Tablet stuff...
{% endif %}

{% if request|is_pc %}
    PC stuff...
{% endif %}

{% if request|is_touch_capable %}
    Touch capable device stuff...
{% endif %}

{% if request|is_bot %}
    Bot stuff...
{% endif %}