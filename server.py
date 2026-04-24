from mcp.server.fastmcp import FastMCP 

# bind host to internal network interface IP on port 8080
## for intermountain ists
mcp = FastMCP("hello-server", host="0.0.0.0")

@mcp.tool()
def hello(name: str = "World") -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")