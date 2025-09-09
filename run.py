import sys
from app import create_app

if __name__ == "__main__":
    app = create_app()
        
    try:
        # for running on custom ports
        port = int(sys.argv[1])
    except Exception:
        port = 5000
        
    app.run(host='0.0.0.0', port=port, debug=True)
