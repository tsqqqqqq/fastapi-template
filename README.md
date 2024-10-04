# fastapi-template
FastApi Template

## Requirement

python3.8 及以上

    
## 快速开始

1. 克隆项目
    ```shell
      git clone
    ```
2. 创建虚拟环境
   ```
   python3 -m venv venv
   ```
3. 使用虚拟环境并且安装依赖
   ```shell
   pip install -r extras/requirements.txt
   ```
4. 配置环境变量

   复制.env.example文件，创建新文件.env, 补充该新文件中的xxx部分。 省事一点的话就直接找接手的负责人要.env文件就行
   ```markdown
     # app
        ADMIN_EMAIL=xxxxxx # 管理员邮箱，随便填 反正用不到
        APP_HOST=xxx.xxx.xxx.xxx # 项目启动host，最好 0.0.0.0
        APP_PORT=xxxx # 项目启动的端口号 默认是8000
   
     # log path
        LOG_PATH=xxxx # 日志路径
        LOG_FILE_NAME=xxxx # 日志文件名
        LOG_LEVEL=xxx # 日志级别 默认是INFO
   
     # db 数据库相关信息
        DB_HOST=xxxxx
        DB_PORT=xxxxx
        DB_USERNAME=xxxxx
        DB_PASSWORD=xxxxxx
        DB_DATABASES=xxxxx
   ```
5. 运行项目

   下面两个命令都可以让项目跑起来

   ```shell
      python main.py
   ```
   
   ```shell
      uvicorn main:app --reload --host 0.0.0.0
   ```

## 数据库相关
   如果是在本地开发，则先在本地数据库中创建一个库，库名跟你env文件配置的库名保持一致就好 **服务器的是 issue_editor**

## 代码结构
```markdown
 |- config   # 配置文件
 |- database # 数据库相关，包含model层
 |- extras   # 文档信息相关
 |- routers  # 路由相关
 |- schemas  # python3.9 开始的强调数据类型规范，这里可以直接映射到model层，详情可以关注fastapi中的schemas作用
 |- script   # 各种脚本
 |- utils    # 工具类
```
