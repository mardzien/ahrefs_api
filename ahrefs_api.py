import json
import requests
from requests.utils import requote_uri


class AhrefsApi:
    def __init__(self, base_url, token):
        self.url = base_url + '?token=' + token

    def ahrefs_rank(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'ahrefs_rank', target, output, mode, limit)

    def anchors(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'anchors', target, output, mode, limit)

    def anchors_refdomains(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'anchors_refdomains', target, output, mode, limit)

    def backlinks(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'backlinks', target, output, mode, limit)

    def backlinks_new_lost(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'backlinks_new_lost', target, output, mode, limit)

    def backlinks_new_lost_counters(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'backlinks_new_lost_counters', target, output, mode, limit)

    def backlinks_one_per_domain(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'backlinks_one_per_domain', target, output, mode, limit)

    def broken_backlinks(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'broken_backlinks', target, output, mode, limit)

    def broken_links(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'broken_links', target, output, mode, limit)

    def domain_rating(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'domain_rating', target, output, mode, limit)

    def linked_anchors(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'linked_anchors', target, output, mode, limit)

    def linked_domains(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'linked_domains', target, output, mode, limit)

    def linked_domains_by_type(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'linked_domains_by_type', target, output, mode, limit)

    def metrics(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'metrics', target, output, mode, limit)

    def metrics_extended(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'metrics_extended', target, output, mode, limit)

    def pages(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'pages', target, output, mode, limit)

    def pages_extended(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'pages_extended', target, output, mode, limit)

    def pages_info(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'pages_info', target, output, mode, limit)

    def refdomains(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'refdomains', target, output, mode, limit)

    def refdomains_by_type(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'refdomains_by_type', target, output, mode, limit)

    def refdomains_new_lost(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'refdomains_new_lost', target, output, mode, limit)

    def refdomains_new_lost_counters(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'refdomains_new_lost_counters', target, output, mode, limit)

    def refips(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'refips', target, output, mode, limit)

    def subscription_info(self, target, output='json', mode='domain', limit=1):
        return self.__LazyRequest(self.url, 'subscription_info', target, output, mode, limit)

    class __LazyRequest:
        def __init__(self, url, method, target, output, mode, limit):
            self.url = url
            self.method = method
            self.target = target
            self.output = output
            self.mode = mode
            self.limit = limit

        @staticmethod
        def __configure_target(target):
            return '&target=' + target
        
        @staticmethod
        def __configure_limit(limit):
            return '&limit=' + str(limit)

        @staticmethod
        def __configure_output(output):
            return '&output=' + output

        @staticmethod
        def __configure_mode(mode):
            return '&mode=' + mode

        def __call(self, method="GET", **kwargs):
            url = self.url + \
                  '&from=' + \
                  self.method + \
                  self.__configure_target(self.target) + \
                  self.__configure_output(self.output) + \
                  self.__configure_mode(self.mode) + \
                  self.__configure_limit(self.limit)

            response = requests.request(method=method, url=url, **kwargs)

            if self.output != 'json':
                raise Exception(self.method, 'not implemented mode')

            result = response.json()

            if 'error' in result:
                raise Exception(self.method, result['error'])

            return result

        def where(self, where_clause):
            self.url = self.url + '&where=' + requote_uri(where_clause)

            return self

        def having(self, having_clause):
            self.url = self.url + '&having=' + requote_uri(having_clause)

            return self

        def order_by(self, order_by_clause):
            self.url = self.url + '&order_by=' + requote_uri(order_by_clause)

            return self

        def get(self):
            return self.__call(method="GET")
