import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="adr-viewer")
def adr_viewer(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('record-id')

    if name:
        return func.HttpResponse("converted-to-html: 0001-FirstAdr")
    else:
        return func.HttpResponse(
            "<p><em>This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.</em></p>",
            headers={"Content-Type": "text/html"},
            status_code=401
        )
