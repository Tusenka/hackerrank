from flask import Flask, Response, render_template
app = Flask(__name__)
FILE='response.json'

@app.route('/1000/prompt/context/<id>', methods=['POST'])
def get_educations(id):
    educations=render_template('response.json', context= {'id': id})
    return Response(response=educations,
                    status=200,
                    mimetype="application/json")
                    
if __name__ == '__main__':
   app.run(port=443, ssl_context=("server_chain.pem", "server.key"))
   