import iso8601


class BaseModel(dict):
    def __getattr__(self, key):
        return self[key]

    def _iso8601_to_datetime(self, source):
        return iso8601.parse_date(source)


class User(BaseModel):
    pass


class Authentication(BaseModel):
    pass


class Client(BaseModel):
    pass


class Domain(BaseModel):
    pass


class Project(BaseModel):
    @property
    def date_created(self):
        return self._iso8601_to_datetime(self.dateCreated)


class JobPart(BaseModel):
    pass
