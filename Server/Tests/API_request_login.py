import requests


class TestLogin:
        url = "https://trip-yoetz.herokuapp.com/auth/login"

        def test_login_correct(self):
            body = {"email":"miki@gmail.com","password":"12345"}
            res = requests.post(self.url,json= body)
            response = res.json()
            assert response["success"] == True
            assert response["message"] == "login successful"
            assert res.elapsed.total_seconds() < 10
            assert res.status_code == 200
            print(res.status_code)
            print(response["message"],response["success"])



        def test_login_with_invalid_details(self):
                 body = {'email': "mik@fsg", 'password': "177777723"}
                 res = requests.post(self.url ,data= body)
                 response = res.json()
                 assert response["success"] == False
                 assert response["message"] == 'no user found'
                 assert res.elapsed.total_seconds() < 10
                 assert res.status_code == 400
                 print (res.status_code)
                 print(response["success"], response["message"])


        def test_login_inorrect_email(self):
                body = {'email': "mik", 'password': "17777772"}
                res = requests.post(self.url, data=body)
                response = res.json()
                assert response["success"] == False
                assert response["message"] == 'no user found'
                assert res.elapsed.total_seconds() < 10
                assert res.status_code == 400
                print(res.status_code)
                print(response["success"], response["message"])



        def test_login_with_empty_password(self):
                body = {'email': "miki@gmail.com", 'password': ""}
                res = requests.post(self.url, data=body)
                response = res.json()
                assert response["success"] == False
                assert response["message"] == "password or email incorrect"
                assert res.elapsed.total_seconds() <10
                assert res.status_code == 400
                print(res.status_code)
                print(response["success"], response["message"])





        def test_login_with_empty_fields(self):
            body = {"email":"","password":""}
            res = requests.post(self.url,data=body)
            response = res.json()
            assert response["success"] == False
            assert response["message"] == "password or email incorrect"
            assert res.elapsed.total_seconds() < 10
            assert res.status_code == 400
            print(res.status_code)
            print(response["success"], response["message"])












