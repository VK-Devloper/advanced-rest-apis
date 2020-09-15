from marshmallow import fields, Schema
from werkzeug.datastructures import FileStorage


class FileStorageField(fields.Field):
    default_error_messages = {
        'invalid': 'Not a valid image.'
    }

    def _deserialize(self, value, attr, data, **kwargs) -> FileStorage:
        if value is None:
            return None

        if not isinstance(value, FileStorage):
            return self.fail('invalid')     # raise ValidationError

        return value


class ImageSchema(Schema):
    image = FileStorageField(required=True)