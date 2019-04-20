import unittest
from app import app
import flask
from app.forms import ContactForm
from werkzeug.datastructures import MultiDict
from app import views


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.testing = True
        self.client.testing = True
        app.config['WTF_CSRF_ENABLED'] = False

    def tearDown(self):
        pass

    def test_index_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    # def test_index_context(self):
    #     with app.test_request_context('/'):
    #         print(flask.request.a)

    def test_valid_form_post(self):
        valid_data = dict(nom='SAM', email='sam@gmail.com', message='be cool')
        response = self.client.post('/', data=valid_data, follow_redirects=True)
        # test response
        self.assertEqual(response.status_code, 200)
        # test flash message
        assert b'merci pour votre message' in response.data
        # test mail well sent


    def test_invalid_form_post(self):
        invalid_data = dict(nom='SAM', email='samgmail.com', message='be cool')
        response = self.client.post('/', data=invalid_data, follow_redirects=True)
        # test flash message
        assert b'le formulaire comporte des erreurs' in response.data


    def test_form(self):
        with app.test_request_context():
            form = ContactForm(MultiDict([('nom', 'jerry'),('email', 'jerry@mail.com')]))
            self.assertEqual(form.validate(), False)
            print(form.errors)

if __name__ == '__main__':
    unittest.main()