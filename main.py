from click import File
from website import create_app
from flask_sslify import SSLify




app = create_app()

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'), host='0.0.0.0', port=5000)
    
  
    
    
