from flask import Flask
from flask_restful import Api, Resource, reqparse
import networkx as nx
from networkx.readwrite import json_graph

serveradress = "127.0.0.1"
serverport = 3000

app = Flask(__name__)
api = Api()


class Main(Resource):
    def get(self, user_id):
        social_graph = nx.read_gml('graph.txt')
        if user_id == '0':
            return json_graph.node_link_data(social_graph)
        if user_id in social_graph:
            out = []
            for a in social_graph[user_id]:
                out.append({"user_id": a, "contacts": social_graph[user_id][a]['weight']})
            return out
        else:
            return "wrong user id"

    def post(self, user_id):
        social_graph = nx.read_gml('graph.txt')
        parser = reqparse.RequestParser()
        parser.add_argument("contact_id", type=str)
        contact_id = parser.parse_args()["contact_id"]
        if social_graph.has_edge(user_id, contact_id):
            social_graph[user_id][contact_id]['weight'] += 1
        else:
            social_graph.add_edge(user_id, contact_id, weight=1)
        nx.write_gml(social_graph, 'graph.txt')
        return json_graph.node_link_data(social_graph)


api.add_resource(Main, "/api/<string:user_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(port=serverport, host=serveradress)