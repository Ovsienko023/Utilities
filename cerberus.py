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
