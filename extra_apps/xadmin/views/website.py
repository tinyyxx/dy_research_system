from __future__ import absolute_import
from django.utils.translation import ugettext as _
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.views.decorators.cache import never_cache
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.http import HttpResponse

from .base import BaseAdminView, filter_hook
from .dashboard import Dashboard
from xadmin.forms import AdminAuthenticationForm
from xadmin.models import UserSettings
from xadmin.layout import FormHelper
from django.http import HttpResponseRedirect
from users.models import UserProfile

class IndexView(Dashboard):
    title = _("Main Dashboard")
    icon = "fa fa-dashboard"

    def get_page_id(self):
        return 'home'


class UserSettingView(BaseAdminView):

    @never_cache
    def post(self, request):
        key = request.POST['key']
        val = request.POST['value']
        us, created = UserSettings.objects.get_or_create(
            user=self.user, key=key)
        us.value = val
        us.save()
        return HttpResponse('')


class LoginView(BaseAdminView):

    title = _("    德亚研究系统登陆")
    login_form = None
    login_template = None

    @filter_hook
    def update_params(self, defaults):
        pass

    @never_cache
    def get(self, request, *args, **kwargs):
        context = self.get_context()
        helper = FormHelper()
        helper.form_tag = False
        helper.include_media = False
        context.update({
            'title': self.title,
            'helper': helper,
            'app_path': request.get_full_path(),
            REDIRECT_FIELD_NAME: request.get_full_path(),
        })
        defaults = {
            'extra_context': context,
            'current_app': self.admin_site.name,
            'authentication_form': self.login_form or AdminAuthenticationForm,
            'template_name': self.login_template or 'xadmin/views/login.html',
        }
        self.update_params(defaults)
        temp = login(request, **defaults)
        # 记录此次登录的ip地址
        if isinstance(temp, HttpResponseRedirect):
            username = request.user.username
            if 'HTTP_X_FORWARDED_FOR' in request.META:
                ip = request.META['HTTP_X_FORWARDED_FOR']
            else:
                ip = request.META['REMOTE_ADDR']
            user_profile = UserProfile.objects.get(username=username)
            user_profile.last_login_ip_backend = ip
            user_profile.save()

        return temp     # login(request, **defaults)

    @never_cache
    def post(self, request, *args, **kwargs):
        return self.get(request)


class LogoutView(BaseAdminView):

    logout_template = None
    need_site_permission = False

    @filter_hook
    def update_params(self, defaults):
        pass

    @never_cache
    def get(self, request, *args, **kwargs):
        context = self.get_context()
        defaults = {
            'extra_context': context,
            'current_app': self.admin_site.name,
            'template_name': self.logout_template or 'xadmin/views/logged_out.html',
        }
        if self.logout_template is not None:
            defaults['template_name'] = self.logout_template

        self.update_params(defaults)
        return logout(request, **defaults)

    @never_cache
    def post(self, request, *args, **kwargs):
        return self.get(request)
