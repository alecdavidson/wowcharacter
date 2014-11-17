##Alec Davidson
import flask
import flask.views
import os
import wowcharacter

app = flask.Flask(__name__)

app.secret_key = "CorrectTurtleBatteryStaple"

class View(flask.views.MethodView):
  def get(self):
    return flask.render_template('index.html')
  
  def post(self):
    faction = flask.request.form['faction']
    count = flask.request.form['count']

    wowcharacter.main(faction, count)
    return self.get()
  
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET','POST'])


