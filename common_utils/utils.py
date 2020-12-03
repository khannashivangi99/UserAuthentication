import jwt
from authentication.models import User
def validate_jwt(func):
    def func_wrapper(view, request):
        auth_token = request.META["HTTP_AUTHORIZATION"]
        jwt_token = auth_token.split(' ')
        payload=jwt.decode(jwt_token[1],'secret',algorithms=['HS256'])

        # check if user is valid
        validity = validate_user(payload)
        print(validity)
        return validity
    return func_wrapper

def validate_user(payload):
    user_id = payload["some"]
    user_obj = User.objects.filter(id=user_id, is_active=True)
    if len(user_obj)>0:
        return True
    return False


