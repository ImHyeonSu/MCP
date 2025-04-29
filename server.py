from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# 初期化
mcp = FastMCP("name-origin")

base_url = "https://api.nationalize.io"

@mcp.tool()
async def predict_origin(name: str) -> dict:
    """Nationalize APIを使用して、指定された名前の出身国を予測します

    引数:
        name (str): 出身国を予測する名前

    戻り値:
        dict: 名前の出身国
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{base_url}/name={name}")
        return response.json()


# 배치도 정의
@mcp.tool()
async def batch_predict(names: list[str]) -> dict:
    """複数の名前の出身国を一度に予測します

    引数:
        names (list[str]): 出身国を予測する名前のリスト

    戻り値:
        dict: 名前ごとの出身国
    """
    results = {}
    for name in names:
        results[name] = await self.predict_origin(name)
    return results


if __name__ == "__main__":
    print("名前の出身国サーバー起動中...")
    mcp.run(transport="stdio")
