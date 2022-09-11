from services import BaseService
from models import User
from repositories import roles_repo


roles_service = BaseService(User, roles_repo)