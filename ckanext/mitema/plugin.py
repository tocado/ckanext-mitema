from ckan.plugins import SingletonPlugin, implements, IConfigurer, ITemplateHelpers, IAuthFunctions
from ckan.logic import get_action
from ckan.common import c
import os
import sys

#print('***** MITEMA PLUGIN MODULE LOADED *****', file=sys.stderr)
class MiTemaPlugin(SingletonPlugin):
    implements(IConfigurer)
    implements(ITemplateHelpers)
    implements(IAuthFunctions)

    def update_config(self, config):
        from ckan.common import config as ckan_config
        import ckan.plugins.toolkit as toolkit

        template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#        print('MI PLUGIN MITEMA - TEMPLATE DIR:', template_dir)
        toolkit.add_template_directory(config, template_dir)
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'mitema')

        # toolkit.add_template_directory(config, 'templates')
        # toolkit.add_public_directory(config, 'public')
        # toolkit.add_resource('fanstatic', 'mitema')

    def get_helpers(self):
        return {
            'get_action': get_action,
            'get_user_name': lambda: c.user,
        }

    def get_auth_functions(self):
        return {
            'package_delete': self.allow_delete_draft
        }

    def allow_delete_draft(self, context, data_dict):
        model = context['model']
        user = context['user']
        pkg = model.Package.get(data_dict.get('id'))

        if not pkg:
            return {'success': False, 'msg': 'Dataset not found'}

        if pkg.state == 'deleted':
            return {'success': False, 'msg': 'Dataset already deleted'}

        # 🚀 Permitimos borrar tanto active como draft
        if pkg.state in ['active', 'draft']:
            return {'success': True}

        # fallback → otros estados no permitidos
        return {'success': False, 'msg': f'Cannot delete dataset in state: {pkg.state}'}
