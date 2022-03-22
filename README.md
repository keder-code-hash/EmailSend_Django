# EmailSend_Django
## Details :
    A simple APi for sending mail to any one.
## web API url : 
<a href="https://sending1email.herokuapp.com/send_email">
<pre>
<code>
https://sending1email.herokuapp.com/send_email
</code>
</pre>
</a>

**only POST request is supported**
## Request Body Format : 
<pre>
<code>
{  
    "username" : "XXXX@hash",
    "send_to" : "XXXXXX@gmail.com"
}
</code>
</pre>

## Some Results : 

1. 😊![success](https://github.com/keder-code-hash/EmailSend_Django/blob/master/static/images/Screenshot%202022-03-22%20132734.jpg)
2. ❌![method-not-allowed](https://github.com/keder-code-hash/EmailSend_Django/blob/master/static/images/ss.jpg)
3. ✔![null](https://github.com/keder-code-hash/EmailSend_Django/blob/master/static/images/null.jpg)
4. ❌![wrongbody](https://github.com/keder-code-hash/EmailSend_Django/blob/master/static/images/invbody.jpg)
5. ✔![invalid-email](https://github.com/keder-code-hash/EmailSend_Django/blob/master/static/images/invalid_email.jpg)
