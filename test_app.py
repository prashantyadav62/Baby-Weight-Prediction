from app import app

def test_hello_route_success():
    tester = app.test_client()
    response = tester.get('/hello')

    assert response.status_code == 200





# def test_hello_route_failure():
#     tester = app.test_client()
#     response = tester.get('/hello')

#     assert response.status_code == 500



## positive test case for '/predict' route

def test_predict_route_success():
    tester = app.test_client()
    data = {
        'gestation': [270],
        'parity': [0],
        'age': [27],
        'height': [165],
        'weight': [68],
        'smoke': [0]
    }
    response = tester.post('/predict', json=data)

    assert response.status_code==200
    