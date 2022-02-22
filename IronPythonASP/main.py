import clr
clr.AddReference('System.Console')
clr.AddReference('Microsoft.AspNetCore')
clr.AddReference('Microsoft.AspNetCore.Routing')

from System import Console, Array, Byte
from Microsoft.AspNetCore.Builder import WebApplication, EndpointRouteBuilderExtensions

builder = WebApplication.CreateBuilder()

app = builder.Build()

def handle_get(ctx):
    return ctx.Response.Body.WriteAsync(Array[Byte](b'hello there'), 0, 11)

EndpointRouteBuilderExtensions.MapGet(app, '/', handle_get)

app.Run()
