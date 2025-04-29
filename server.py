from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# 서버 초기화
mcp = FastMCP("name-origin")

# API 기반 URL
base_url = "https://api.nationalize.io"


# 예제도 정의
@mcp.tool()
async def predict_origin(name: str) -> dict:
    """Nationalize API를 사용하여 주어진 이름의 출신 국가를 예측합니다

    Args:
        name (str): 출신 국가를 예측할 이름

    Returns:
        dict: 이름의 출신 국가
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{base_url}/name={name}")
        return response.json()


# 배치도 정의
@mcp.tool()
async def batch_predict(names: list[str]) -> dict:
    """여러 이름의 출신 국가를 한 번에 예측합니다

    Args:
        names (list[str]): 출신 국가를 예측할 이름 목록

    Returns:
        dict: 이름들의 출신 국가
    """
    results = {}
    for name in names:
        results[name] = await self.predict_origin(name)
    return results


if __name__ == "__main__":
    print("이름 출신 국가 서버 시작 중...")
    mcp.run(transport="stdio")
