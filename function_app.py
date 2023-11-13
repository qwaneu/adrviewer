import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="adr-viewer")
def adr_viewer(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"<h1>Hello, {name}. This HTTP triggered function executed successfully.</h1>")
    else:
        return func.HttpResponse(
             "<p><em>This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.</em></p>",
             headers={"Content-Type": "text/html"},
             status_code=200
        )