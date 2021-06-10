import config
from initialize_data import initialize_data

connex_app = config.connex_app
connex_app.add_api("swagger.yml", strict_validation=True)


if __name__ == '__main__':
    initialize_data()
    connex_app.run(debug=True)
