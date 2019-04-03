from connexion.resolver import RestyResolver
import connexion
from providers.CouchProvider import CouchProvider
from flask_injector import FlaskInjector
from api.customer import Customer
from injector import Binder

def configure(binder: Binder) -> Binder:
    binder.bind(
        CouchProvider
    )

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('simple_connexion_yaml.yaml', resolver=RestyResolver('api'))
    app.add_api('customerConnexion.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    app.run(port=5000,debug=True)