from app import app
from flask import render_template,redirect,url_for,request #renderização
from app.forms.alpha import equipa_form
from app.models.alpha import equipa_model
from app import db
"""""
@app.route("/cadequipa  ",methods=["POST","GET"])
def cadastrar_equipamento():
      form = equipa_form.EQUIPAForm()
      if form.validate_on_submit():
       nome = form.nome.data #capturando o conteúdo validado
       equipa = equipa_model.EQUIPA(nome=nome)
       try:
          #adicionar na sessão 
          db.session.add(equipa)
          #salvar a sessão
          db.session.commit()
          if request.method == 'POST':
           return redirect(url_for('equaipamentos'))
       except:
         print("equipameno não cadastrado")
      return render_template("equipa/cad_equipa.html",form=form)
"""

@app.route("/cadequipa")
def cadastrar_equipamento():
    return render_template("equipa/cad_equipa.html")


""""
@app.route("/equipa")
def listar_niveis():
    niveis = equipa_model.Nivel.query.all()  # Consulta todos os registros na tabela Nivel
    return render_template("equipa/equipa_1.html", niveis=niveis)

"""
