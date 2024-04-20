# 循环对话也记忆了？？
# 导入所需的库和模块
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


# 定义一个命令行聊天机器人的类
class CommandlineChatbot:
    # 在初始化时，设置花卉行家的角色并初始化聊天模型
    def __init__(self):
        self.chat = ChatOpenAI()
        self.messages = [SystemMessage(content="你是一个花卉行家。")]

    # 定义一个循环来持续与用户交互
    def chat_loop(self):
        print("Chatbot 已启动! 输入'exit'来退出程序。")
        while True:
            user_input = input("你: ")
            # 如果用户输入“exit”，则退出循环
            if user_input.lower() == "exit":
                print("再见!")
                break
            # 将用户的输入添加到消息列表中，并获取机器人的响应
            self.messages.append(HumanMessage(content=user_input))
            response = self.chat.invoke(self.messages)
            print(f"Chatbot: {response.content}")


# 如果直接运行这个脚本，启动聊天机器人
if __name__ == "__main__":
    bot = CommandlineChatbot()
    bot.chat_loop()


# Chatbot 已启动! 输入'exit'来退出程序。
# 你: 我姐姐明天要过生日，我需要一束生日花束
# Chatbot: 那真是个美好的礼物选择！你知道你姐姐喜欢什么样的花吗？她有任何特别喜欢的颜色或花朵吗？
# 你: 她喜欢粉色玫瑰，颜色是粉色的。
# Chatbot: 那听起来很美！粉色玫瑰是一种绝佳的选择，可以传达出温柔和浪漫的感觉。你可以考虑配上一些其他粉色或白色的花朵，例如粉色康乃馨、粉色或白色洋桔梗、粉色或白色满天星等，
# 来增加花束的层次和美感。最后，你可以选择一款精美的包装纸和蝴蝶结，让整束花更加精致。这样的生日花束肯定会让你姐姐感到惊喜和欢喜！
# 你: 我又来了，还记得我昨天为什么要来买花吗？
# Chatbot: 当然记得！你姐姐明天要过生日，你想为她准备一束粉色玫瑰的花束。
