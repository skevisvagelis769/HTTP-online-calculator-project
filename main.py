from flask import Flask,render_template,redirect,url_for,request
app =Flask(__name__)

@app.route('/')
def welcome():
    return render_template('calc.html')
@app.route('/temp/<string:result>')
def temp(result):
    return render_template('result.html',results=result)
@app.route('/submit',methods=['GET','POST'])
def submit():
    check = {'+','-','/','*'}
    n1 = 0
    n2 = 0
    res =0
    op =''
    if request.method=='POST':
        try:
            n1 = float(request.form['n1'])
            n2 = float(request.form['n2'])
        except:
            return "You may only use numbers!"
        oper = request.form['op']


        if oper in check:
            match oper:
                case "+":
                    res = n1+n2
                case "-":
                    res = n1-n2
                case '*':
                    res = n1*n2
                    if res == -0.0 or res == 0.0:
                            res = 0
                case '/':
                    if(n2 == 0):
                        return "Second number cannot be 0 in division!"
                    else:
                        res = n1/n2
                        if res == -0.0 or res == 0.0:
                            res = 0

            return redirect(url_for('temp',result=str(res)))

        else:
            return "please try using a proper operand"





if __name__ == '__main__':
    app.run()