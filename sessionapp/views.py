from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 




class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return 
    
    

    
# @method_decorator(csrf_exempt, name='dispatch')
class Register(APIView):   
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)    
    def post(self, request):
        data=request.data
        print(data,9999999999)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data,88888888888)   
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

# @method_decorator(csrf_exempt,name='dispatch')
class UserLogin(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, request):
        print(request.user)
        if request.user.is_authenticated:
            return Response({'message': 'User is already logged in.'}, status=status.HTTP_200_OK)
        
        else:
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return Response({'message': 'Logged in successfully.'}, status=status.HTTP_200_OK)
        
            else:
              return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
# @method_decorator(csrf_exempt,name='dispatch')
class LogOut(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated,]
    def post(self, request):
        logout(request)
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        

