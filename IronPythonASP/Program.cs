using IronPython.Hosting;
using Microsoft.Scripting.Hosting;

ScriptEngine engine = Python.CreateEngine();
engine.ExecuteFile("main.py");
