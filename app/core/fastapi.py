from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.requests import Request


class CustomFastAPI(FastAPI):
    """
    CustomFastAPI adds servers to the FastAPI Open Schema generation.
    """
    def setup(self) -> None:
        if self.openapi_url:
            async def openapi(req: Request) -> JSONResponse:
                schema = self.openapi()
                schema["servers"] = [{
                    "url": str(req.base_url)
                }]
                return JSONResponse(schema)
            self.add_route(self.openapi_url, openapi, include_in_schema=False)
        super().setup()