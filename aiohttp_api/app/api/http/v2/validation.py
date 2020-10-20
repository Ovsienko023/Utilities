
schema = {
    'lang_id': {'required': True, 'regex': r'[1-9]'},
    'time_zone_id': {'required': True, 'regex': r'[1-9]'},
    'name': {'type': 'string', 'nullable': True},
    'display_name': {'type': 'string'},
    'email': {'type': 'string', 'regex': r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'}    
}