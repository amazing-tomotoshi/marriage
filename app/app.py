from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField, validators, ValidationError

# 予測する(楽しんごで確定)
def predict(partner):
    
    return "楽しんご"

app = Flask(__name__)

# flaskとwtformsを使い、index.html側で表示させるフォームを構築する
class MarriageForm(Form):
    partner = StringField("求婚相手",
                     [validators.InputRequired("この項目は入力必須です")])

    # html側で表示するsubmitボタンの表示
    submit = SubmitField("求婚")

@app.route('/', methods = ['GET', 'POST'])
def predicts():
    form = MarriageForm(request.form)
    if request.method == 'POST':
        if form.validate() == False:
            return render_template('index.html', form=form)
        else:            
            partner = request.form["partner"]            

            marriagePartner = predict(partner)

            return render_template('result.html', marriagePartner=marriagePartner)
    elif request.method == 'GET':

        return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()