from app import create_app

app = create_app()

def handler(request):
    return app
