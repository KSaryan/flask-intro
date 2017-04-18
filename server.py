"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page. <p>
    <a href="http://localhost:5000/hello">Hello</a></p></html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Get compliment!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <p>
          Choose your compliment:
          <select name="compliment">
            <option value="awesome">Awesome</option>
            <option value="smashing">Smashing</option>
            <option value="ducky">Ducky</option>
            <option value="neato">Neato</option>
          </select>
          <input type="submit" value="Submit">
        </form>
        <h1>The insult room!</h1>
        <form action="/diss">
        What's your name? <input type="text" name="person">
        <p>
        Choose your insult:
        <select name="diss">
          <option value="a gormless antiquarian! Thpppt!">a gormless antiquarian</option>
          <option value="a tedious heap of parrot droppings! Fetchez la vache!!">a tedious heap of parrot droppings</option>
          <option value="an electric donkey bottom biter!">an electric donkey bottom biter!</option>
        </select>
        </p>
        <input type="submit" value="Submit">
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


@app.route('/diss')
def diss_person():

  """Insult person."""

  player = request.args.get("person")

  diss = request.args.get("diss")

  return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """.format(player=player, diss=diss)



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
