
import ckan.plugins as plugins
import ckan.logic as logic
import ckan.plugins.toolkit as tk
class SitemapPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IRoutes, inherit=True)

    def before_map(self, map):
        map.connect('/sitemap.xml',
                    controller='ckanext.sitemap.controller:SitemapController', action='sitemap')
        return map