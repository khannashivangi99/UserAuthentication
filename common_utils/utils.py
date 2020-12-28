import jwt
from rest_framework.response import Response
from authentication.models import User
def validate_jwt(func):
    def func_wrapper(view, request):
        auth_token = request.META["HTTP_AUTHORIZATION"]
        print(auth_token)
        try:
            payload=jwt.decode(auth_token,'some',algorithms=['HS256'])
        except Exception as e:
            return Response({"message":"Token invalid"},status=401)
         
        # check if user is valid
        validity = validate_user(payload)
        if not validity:
            return Response({"message":"User not found"},status=401)
        return func(view, request)
    return func_wrapper

def validate_user(payload):
    user_id = payload["user_id"]
    user_obj = User.objects.filter(id=user_id, is_active=True)
    if user_obj.count()>0:
        return True
    return False

def generate_jwt(d2):
    from datetime import datetime, timedelta
    d = {
        "email":d2.email,
        "timestamp": str(datetime.now())
    }
    print(d)
    token = jwt.encode(d, 'secret', algorithm='HS256')
    #print(token)
    return token

