from flask import Flask, url_for, request, render_template, session
import MySQLdb
import hashlib

app = Flask(__name__)

app.secret_key = "sadgashdf15sadasds"

def md5(data):
    return hashlib.md5(data.encode("utf-8")).hexdigest()

def mysqlPripoj():
    db=MySQLdb.connect("usr12121.mysql.pythonanywhere-services.com","usr12121","heslo1234","usr12121$VTIPY")
    db.set_character_set("utf8")
    return db

@app.route('/')
def index():
    kategorie=""
    db=mysqlPripoj()
    cur=db.cursor()
    cur.execute("select nazev,id from kateg")
    kategorie=cur.fetchall()

    if "idkat" in request.args:
        idkat = request.args["idkat"]
    else:
        idkat=1

    cur.execute("select datum,obsah,vlozil from vtip where id_kateg=%s",[idkat])
    vtipy=cur.fetchall()

    db.close()
    return render_template("vtipy.html",kategorie=kategorie,vtipy=vtipy)




@app.route('/registrace/', methods = ["GET","POST"] )
def registrace():
    chyba=""
    if request.method=="POST":
        login =request.form["login"]
        heslo1=request.form["heslo1"]
        heslo2=request.form["heslo2"]
        email =request.form["email"]
        if heslo1!=heslo2:
            chyba="Hesla se neshodují"
        else:
            if len(login)>0:
                #existuje??
                db=mysqlPripoj()
                cur=db.cursor()
                cur.execute("select login from uziv where login=%s", [login])
                if cur.rowcount>0:
                    chyba="login uz zabrany"
                else:
                    cur.execute("select max(id) from uziv")
                    row=cur.fetchone()
                    id=int(row[0])+1

                    cur.execute("insert into uziv (id,login,heslo,email) values (%s,%s,%s,%s)", (id,login,md5(heslo1),email))
                    db.commit()
                    chyba="Uzivatel uspesne pridan"
                db.close()
            else:
                chyba="Login musi byt vyplnen"
    return render_template("registrace.html", chyba=chyba)


@app.route('/prihlaseni/', methods=["GET", "POST"])
def prihlaseni():
    login=""
    zprava=""
    uspech=""

    if "uziv" in session:
        uspech="Uživatel "+ session["uziv"]+" úspěšně odhlášen"
        del session["uziv"]

    if request.method=="POST":
        heslo=""
        try:
            login=request.form["login"]
            heslo=request.form["heslo"]
            zprava="Neplatné jméno a heslo"

            db = mysqlPripoj()
            cur = db.cursor()
            cur.execute("select * from uziv where login = %s and heslo = %s",  (login, md5(heslo) ))

            if cur.rowcount > 0:
                zprava=""
                uspech="Uspesne prihlaseni"
                session["uziv"]=login

            db.close()
        except:
            zprava="Chyba parametrů formuláře"

    return render_template("prihlaseni.html", uzivatel=login, zprava=zprava, uspech=uspech)


@app.route('/pridat/', methods=["GET", "POST"])
def pridat():
    zprava=""
    uspech=""
    if not "uziv" in session:
        zprava="Musíte se přihlásit!"
    elif request.method=="POST":
        try:
            kategorie = request.form["kategorie"]
            vtip      = request.form["vtip"]

            db = mysqlPripoj()
            cur = db.cursor()
            cur.execute("insert into vtip (id_kateg,datum,obsah,vlozil) values (%s,curdate(),%s,%s)", (kategorie,vtip,session["uziv"]))
            db.commit()
            uspech="vtip byl úspěšně přidán"
            db.close()
        except:
            zprava="Chyba parametrů formuláře"

    return render_template("pridat.html",zprava=zprava, uspech=uspech)


@app.route('/sprava-vtipu/')
def spravavtipu():

    if not "uziv" in session:
        return index()

    db=mysqlPripoj()
    cur = db.cursor()

    nz = request.args.get("id")
    if nz != None:
        try:
            db = mysqlPripoj()
            cur = db.cursor()
            cur.execute("delete from vtip where id=%s",(nz,))
            db.commit()
            db.close()
        except:
            pass
    try:
        db=mysqlPripoj()
        cur = db.cursor()
#       cur.execute("select datum,obsah,id from vtip where id_uziv=%s",[session["uziv_id"]])
        cur.execute("select datum,obsah,vlozil,id from vtip")
        vtipy=cur.fetchall()
        db.close()
    except:
        pass

    return render_template("spravavtipu.html",vtipy=vtipy)
