from flask import Flask
from Routers.cityRouter import city_router
import sync

app = Flask(__name__)

# Registrar el blueprint de city
app.register_blueprint(city_router)
 
if __name__ == "__main__":
  sync.sync()
  app.run(debug=True)