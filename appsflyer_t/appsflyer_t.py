from flask import Flask
from flask import request
import json
from date.t_clean import t_clean_json
from date.track_logs import track_logs

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/callback/soloads',methods=['POST','GET'])
def callback():
    data = {
        "code": 0,
        "msg": "ok",
        "result": 0
    }
    return json.dumps(data)

@app.route('/api/v4/androidevent', methods=['POST',])
def android():
    if request.method== "POST":
        app_info ={}
        buildnumber = request.args.get('buildnumber')
        app_id = request.args.get('app_id')
        app_info['buildnumber'] = buildnumber
        app_info['app_id'] = app_id
        print(app_info)
        try:
            data = request.get_json(force=True)
            headers = json.dumps(dict(request.headers))
            data_b = json.dumps(dict(data))
            datas = json.loads(data_b)
            print(datas['sdk'])
            print(headers,type(headers))
            t_clean_json(datas,headers,app_info)
            return json.dumps({"status": 200, "result": 300})
        except Exception as e:
            print(e)
            return json.dumps({"status": 500, "message": "用户信息加载失败"})


@app.route('/api/trace_log',methods=['POST','GET'])
def trace_log():
    try:
        data = request.get_json(force=True)
        track_logs(data)
        return json.dumps({"status": 200, "result": 300})
    except Exception as e:
        print(e)
        return json.dumps({"status": 500, "message": "用户信息加载失败"})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=False)
