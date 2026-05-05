<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>AI 自动生成小游戏工厂下载</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f9f9f9; }
        h1 { color: #333; }
        button { margin-top: 20px; padding: 10px 20px; font-size: 16px; border: none; background-color: #4CAF50; color: white; border-radius: 5px; cursor: pointer; }
        button:hover { background-color: #45a049; }
    </style>
</head>
<body>
    <h1>AI 自动生成小游戏工厂</h1>
    <p>点击下面的按钮下载整个项目 zip 包：</p>
    <button onclick="downloadZip()">下载项目 ZIP</button>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"></script>
    <script>
        function downloadZip() {
            const zip = new JSZip();

            // 添加 Python 文件
            const pythonCode = `import openai
import json
from datetime import datetime

API_KEY = "YOUR_API_KEY"  # 请改为环境变量或实际 Key
MODEL = "gpt-4o-mini"

openai.api_key = API_KEY

def generate_game_plan(user_input):
    prompt = f"""
你是一个资深游戏策划专家。
用户提供创意需求: \"{user_input}\"
请生成一份完整的小游戏策划方案...
"""
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=600
    )
    return response.choices[0].message.content.strip()

def generate_visual_prompts(game_plan):
    prompt = f"""
你是一个游戏视觉设计专家。
根据游戏策划方案生成角色和场景提示词...
"""
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=400
    )
    return response.choices[0].message.content.strip()

class TokenTracker:
    def __init__(self):
        self.total_tokens = 0
    def add(self, tokens):
        self.total_tokens += tokens
    def report(self):
        print(f"[{datetime.now()}] 已消耗约 {self.total_tokens} Tokens")

def main():
    tracker = TokenTracker()
    user_input = input("请输入你的小游戏创意：")
    game_plan = generate_game_plan(user_input)
    print("\n=== 游戏策划方案 ===")
    print(game_plan)
    tracker.add(600)
    visual_prompts = generate_visual_prompts(game_plan)
    print("\n=== 视觉提示词 ===")
    print(visual_prompts)
    tracker.add(400)
    tracker.report()

if __name__ == "__main__":
    main()`;
            zip.file('ai_game_factory.py', pythonCode);

            // 添加 README.md
            const readme = `# AI 自动生成小游戏工厂

这是一个示例项目，演示如何使用 AI 自动生成小游戏策划方案和视觉提示词。

## 文件说明
- ai_game_factory.py：Python 代码文件
- index.html：网页文件，可点击下载项目

## 使用方法
1. 设置环境变量或在代码中替换 API_KEY
2. 运行 ai_game_factory.py
3. 输入小游戏创意，即可生成策划方案和提示词
`;
            zip.file('README.md', readme);

            // 添加 index.html
            const htmlContent = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>AI 自动生成小游戏工厂</title>
</head>
<body>
<h1>AI 自动生成小游戏工厂</h1>
<p>点击下载 Python 文件即可运行示例。</p>
</body>
</html>`;
            zip.file('index.html', htmlContent);

            zip.generateAsync({type:"blob"})
            .then(function(content) {
                const a = document.createElement('a');
                a.href = URL.createObjectURL(content);
                a.download = 'ai_game_factory_project.zip';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
            });
        }
    </script>
</body>
</html>