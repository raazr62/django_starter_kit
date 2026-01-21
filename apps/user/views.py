from .models import UserProfile
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from .authentication import CookieJWTAuthentication
from rest_framework.validators import ValidationError
from rest_framework.response import Response

# Use hybrid response utility
from .utils import create_hybrid_auth_response

from .serializers import (
    SignUpSerializer,
    SignInSerializer,
    SignOutSerializer,
    ChangePasswordSerializer,
    SendOTPSerializer,
    ResendOTPSerializer,
    VerifyOTPSerializer,
    ResetPasswordSerializer,
    UpdataProfileAvatarSerializer,
    UserProfileSerializer,
)

from apps.utils.helpers import success, error


# Singup
class SignUpView(APIView):
    permission_classes = []

    def post(self, request):

        serializer = SignUpSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            serializer.save()
            result = serializer.data
            return Response({
                "status": "success",
                "message": "Signup successful.",
                "data": result['user'],
            })
        raise ValidationError(serializer.errors)

# Signin
class SignInView(APIView):

    permission_classes = []

    def post(self, request):
        print("REQUEST DATA:", request.data)
        
        serializer = SignInSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            result = serializer.data
            
            
            return Response({
                "status": "success",
                "message": "Signin successful.",
                "data": result['user'],
                "access_token": result['access'],
                "refresh_token": result['refresh'],

            })
        raise ValidationError(serializer.errors)

# Signout
class SignOutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = SignOutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':status.HTTP_200_OK, 'success':True, 'message': 'Logout successful.', 'data': serializer.data}, status.HTTP_200_OK)
        return Response({'status':status.HTTP_400_BAD_REQUEST, 'success':False, 'message': 'Logout failed.', 'data': serializer.errors}, status.HTTP_400_BAD_REQUEST)

# Change Password
class ChangePasswordView(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return success(data=[], message="Password change successfully.", status_code=status.HTTP_200_OK)
        raise ValidationError(serializer.errors)

# Forgot Password (OTP Send)
class SendOTPView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        if serializer.is_valid():
            return success(data=[], message="OTP send to mail successfully.", status_code=status.HTTP_200_OK)
        errors = serializer.errors
        if "email" in errors:
            errors["error"] = errors.pop("email")
        raise ValidationError(errors)

# Reset Password (OTP Verify and Reset)
class ResetPasswordView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success(data=[], message="Password reset successfully.", status_code=status.HTTP_200_OK)
        errors = serializer.errors
        if "non_field_errors" in errors:
            errors["error"] = errors.pop("non_field_errors")
        return error(message="Password reset failed.", status_code=status.HTTP_400_BAD_REQUEST, errors=errors)

# Resend OTP
class ResendOTPView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = ResendOTPSerializer(data=request.data)
        if serializer.is_valid():
            return success(data=[], message="OTP send to mail successfully.", status_code=status.HTTP_200_OK)
        errors = serializer.errors
        if "email" in errors:
            errors["error"] = errors.pop("email")
        raise ValidationError(errors)

# Verify OTP (with purpose)
class VerifyOTPView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success(data=[], message="OTP verify is successfully.", status_code=status.HTTP_200_OK)
        return error(message="OTP verify is failed.", status_code=status.HTTP_400_BAD_REQUEST, errors=serializer.errors)

# Profile Views
class UpdataProfileAvatarView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CookieJWTAuthentication]

    def post(self, request):
        user = request.user
        
        serializer = UpdataProfileAvatarSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return success(data=serializer.data, message="Profile avatar update successfully.", status_code=status.HTTP_200_OK)
        return error(message="Profile avatar update failed.", status_code=status.HTTP_400_BAD_REQUEST, errors=serializer.errors)

# Profile Update
class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CookieJWTAuthentication]

    def put(self, request):
        user = request.user

        try:
            userProfile = UserProfile.objects.select_related('user').get(user=user)
        except UserProfile.DoesNotExist:
            return error(message="User not found.", status_code=status.HTTP_400_BAD_REQUEST, errors=[])

        serializer = UserProfileSerializer(userProfile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return success(data=serializer.data, message="Profile update successfully.", status_code=status.HTTP_200_OK)
        return error(message="Profile update failed.", status_code=status.HTTP_400_BAD_REQUEST, errors=serializer.errors)

# Profile Get
class ProfileGet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CookieJWTAuthentication]

    def get(self, request):
        user = request.user

        try:
            profile = UserProfile.objects.select_related('user').get(user=user)
        except UserProfile.DoesNotExist:
            return success(data=[], message="Profile not found.", status_code=status.HTTP_200_OK)

        data = {
            'id': profile.id,
            'email': profile.user.email,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'avater': profile.user.avatar.url if profile.user.avatar else None,
            'phone': profile.phone,
            'accepted_terms': profile.accepted_terms,
            'created_at': profile.created_at,
            'updated_at': profile.updated_at,
        }
        return success(data=data, message="Profile get successfully.", status_code=status.HTTP_200_OK)


class CookieTokenRefreshView(TokenRefreshView):
    """
    Hybrid Token Refresh View
    
    Supports both Web and Mobile clients:
    - Web: Reads refresh token from HttpOnly cookie, returns new tokens in cookies
    - Mobile: Reads refresh token from request body, returns new tokens in response body
    """
    
    def post(self, request, *args, **kwargs):
        # Inject refresh token from cookie into data if not present (for web clients)
        data = request.data.copy()
        if 'refresh' not in data and 'refresh_token' in request.COOKIES:
            data['refresh'] = request.COOKIES['refresh_token']
        
        serializer = self.get_serializer(data=data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        token_data = serializer.validated_data
        
        # Use hybrid response utility
        from .utils import create_hybrid_refresh_response
        
        tokens = {
            'access': token_data['access'],
            'refresh': token_data.get('refresh')  # May not exist if rotation is disabled
        }
        
        response = create_hybrid_refresh_response(
            tokens=tokens,
            request=request,
            message="Token refreshed successfully.",
            status_code=status.HTTP_200_OK
        )
        
        return response


class CookieTokenVerifyView(TokenVerifyView):
    """
    Hybrid Token Verify View
    
    Supports both Web and Mobile clients:
    - Web: Reads access token from HttpOnly cookie
    - Mobile: Reads token from request body
    """
    
    def post(self, request, *args, **kwargs):
        # Inject access token from cookie into data if not present (for web clients)
        data = request.data.copy()
        if 'token' not in data and 'access_token' in request.COOKIES:
            data['token'] = request.COOKIES['access_token']
        
        serializer = self.get_serializer(data=data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        return success(data=[], message="Token is valid.", status_code=status.HTTP_200_OK)




