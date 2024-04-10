from langchain_community.utilities import SerpAPIWrapper


# 重新定制SerpAPIWrapper，重构_process_response，返回URL
class CustomSerpAPIWrapper(SerpAPIWrapper):
    def __init__(self):
        super(CustomSerpAPIWrapper, self).__init__()

    @staticmethod
    def _process_response(res: dict) -> str:
        """Process response from SerpAPI."""
        if "error" in res.keys():
            raise ValueError(f"Got error from SerpAPI: {res['error']}")
        if "answer_box_list" in res.keys():
            res["answer_box"] = res["answer_box_list"]
        """删去很多无关代码"""
        snippets = []
        if "knowledge_graph" in res.keys():
            knowledge_graph = res["knowledge_graph"]
            title = knowledge_graph["title"] if "title" in knowledge_graph else ""
            if "description" in knowledge_graph.keys():
                snippets.append(knowledge_graph["description"])
            for key, value in knowledge_graph.items():
                if (
                    isinstance(key, str)
                    and isinstance(value, str)
                    and key not in ["title", "description"]
                    and not key.endswith("_stick")
                    and not key.endswith("_link")
                    and not value.startswith("http")
                ):
                    snippets.append(f"{title} {key}: {value}.")
        if "organic_results" in res.keys():
            # 结果不一定是获取到微博的博主地址
            # 这里对获取到的数据进行过滤
            first_organic_result = next(
                (
                    item
                    for item in res["organic_results"]
                    if "https://weibo.com/u" in item["link"]
                    or "https://m.weibo.cn/u/" in item["link"]
                ),
                None,
            )
            if "snippet" in first_organic_result.keys():
                # 此处是关键修改
                # snippets.append(first_organic_result["snippet"])
                snippets.append(first_organic_result["link"])
            elif "snippet_highlighted_words" in first_organic_result.keys():
                snippets.append(first_organic_result["snippet_highlighted_words"])
            elif "rich_snippet" in first_organic_result.keys():
                snippets.append(first_organic_result["rich_snippet"])
            elif "rich_snippet_table" in first_organic_result.keys():
                snippets.append(first_organic_result["rich_snippet_table"])
            elif "link" in first_organic_result.keys():
                snippets.append(first_organic_result["link"])
        if "buying_guide" in res.keys():
            snippets.append(res["buying_guide"])
        if "local_results" in res.keys() and "places" in res["local_results"].keys():
            snippets.append(res["local_results"]["places"])

        if len(snippets) > 0:
            return str(snippets)
        else:
            return "No good search result found"


# 获取与某种鲜花相关的微博UID的函数
def get_UID(flower: str):
    """Searches for Linkedin or twitter Profile Page."""
    # search = SerpAPIWrapper()
    search = CustomSerpAPIWrapper()
    res = search.run(f"{flower}")
    return res
