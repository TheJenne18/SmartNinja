from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("about.html", name=request.cookies.get("user_name"))

@app.route("/contact", methods=["POST", "GET"])
def contact():
    contact_name = "Jens Polspoel"
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_message)

    response = make_response(render_template("success.html"))
    response.set_cookie("user_name", contact_name)

    return response


app.run()