from ninja import NinjaAPI
from ninja.security import HttpBearer
from .auth import router as auth_router
from .courses import router as course_router
from .enrollments import router as enrollment_router
from api.jwt_utils import decode_token
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        payload = decode_token(token)
        if payload:
            try:
                user = User.objects.get(id=payload["user_id"])
                return user
            except User.DoesNotExist:
                return None
        return None


api = NinjaAPI(title="Simple LMS API", auth=AuthBearer())

api.add_router("/auth/", auth_router)
api.add_router("/courses/", course_router)
api.add_router("/enrollments/", enrollment_router)
