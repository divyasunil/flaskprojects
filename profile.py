from flask import Flask

new_profile = Flask(__name__)


@new_profile.route('/profile/<username>')
def profile(username):
    return '<h1>Profile of %s</h1>' % username


@new_profile.route('/profile/<int:id>')
def profileid(id):
    return '<h1>Profile ID is: %d</h1>' % id


# new_profile.run()
new_profile.run(debug=True) # proper reload
