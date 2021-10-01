from django.shortcuts import render

def home(request):
	context = {}
	if request.user_agent.is_pc:
		context['device'] = "Browse from PC"
		context['browser'] = request.user_agent.browser
		context['browser_Family'] = request.user_agent.browser.family
		context['browser_version'] = request.user_agent.browser.version_string
		context['os'] = request.user_agent.os
		context['user_device'] = request.user_agent.device.family
		
	elif request.user_agent.is_tablet:
		context['device'] = "Browse from tablet"		
		context['browser'] = request.user_agent.browser
		context['browser_Family'] = request.user_agent.browser.family
		context['browser_version'] = request.user_agent.browser.version_string
		context['os'] = request.user_agent.os
		context['user_device'] = request.user_agent.device.family

	elif request.user_agent.is_mobile:
		context['device'] = "Browse from Mobile"
		context['browser'] = request.user_agent.browser
		context['browser_Family'] = request.user_agent.browser.family
		context['browser_version'] = request.user_agent.browser.version_string
		context['os'] = request.user_agent.os
		context['user_device'] = request.user_agent.device.family

	elif request.user_agent.is_touch_capable:
		context['device'] = "Browse from touch capable"
		context['browser'] = request.user_agent.browser
		context['browser_Family'] = request.user_agent.browser.family
		context['browser_version'] = request.user_agent.browser.version_string
		context['os'] = request.user_agent.os
		context['user_device'] = request.user_agent.device.family

	elif request.user_agent.is_bot:
		context['device'] = "Browse from Bot"
		context['browser'] = request.user_agent.browser
		context['browser_Family'] = request.user_agent.browser.family
		context['browser_version'] = request.user_agent.browser.version_string
		context['os'] = request.user_agent.os
		context['user_device'] = request.user_agent.device.family
	

	return render(request,'index.html',context)