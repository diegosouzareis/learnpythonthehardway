import web
from gothonweb import mapa

urls = (
  '/game', 'GameEngine',
  '/', 'Index',
)

app = web.application(urls, globals())

if web.config.get('_session') is None:
    loja = web.session.DiskStore('sessions')
    session = web.session.Session(app, loja,
                                  initializer={'quarto': None})
    web.config._session = session
else:
    session = web.config._session

renderizador = web.template.render('templates/', base="layout")


class Index(objeto):
    def GET(self):
        session.quarto = map.START
        web.seeother("/game")


class Engine(object):

    def GET(self):
        if session.quarto:
            return render.mostre_quarto(quarto=session.quarto)
        else:
            return render.voce_morreu()

    def POST(self):
        formulario = web.input(acao=None)

        if session.quarto and formulario.acao:
            session.quarto = session.quarto.go(formulario.acao)

        web.seeother("/game")

if __nome__ == "__main__":
    app.roda()
