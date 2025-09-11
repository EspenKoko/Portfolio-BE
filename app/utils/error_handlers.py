def error_handlers(app):
    # TODO abstract somehow
    @app.errorhandler(400)
    def bad_request(error):
        return {"error": "Bad request", "message": str(error)}, 400
      
    # TODO why are the error messages inconsistent?
    @app.errorhandler(404) # this is called when abort(404) is triggered
    def not_found_error(error):
        return {"error": "Resource not found", "message": str(error)}, 404
    
    @app.errorhandler(409)
    def conflict(error):
        return {"error": "Server conflict", "message": str(error)}, 409
      
    @app.errorhandler(500)
    def internal_error(error):
        return {"error": "Internal server error", "message": str(error)}, 500
      