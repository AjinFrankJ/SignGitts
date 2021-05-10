

from gtts import gTTS

from playsound import playsound


mytext = 'Get ready'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
playsound('welcome.mp3')

# The text that you want to convert to audio ​
msg_welcome = "Welcome to my program"

# Language in which you want to convert ​

language = "en"
myobj = gTTS(text=msg_welcome, lang=language, slow=False)
myobj.save("msg_welcome.mp3")
playsound("msg_welcome.mp3")

a="Do you want to login or signup or exit and to login press L and to signup press S and to exit press E"
language="en"
myobj=gTTS(text=a,lang=language,slow=False)
myobj.save("a.mp3")
playsound("a.mp3")
deci =input("Do you want to login(L) or signup(S) or exit(E):").upper()
userdetails ={}
while(deci!='E'):
    if(deci=='S'):
        qr = 'Please enter your username'
        language = 'en'
        myobj = gTTS(text=qr, lang=language, slow=False)
        myobj.save("qr.mp3")
        playsound('qr.mp3')
        user_name =input("Please enter your username:")
        while(not(user_name and user_name.strip())):
            op = 'username cannot be blank so please enter valid username'
            language = 'en'
            myobj = gTTS(text=op, lang=language, slow=False)
            myobj.save("op.mp3")
            playsound('op.mp3')
            user_name =input("Username cannot be blank please enter valid username:")
        mn = 'Please enter the password'
        language = 'en'
        myobj = gTTS(text=mn, lang=language, slow=False)
        myobj.save("mn.mp3")
        playsound('mn.mp3')
        password =input("Please enter the password\n(Note:Password should be minimum 8 characters):")
        kl = 'Reenter password'
        language = 'en'
        myobj = gTTS(text=kl, lang=language, slow=False)
        myobj.save("kl.mp3")
        playsound('kl.mp3')
        rpassword =input("Reenter password:")
        while((len(password )<=7) or (password!=rpassword)):
            ij = 'enter the valid password'
            language = 'en'
            myobj = gTTS(text=ij, lang=language, slow=False)
            myobj.save("ij.mp3")
            playsound('ij.mp3')
            password =input("Enter the valid password(note: Minimum 8 characters):")
            ef = 'reenter the password'
            language = 'en'
            myobj = gTTS(text=ef, lang=language, slow=False)
            myobj.save("ef.mp3")
            playsound('ef.mp3')
            rpassword =input("Reenter the password:")
        cd = 'password accepted'
        language = 'en'
        myobj = gTTS(text=cd, lang=language, slow=False)
        myobj.save("cd.mp3")
        playsound('cd.mp3')
        print("password accepted")
        ab = 'Enter your mobile number'
        language = 'en'
        myobj = gTTS(text=ab, lang=language, slow=False)
        myobj.save("ab.mp3")
        playsound('ab.mp3')
        num =input("Enter your mobile number:")
        while(len(num)!=10) or (num.isdigit()==False):
            z = 'Enter the mobile number again'
            language = 'en'
            myobj = gTTS(text=z, lang=language, slow=False)
            myobj.save("z.mp3")
            playsound('z.mp3')
            num =input("Enter the number again:")
        y = 'number accepted'
        language = 'en'
        myobj = gTTS(text=y, lang=language, slow=False)
        myobj.save("y.mp3")
        playsound('y.mp3')
        print("number accepted")
        x = 'Enter your email id'
        language = 'en'
        myobj = gTTS(text=x, lang=language, slow=False)
        myobj.save("x.mp3")
        playsound('x.mp3')
        email =input("Enter your email\n(note:first character must be an alphabet and @ should bve present):")
        while(('@' in email )== False) or (email[0].isdigit()== True):
            xy = 'enter valid email'
            language = 'en'
            myobj = gTTS(text=xy, lang=language, slow=False)
            myobj.save("xy.mp3")
            playsound('xy.mp3')
            email =input("Enter valid email:")
        v = 'Email id is accepted'
        language = 'en'
        myobj = gTTS(text=v, lang=language, slow=False)
        myobj.save("v.mp3")
        playsound('v.mp3')
        print("Emailid is accepted")
        u = 'do you want to save your details then press y for yes and n for no'
        language = 'en'
        myobj = gTTS(text=u, lang=language, slow=False)
        myobj.save("u.mp3")
        playsound('u.mp3')
        Udeci =(input("Do you want to save your details? yes(Y) or no(N):").upper())
        userdetails ={}
        if(Udeci=='Y'):
            userdetails["username" ] =user_name
            userdetails["password" ] =password
            userdetails["email" ] =email
            userdetails["num" ] =num
            t = 'Data saved successfully'
            language = 'en'
            myobj = gTTS(text=t, lang=language, slow=False)
            myobj.save("t.mp3")
            playsound('t.mp3')
            print("Data saved successfully ")
            s = 'do u want to login or exit so press l for login and e for exit from program'
            language = 'en'
            myobj = gTTS(text=s, lang=language, slow=False)
            myobj.save("s.mp3")
            playsound('s.mp3')
            deci =(input("Do you want to login(L) or exit(E)").upper())
        else:
            r = 'your data not saved!!!'
            language = 'en'
            myobj = gTTS(text=r, lang=language, slow=False)
            myobj.save("r.mp3")
            playsound('r.mp3')
            print("Your data not saved!!!")
            q = 'do you want to signup or exit press s for signup and e for exit from program'
            language = 'en'
            myobj = gTTS(text=q, lang=language, slow=False)
            myobj.save("q.mp3")
            playsound('q.mp3')
            deci =(input("Do you want to signup(S) or exit(E):").upper())
    else:
        if(deci=='L'):
            p = 'please enter the username'
            language = 'en'
            myobj = gTTS(text=p, lang=language, slow=False)
            myobj.save("p.mp3")
            playsound('p.mp3')
            username =input("Please enter the username:")
            while(userdetails["username"] != username):
                o = 'invalid username,please enter valid username'
                language = 'en'
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("o.mp3")
                playsound('o.mp3')
                username =input("invalid username,please enter valid username:")
            for i in range(1,4):
                n = 'please enter your password'
                language = 'en'
                myobj = gTTS(text=n, lang=language, slow=False)
                myobj.save("n.mp3")
                playsound('n.mp3')
                password =input("please enter your password:")
                if(userdetails["password" ]==password):
                    m = 'login successful'
                    language = 'en'
                    myobj = gTTS(text=m, lang=language, slow=False)
                    myobj.save("m.mp3")
                    playsound('m.mp3')
                    print("login successful")
                    ls=1
                    i=5
                    break
                else:
                    l = 'hey its wrong password'
                    language = 'en'
                    myobj = gTTS(text=l, lang=language, slow=False)
                    myobj.save("l.mp3")
                    playsound('l.mp3')
                    print("hey its wrong password, you left with",3-i,"attempts")
            if(i==3):
                k = 'sorry,account blocked!!!'
                language = 'en'
                myobj = gTTS(text=k, lang=language, slow=False)
                myobj.save("k.mp3")
                playsound('k.mp3')
                print("sorry,account blocked!!!")
                exit(0)
            else:
                while(ls!=0):
                    jm = 'please enter your choice and press 1 to view your profile and press 2 to change your password and press 3 to logout and press 4 to exit out of the program'
                    language = 'en'
                    myobj = gTTS(text=jm, lang=language, slow=False)
                    myobj.save("jm.mp3")
                    playsound('jm.mp3')
                    ldeci=int(input("\nPlease enter your choice  :\n1)View profile \n2)change password \n3)logout \n4)exit"))
                    if(ldeci==1):
                        lm = 'Here is your details and thanks for using us'
                        language = 'en'
                        myobj = gTTS(text=lm, lang=language, slow=False)
                        myobj.save("lm.mp3")
                        playsound('lm.mp3')
                        print(" == ======userprofie============")
                        print("Username:",userdetails["username"])
                        print("Password:",userdetails["password"])
                        print("Email;:",userdetails["email"])
                        print("Mobile Number:",userdetails["num"])
                        print("===============================")
                        break
                    if ldeci==2:
                        i = 'enter your current password'
                        language = 'en'
                        myobj = gTTS(text=i, lang=language, slow=False)
                        myobj.save("i.mp3")
                        playsound('i.mp3')
                        cpassword= input("enter your current password:" )
                        if(userdetails["password"]==cpassword):
                            h = 'Please enter the password'
                            language = 'en'
                            myobj = gTTS(text=h, lang=language, slow=False)
                            myobj.save("h.mp3")
                            playsound('h.mp3')
                            password = input("Please enter the password\n(Note:Password should be minimum 8 characters):")
                            g = 'Reenter password'
                            language = 'en'
                            myobj = gTTS(text=g, lang=language, slow=False)
                            myobj.save("g.mp3")
                            playsound('g.mp3')
                            rpassword = input("Reenter password:")
                            while ((len(password) <= 7) or (password != rpassword)):
                                f = 'enter the valid password'
                                language = 'en'
                                myobj = gTTS(text=f, lang=language, slow=False)
                                myobj.save("f.mp3")
                                playsound('f.mp3')
                                password = input("enter the valid password(note: Minimum 8 characters):")
                                e = 'renter the password'
                                language = 'en'
                                myobj = gTTS(text=e, lang=language, slow=False)
                                myobj.save("e.mp3")
                                playsound('e.mp3')
                                rpassword = input("renter the password")
                            d = 'password accepted'
                            language = 'en'
                            myobj = gTTS(text=d, lang=language, slow=False)
                            myobj.save("d.mp3")
                            playsound('d.mp3')
                            print("password accepted")
                        else:
                            c = 'password mismatch'
                            language = 'en'
                            myobj = gTTS(text=c, lang=language, slow=False)
                            myobj.save("c.mp3")
                            playsound('c.mp3')
                            print("password mismatch")
                    if(ldeci==3):
                        ls=0
                        b = 'logged out successfully'
                        language = 'en'
                        myobj = gTTS(text=b, lang=language, slow=False)
                        myobj.save("b.mp3")
                        playsound('b.mp3')
                        print("logged out successfully")
                        break
                    if(ldeci==4):
                        deci==' E'
                        break
