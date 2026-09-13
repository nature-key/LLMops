from pkg import HttpCode

import pytest

class TestAppHandler:


    @pytest.mark.parametrize('query', [None,"你好，你是？"])
    def test_completion(self, query, client):
        r = client.post("/chat/completion", json={"query": query})
        print(f"query: {query}, r.json: {r.json}")
        print('-----------------')
        assert r.status_code == 200
        print(f"code: {r.json.get('code')}")

        # if query is None:
        #     # assert r.json.get("code") == HttpCode.VALIDATE_ERROR
        # else:
        #     # assert r.json.get("code") == HttpCode.SUCCESS