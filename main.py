from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>Lets Play a game</h1>" \
           "<img src='https://media.giphy.com/media/17nllpH1dhdI9Z21qE/giphy.gif' width='200px'/>" \
           "<p style='color:blue'>You have to select a number from 1-5 and put it in the url if you choose the correct number then you win</p>" \





@app.route("/<name>/<int:number>")
def name(name,number):
    return f"hello  sir {name} and age{number}"

def bold(function):
    def wrapper():

        function()
    return f" <b>{wrapper()}<b>"


@app.route("/bye")
# @bold
def yee_yee():
    return '<h1>byee</h1>'


@app.route("/<number>")
def num_1(number):
    if "1" in number:
        return '<h1 style="text-align:center; color:blue">Wrong try  a higher number <h1>' \
               '<img style="display: block;margin-left: auto;margin-right: auto;width: 50%;" src="https://media.giphy.com/media/11nQ2iZnQpPkgo/giphy.gif"/ width=700px>'

    elif "2" in number:
        return '<h1 style="text-align:center; color:red">You got it correct,Congratulations!! <h1>' \
               '<img style="display: block;margin-left: auto;margin-right: auto;width: 50%;" src="https://media.giphy.com/media/pHZdGyFNp5sUXq4jp5/giphy-downsized-large.gif"/ width=500px>'

    elif "3" in number:
        return '<h1 style="text-align:center; color:green">Wrong try a lower number <h1>' \
               '<img style="display: block;margin-left: auto;margin-right: auto;width: 50%;" src="https://media.giphy.com/media/11Xc3nOtJcb8Aw/giphy.gif"/ width=700px>'

    elif "4" in number:
        return '<h1 style="text-align:center; color:red">try a lower number <h1>' \
               '<img style="display: block;margin-left: auto;margin-right: auto;width: 50%;" src="https://media.giphy.com/media/RJ1HZzWGCzdogvq5qP/giphy.gif"/ width=200px>'


    elif "5" in number:
        return '<h1 style="text-align:center; color:red">try a lower number <h1>' \
               '<img style="display: block;margin-left: auto;margin-right: auto;width: 50%;" src="https://media.giphy.com/media/WZP3qaxYj10gU/giphy.gif"/ width=200px>'

    else:
        return '<h1 style="text-align:center; color:red">Enter a valid number between 1-5 <h1>' \
               '<img style="display: block;margin-left: auto;margin-right: auto;width: 50%;" src="https://media.giphy.com/media/Y2nlgS7wp2iGUdu0OG/giphy.gif"/ width=200px>'

if __name__=="__main__":
    app.run(debug=True)