from .routes import Routes
from app.internal import router


__routes__ = Routes(routes=(router,))
