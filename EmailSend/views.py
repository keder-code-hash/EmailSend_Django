from django.http import JsonResponse
from rest_framework.response import Response 
from rest_framework import status 
from django.core.mail import EmailMultiAlternatives 
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template 
import os 
import json
from dotenv import load_dotenv
load_dotenv() 

def send_email(user_name,send_to): 
    try : 
        subject,from_email,to='Visit Us Today',os.environ['EMAIL_HOST_USER'],"kedernath.mallick.tint022@gmail.com"
        text_context=f'{user_name}wants to contact with you' 

        context = { "username": user_name }
        message = get_template("index.html").render(context)


        msg=EmailMultiAlternatives(subject,text_context,from_email,[to])
        msg.attach_alternative(message,'text/html')

        msg.send()
        return True
    except : 
        return False


@api_view(['POST',])
@renderer_classes([JSONRenderer])
@csrf_exempt
def send_email_user(request): 
    try:
        decoded_req_body = request.body.decode('utf-8')
        req_body = json.loads(decoded_req_body)
        user_name=req_body.get("username")
        send_to=req_body.get("send_to")
        
         
        if len(user_name)==0 or len(send_to)==0:
            return Response({"message":"username or send_to is null."},status=status.HTTP_400_BAD_REQUEST)

        if send_email(user_name=user_name,send_to=send_to): 
            return Response({"message":"emails are sent successfully to "+user_name +"."},status=status.HTTP_200_OK)
        else :
            return Response({"message":"errors in sending emails."},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except:
        return Response({"message":"please check request body format."},status=status.HTTP_400_BAD_REQUEST)

def check(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode) 
    subject,from_email,to='contact',os.environ['EMAIL_HOST_USER'],"kedernath.mallick.tint022@gmail.com"
    text_context=f'{"user_name"}wants to contact with you'
    html_content='<p><strong>EMAIL:</strong>'+"send_to"+'</p><br><h4>MESSAGE:</h4>'+"Welcome "+"user_name"


    d = { 'username': "username" }
    message = get_template("index.html").render(d)


    print(message)
    msg=EmailMultiAlternatives(subject,text_context,from_email,[to])
    msg.attach_alternative(message,'text/html')
    msg.send()
    return JsonResponse({"msg":body})