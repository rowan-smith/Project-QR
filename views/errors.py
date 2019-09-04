from flask import Blueprint, render_template, request

errors = Blueprint('errors', __name__)


# Error handle 404 (Page Not Found)
@errors.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404

# Error handle 500 (Internal Server Error)
@errors.errorhandler(500)
def internal_server_error(error):
    return render_template("errors/500.html"), 500

# Error handle 401 (Unauthorized Access)
@errors.errorhandler(401)
def unauthorized_access(error):
    return render_template("errors/401.html"), 401

# Error handle all
@errors.errorhandler(Exception)
def unhandled_exception(error):
    errors.logger.error(f"Unhandled Exception: {error}")
    return render_template('errors/UnknownError.html')