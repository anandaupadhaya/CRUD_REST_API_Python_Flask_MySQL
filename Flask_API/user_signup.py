from app import app

@app.route("/user_signup")
def user_signup():
    return(" This is the signup page")