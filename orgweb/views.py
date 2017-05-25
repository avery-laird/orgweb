from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import info
from django.contrib.auth.decorators import login_required
from .models import Profile, OrgModel
from .forms import OrgForm

from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.core.urlresolvers import NoReverseMatch
import json


def profile(request, **kwargs):
    """
    user_id can be a private key or a string
    :param request:
    :param user_id:
    :return:
    """
    context = {}
    return render(request, 'orgweb/profile.html', context)

@login_required
def create(request):
    return render(request, 'orgweb/org_create.html', context={})


def edit(request, file_name, template='orgweb/edit.html'):
    """
    Takes file name, and performs the desired changes in the database. NOTE: This was originally
    desired to have JSON functionality, so that the interface could be fully js (no reloads).
    Fuck that.
    Now, it's only url and redirection based (MAYBE modals). In the future, maybe I will API-ize it,
    to serve both purposes.
    :param request:
    :param file_name:
    :return:
    """
    org_file, created = OrgModel.objects.get_or_create(title=file_name, user=request.user.profile)
    form = OrgForm(request.POST or None, instance=org_file)
    print request.method
    if request.method == 'POST' and form.is_valid():
        org_file = form.save()
        info(request, "orgfile updated")
        return redirect("org_edit", file_name=org_file.title)
    context = {'form': form, 'title': "Edit File", 'file': org_file}
    return TemplateResponse(request, template, context)

@login_required
def delete(request, orgfile):
    orgf = OrgModel.objects.get(pk=orgfile)
    if request.user.profile == orgf.user:
        t = orgf.title
        orgf.delete()
        info(request, t + ' has been removed', extra_tags='success')
    else:
        info(request, "you do not have permission to remove this object", extra_tags='warning')
    return render(request, "orgweb/org_create.html", context={})


def view(request):
    pass


#### EXAMPLE JSON ENCODING
#[{
# 	"title": "test",
# 	"children": {
# 		"type": "header",
# 		"title": "test",
# 		"level": "2",
# 		"children": {
# 			"type": "header",
# 			"title": "child",
# 			"level": 4
# 		}
#  	}
#}]
# HEADER properties:
#
