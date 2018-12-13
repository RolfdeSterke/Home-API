from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from controllers.TodoResource import TodoResource, TodosResource, HiddenResource
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://dev:secret@127.0.0.1:3306/home_api'  # 'mysql://username:password@ip:port/databasename'
app.config['HOMELYNK_URI'] = 'http://remote:Selficient@10.1.1.10/scada-remote/request.cgi?m=json&r=grp&fn=write&'
CORS(app)
api = Api(app)


api.add_resource(TodosResource, '/api/todos')
api.add_resource(TodoResource, '/api/todos/<int:todo_id>')
api.add_resource(HiddenResource, '/api/todos/hidden=True')


if __name__ == "__main__":
    from db import db
    db.init_app(app)

    app.run(debug=True, host='0.0.0.0')

