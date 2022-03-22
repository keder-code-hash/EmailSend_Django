from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
from rest_framework import status 
from django.core.mail import EmailMultiAlternatives 
from rest_framework.decorators import api_view 
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template 
from .serializers import EmailSerializers
import os 
import re
import json
from dotenv import load_dotenv
load_dotenv() 

def send_email(user_name,send_to): 
    try : 
        subject,from_email,to='Visit Us Today',os.environ['EMAIL_HOST_USER'],send_to
        text_context=f'{user_name}wants to contact with you' 

        context = { "username": user_name }
        message = get_template("index.html").render(context)


        msg=EmailMultiAlternatives(subject,text_context,from_email,[to])
        msg.attach_alternative(message,'text/html')

        msg.send()
        return True
    except : 
        return False
 
def check_email(email):    
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False
 

@api_view(['POST'])
# @renderer_classes([JSONRenderer])
# @csrf_exempt
def send_email_user(request): 
    try:
        decoded_req_body = request.body.decode('utf-8')
        req_body = json.loads(decoded_req_body)
        user_name=req_body.get("username")
        send_to=req_body.get("send_to")
         
        if len(user_name)==0 or len(send_to)==0:
            return Response({"message":"username or send_to is null."},status=status.HTTP_400_BAD_REQUEST)

        if check_email(send_to)==False:
            return Response({"message":"Invalid Email."},status=status.HTTP_400_BAD_REQUEST)

        try : 
            data = JSONParser().parse(request) 
            serializer = EmailSerializers(data=data)
            if serializer.is_valid():
                serializer.save() 
                if send_email(user_name=user_name,send_to=send_to): 
                    return Response({"message":"email sent successfully to "+user_name +"."},status=status.HTTP_200_OK)
                else :
                    return Response({"message":"errors in sending emails."},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except :
            return Response({"message":"Internal Server Error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except:
        return Response({"message":"please check request body format."},status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def check(request): 
    return Response({"msg":"hii APi is working fine"})