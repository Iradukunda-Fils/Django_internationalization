import jwt
from django.utils.translation import activate
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

class LanguageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the Authorization header exists
        auth_header = request.headers.get('Authorization')
        
        if auth_header:
            try:
                # Extract the token from the Authorization header
                token = auth_header.split(' ')[1]
                decoded_token = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
                
                # Get the language from the token, defaulting to 'en' if not present
                language = decoded_token.get('language', 'en')
                
                # Set the language for the current request
                activate(language)
            except jwt.ExpiredSignatureError:
                return JsonResponse({"error": "Token expired"}, status=401)
            except jwt.DecodeError:
                return JsonResponse({"error": "Invalid token"}, status=401)
        else:
            # Default language if there's no token
            activate('en')
