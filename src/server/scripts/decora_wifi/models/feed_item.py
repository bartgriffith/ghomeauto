# Leviton Cloud Services API model FeedItem.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class FeedItem(BaseModel):
    def __init__(self, session, model_id=None):
        super(FeedItem, self).__init__(session, model_id)

    @classmethod
    def count(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/count"
        return session.call_api(api, attribs, 'get')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems"
        items = session.call_api(api, attribs, 'get')

        result = []
        if items is not None:
            for data in items:
                model = FeedItem(session, data['id'])
                model.data = data
                result.append(model)
        return result

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.data.update(data)
        return self

    @classmethod
    def find_one(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/findOne"
        return session.call_api(api, attribs, 'get')

    def refresh(self):
        api = "/FeedItems/{0}".format(self._id)
        result = self._session.call_api(api, {}, 'get')
        if result is not None:
            self.data.update(result)
        return self

    def get_controller(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/{0}/controller".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .controller import Controller
        model = Controller(self._session, data['id'])
        model.data = data
        return model

    def get_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/{0}/installation".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .installation import Installation
        model = Installation(self._session, data['id'])
        model.data = data
        return model

    def get_load(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/{0}/load".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .load import Load
        model = Load(self._session, data['id'])
        model.data = data
        return model

    def get_organization(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/{0}/organization".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .organization import Organization
        model = Organization(self._session, data['id'])
        model.data = data
        return model

    def get_person(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/{0}/person".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .person import Person
        model = Person(self._session, data['id'])
        model.data = data
        return model

    def get_sensor(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/{0}/sensor".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .sensor import Sensor
        model = Sensor(self._session, data['id'])
        model.data = data
        return model

    def get_shade(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/{0}/shade".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .shade import Shade
        model = Shade(self._session, data['id'])
        model.data = data
        return model

    def get_thermostat(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/{0}/thermostat".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        from .thermostat import Thermostat
        model = Thermostat(self._session, data['id'])
        model.data = data
        return model

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def replace_or_create(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/replaceOrCreate"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def upsert_with_where(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/upsertWithWhere"
        return session.call_api(api, attribs, 'post')

