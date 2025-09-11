import sys
from app import create_app

app = create_app()

if __name__ == "__main__":
    try:
    # for running on custom ports
        port = int(sys.argv[1])
    except Exception:
        port = 5000
        
    print(f"http://localhost:{port}/apidocs/")
    app.run(host='0.0.0.0', port=port, debug=True)
