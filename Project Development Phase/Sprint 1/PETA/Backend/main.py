from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

account_put_args = reqparse.RequestParser()
account_put_args.add_argument("name", type=str, help="Name of the Account is required", required=True)
account_put_args.add_argument("email", type=str, help="Email of the Account is required", required=True)
account_put_args.add_argument("password", type=str, help="Password of the Account is required", required=True)

Accounts = {}

def abort_if_account_id_doesnt_exist(account_id):
    if account_id not in Accounts:
        abort(404, message="account_id is not valid....")

def abort_if_account_exist(account_id):
    if account_id in Accounts:
        abort(409, message="Account already exist with same account_id ......")


class Account(Resource):
    def get(self, account_id):
        abort_if_account_id_doesnt_exist(account_id)
        return Accounts[account_id]
    
    def put(self,account_id):
        abort_if_account_exist(account_id)
        args = account_put_args.parse_args()
        Accounts[account_id] = args
        return Accounts[account_id], 201

    def delete(self, account_id):
        abort_if_account_id_doesnt_exist(account_id)
        del Accounts[account_id]
        return '', 204

        

api.add_resource(Account, "/account/<int:account_id>")

if __name__ == "__main__":
    app.run(debug=True)


























# BASIC GET API

# class HelloWorld(Resource):
#     def get(self):
#         return {"data" : "Hello World"}

# api.add_resource(HelloWorld, "/helloworld")