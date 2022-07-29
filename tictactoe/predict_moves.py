import json
import requests

temp = {
"board": [
    0, 0, 0,
    0, 1, 1,
    0, 2, 2
    ],
"values": [0, 1, 2]
}
def predict_best_move(board, values, tries=5):
    body = {
        "board": board,
        "values": values
    }
    for i in range(0, tries):
        r = requests.post("http://localhost:4000/v1/move", data=json.dumps(body))
        if r.status_code == 200: return int(r.text)
    return -1