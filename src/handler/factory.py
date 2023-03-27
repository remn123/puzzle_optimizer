from .object import Object


class ObjectFactory:


    def __init__(self, objects_info):
        self._objects_info = objects_info

    @property
    def types(self):
        return list(self._objects_info.keys())

    def make(self, type):
        info = self._objects_info.get(type, None)
        return Object(type, info)
