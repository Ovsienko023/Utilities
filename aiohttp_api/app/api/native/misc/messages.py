from typing import List


class MessageLang:
    def __init__(self,
                 lang_id: int,
                 name: str):
        self._lang_id = lang_id
        self._name = name

    @property
    def lang_id(self) -> int:
        return self._lang_id

    @property
    def name(self) -> str:
        return self._name

    def get_entity(self):
        return {
            "lang_id": self._lang_id,
            "name": self._name
        }


class MessageLangList:
    def __init__(self,
                 langs: List[MessageLang],
                 count: int):
        self._langs = langs
        self._count = count

    @property
    def langs(self) -> list:
        return self._langs

    @property
    def count(self) -> int:
        return self._count

    def add(self, item):
        self._langs.append(item)

    def get_entity(self):
        res = []

        for lang in self.langs:
            res.append(lang.get_entity())

        return {
            "count": self.count,
            "langs": res
        }
