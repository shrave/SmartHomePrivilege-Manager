#!/user/bin/env python
import click

from app import create_app, db, models, forms
from tests import test_app
from flask import jsonify
from flask import request
import json

app = create_app()


# flask cli context setup
@app.shell_context_processor
def get_context():
	"""Objects exposed here will be automatically available from the shell."""
	return dict(app=app, db=db, models=models, forms=forms)


@app.cli.command()
def create_db():
	"""Create the configured database."""
	db.create_all()

@app.route("/test", methods=["POST"])
def test():
	print(request.get_json(force = True))
	d = request.get_json(force = True)
	user_request_dict = json.loads(d)
	user_name = user_request_dict['User']
	task_name = user_request_dict['Task']
	# print(user_name, task_name)
	return jsonify(request.json)


@app.cli.command()
@click.confirmation_option(prompt='Drop all database tables?')
def drop_db():
	"""Drop the current database."""
	db.drop_all()


if __name__ == '__main__':
	app.run()
