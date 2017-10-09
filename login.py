from flask import Flask, session, render_template, request, redirect, url_for
import os

login = Flask(__name__)
login.secret_key = os.urandom(64)

@login.route('/', methods = ['GET', 'POST'])
def root():
    if 'username' in session:
        return render_template('response.html', user = session["username"])
    elif request.method == 'POST':
        # Username and password check
        if request.form["username"] != "username":
            return render_template('login.html', error = "Invalid Username")
        elif request.form["password"] != "password":
            return render_template('login.html', error = "Invalid Password")
        else: # Success
            session["username"] = request.form["username"] # Store username
            return render_template('response.html', user = session["username"])
    return render_template('login.html')

@login.route('/response') # Runs when logout is clicked
def response():
    if 'username' in session:
        session.pop("username"); # Remove username value
    return redirect( url_for('root') )

@login.route('/coolthingy')
def coolthingy():
    return redirect('/dragon')

@login.route('/dragon')
def dragon():
    return '''<pre>

                                            ,   ,
                                            $,  $,     ,
                                            "ss.$ss. .s'
                                    ,     .ss$$$$$$$$$$s,
                                    $. s$$$$$$$$$$$$$$`$$Ss
                                    "$$$$$$$$$$$$$$$$$$o$$$       ,
                                   s$$$$$$$$$$$$$$$$$$$$$$$$s,  ,s
                                  s$$$$$$$$$"$$$$$$""""$$$$$$"$$$$$,
                                  s$$$$$$$$$$s""$$$$ssssss"$$$$$$$$"
                                 s$$$$$$$$$$'         `"""ss"$"$s""
                                 s$$$$$$$$$$,              `"""""$  .s$$s
                                 s$$$$$$$$$$$$s,...               `s$$'  `
                             `ssss$$$$$$$$$$$$$$$$$$$$####s.     .$$"$.   , s-
                               `""""$$$$$$$$$$$$$$$$$$$$#####$$$$$$"     $.$'
                                     "$$$$$$$$$$$$$$$$$$$$$####s""     .$$$|
                                      "$$$$$$$$$$$$$$$$$$$$$$$$##s    .$$" $
                                       $$""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"   `
                                      $$"  "$"$$$$$$$$$$$$$$$$$$$$S""""'
                                 ,   ,"     '  $$$$$$$$$$$$$$$$####s
                                 $.          .s$$$$$$$$$$$$$$$$$####"
                     ,           "$s.   ..ssS$$$$$$$$$$$$$$$$$$$####"
                     $           .$$$S$$$$$$$$$$$$$$$$$$$$$$$$#####"
                     Ss     ..sS$$$$$$$$$$$$$$$$$$$$$$$$$$$######""
                      "$$sS$$$$$$$$$$$$$$$$$$$$$$$$$$$########"
               ,      s$$$$$$$$$$$$$$$$$$$$$$$$#########""'
               $    s$$$$$$$$$$$$$$$$$$$$$#######""'      s'         ,
               $$..$$$$$$$$$$$$$$$$$$######"'       ....,$$....    ,$
                "$$$$$$$$$$$$$$$######"' ,     .sS$$$$$$$$$$$$$$$$s$$
                  $$$$$$$$$$$$#####"     $, .s$$$$$$$$$$$$$$$$$$$$$$$$s.
       )          $$$$$$$$$$$#####'      `$$$$$$$$$###########$$$$$$$$$$$.
      ((          $$$$$$$$$$$#####       $$$$$$$$###"       "####$$$$$$$$$$
      ) \         $$$$$$$$$$$$####.     $$$$$$###"             "###$$$$$$$$$   s'
     (   )        $$$$$$$$$$$$$####.   $$$$$###"                ####$$$$$$$$s$$'
     )  ( (       $$"$$$$$$$$$$$#####.$$$$$###' -Tua Xiong     .###$$$$$$$$$$"
     (  )  )   _,$"   $$$$$$$$$$$$######.$$##'                .###$$$$$$$$$$
     ) (  ( \.         "$$$$$$$$$$$$$#######,,,.          ..####$$$$$$$$$$$"
    (   )$ )  )        ,$$$$$$$$$$$$$$$$$$####################$$$$$$$$$$$"
    (   ($$  ( \     _sS"  `"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$S$$,
     )  )$$$s ) )  .      .   `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"'  `$$
      (   $$$Ss/  .$,    .$,,s$$$$$$##S$$$$$$$$$$$$$$$$$$$$$$$$S""        '
        \)_$$$$$$$$$$$$$$$$$$$$$$$##"  $$        `$$.        `$$.
            `"S$$$$$$$$$$$$$$$$$#"      $          `$          `$
                `"""""""""""""'         '           '           ''
    <br></pre>'''


if __name__ == "__main__":
    login.debug = True
    login.run()
