from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN")
SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.str('DEBUG')


