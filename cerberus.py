import cerberus
from cerberus.errors import BasicErrorHandler


"""
    {field} - где произошла ошибка,
    {value} - невалидное значение,
    {constraint} - то что должно быть(указанно в схеме)
    ---------------------------------------------------------------------------------------
    {'min': 10.1, 'max': 10.9}  # что бы сработало, 'lang_id' обязательно болжно быть int()
    {'minlength': 1, 'maxlength': 3}
    {'nullable': True}  # значение ключа может быть None
    {'regex': r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'}  # Для email
    {'empty': False}  # значение не должно быть пустым ''
    {'required': True}  # обязательное значение
    {'coerce': int}  #  пытается сделать int()
    {'allowed': ['password']}  #  сверяет значение ключа с листом
    {'allowed': ['refresh_token']}  # на конкретное поле
    {'rename': 'bar'}  # переименование
    {'default': 'my_value'}  # задание значения ключу по умолчанию
    {'coerce': to_bool}  # преведение к булевому типу: 'true' -> True
""" 


class CustomErrorHandler(BasicErrorHandler):
    messages = BasicErrorHandler.messages.copy()

    messages[0x02] = "нет обязательного поля!"

    messages[0x24] = 'значение должно быть типа {constraint} как в схеме '

    messages[0x41] = "для регялярки на email"
    messages[0x42] = "меньше мin {constraint}"
    messages[0x43] = "привышен мах {constraint}"
    messages[0x44] = "значение должно быть этим словом: {constraint}"
    
    messages[0x61] = "Ошибка приведения к типу {constraint} (у нас int())"


schema = {
    'lang_id': {'required': True, 'regex': r'[1-9]'},
    'time_zone_id': {'required': True, 'regex': r'[1-9]'},
    'name': {'type': 'string', 'nullable': True},
    'display_name': {'type': 'string'},
    'email': {'type': 'string', 'regex': r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'}    
}

validator = cerberus.Validator(schema, error_handler=CustomErrorHandler)
validator.allow_unknown = True  # Для разрешения ключей которых нет в схеме


doc = {
    'lang_id': 2,
    'time_zone_id': 349,
    'name': 'mod_Miki',
    'display_name': 'Admin_Bob',
    'email': 'Admin_Bob@trueconf.ru'
}

print(validator(doc))
print(validator.errors)


old_messages = {
        0x00: "{0}",
        0x01: "document is missing",
        0x02: "required field",
        0x03: "unknown field",
        0x04: "field '{0}' is required",
        0x05: "depends on these values: {constraint}",
        0x06: "{0} must not be present with '{field}'",
        0x21: "'{0}' is not a document, must be a dict",
        0x22: "empty values not allowed",
        0x23: "null value not allowed",
        0x24: "must be one of these types: {constraint}",
        0x26: "length of list should be {0}, it is {1}",
        0x27: "min length is {constraint}",
        0x28: "max length is {constraint}",
        0x41: "value does not match regex '{constraint}'",
        0x42: "min value is {constraint}",
        0x43: "max value is {constraint}",
        0x44: "unallowed value {value}",
        0x45: "unallowed values {0}",
        0x46: "unallowed value {value}",
        0x47: "unallowed values {0}",
        0x48: "missing members {0}",
        0x61: "field '{field}' cannot be coerced: {0}",
        0x62: "field '{field}' cannot be renamed: {0}",
        0x63: "field is read-only",
        0x64: "default value for '{field}' cannot be set: {0}",
        0x81: "mapping doesn't validate subschema: {0}",
        0x82: "one or more sequence-items don't validate: {0}",
        0x83: "one or more keys of a mapping  don't validate: {0}",
        0x84: "one or more values in a mapping don't validate: {0}",
        0x85: "one or more sequence-items don't validate: {0}",
        0x91: "one or more definitions validate",
        0x92: "none or more than one rule validate",
        0x93: "no definitions validate",
        0x94: "one or more definitions don't validate",
    }
