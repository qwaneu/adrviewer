import azure.functions as func
from function_app import adr_viewer
from hamcrest import *

class TestE2ERequest:
    def test_responds_with_a_message(self):
        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/adr-viewer',
            params={'record-id': '0001-FirstAdr'})
        func_call = adr_viewer.build().get_user_function()
        resp = func_call(req)
        assert_that(resp.get_body().decode(), equal_to("converted-to-html: 0001-FirstAdr"))
