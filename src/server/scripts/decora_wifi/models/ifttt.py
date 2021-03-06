# Leviton Cloud Services API model Ifttt.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class Ifttt(BaseModel):
    def __init__(self, session, model_id=None):
        super(Ifttt, self).__init__(session, model_id)

    @classmethod
    def brighten_switch(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/brighten_switch"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def dim_switch(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/dim_switch"
        return session.call_api(api, attribs, 'post')

    def refresh(self):
        api = "/ifttt/{0}".format(self._id)
        result = self._session.call_api(api, {}, 'get')
        if result is not None:
            self.data.update(result)
        return self

    @classmethod
    def get_activity_options(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/run_activity/fields/name/options"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def get_all_options(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/all/fields/name/options"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def get_dimmer_options(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/brighten_switch/fields/name/options"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def get_dimmer_options1(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/set_brightness/fields/name/options"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def get_dimmer_options2(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/dim_switch/fields/name/options"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def get_room_options(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/toggle_room_on/fields/name/options"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def get_scene_options(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/run_scene/fields/name/options"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def get_status(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/status"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def get_switch_on(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/triggers/switch_on"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def get_switch_options(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/triggers/switch_on/fields/name/options"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def get_switch_options1(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/toggle_switch/fields/name/options"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def get_user_info(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/user/info"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def run_activity(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/run_activity"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def run_scene(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/run_scene"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def set_brightness(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/set_brightness"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def setup(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/test/setup"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def toggle_room(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/toggle_room_on"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def toggle_room1(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/toggle_room_off"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def toggle_switch(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ifttt/v1/actions/toggle_switch"
        return session.call_api(api, attribs, 'post')

