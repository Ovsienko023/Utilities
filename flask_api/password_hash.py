from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


hash_ = generate_password_hash('foobar')
print(hash_)

print(check_password_hash(hash_, 'foobar'))
print(check_password_hash(hash_, 'barfoo'))
