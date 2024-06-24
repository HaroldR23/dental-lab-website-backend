from mangum import Mangum

from api import create_app

app = create_app()

handler = Mangum(app)
