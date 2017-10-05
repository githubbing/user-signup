from flask import Flask, request, redirect
import cgi
import os 
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    template = jinja_env.get_template('form.html')
    return template.render()

@app.route("/", methods = ['POST'])
def user_verify():
    
    usern = request.form['username']
    pword = request.form['password']
    vpword = request.form['verify']
    em = request.form['email']

    if usern == '' or len(usern) < 3 or len(usern) > 20 or ' ' in usern:
        user_err_msg = 'Invalid Username'
    else:
        user_err_msg = ''
    if pword == '' or len(pword) < 3 or len(pword) > 20 or ' ' in pword:
        p_err_msg = 'Invalid Password'
    else:
        p_err_msg = ''
    if vpword != pword:
        v_err_msg = 'Passwords do not match'
    else:
        v_err_msg = ''
    if em.count("@") != 1 or em.count(".") != 1 or len(em) < 3 or len(em) > 20:
        em_err_msg = 'Invalid Email'
       
           
    if user_err_msg != '' or p_err_msg != '' or v_err_msg != '':

        template = jinja_env.get_template('form.html')
        return template.render(username_err=user_err_msg, pass_err=p_err_msg, 
        pass_match_err=v_err_msg, email_err=em_err_msg, e_mail=em, uname=usern)
    else:
        template = jinja_env.get_template('hello.html')
        return template.render(user_name=usern,)
app.run()