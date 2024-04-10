# 导入所取的库
import re
from agents.weibo_agent import lookup_V
from tools.scraping_tool import get_data
from tools.general_tool import remove_non_chinese_fields
from tools.textgen_tool import generate_letter


def find_bigV(flower: str):
    # 拿到UID
    response_UID = lookup_V(flower_type=flower)
    # print(response_UID)

    # 抽取UID里面的数字
    UID = re.findall(r"\d+", response_UID)[0]
    # print("这位鲜花大V的微博ID是", UID)

    # 根据UID爬取大V信息
    person_info = get_data(UID)
    # print(person_info)

    # 移除无用的信息
    remove_non_chinese_fields(person_info)
    # print(person_info)

    # 调用函数根据大V信息生成文本
    result = generate_letter(information=person_info)
    return result
