# 臭氧催化氧化体系催化剂推荐系统

这是一个基于 Flask 的网络应用程序，用于推荐臭氧催化氧化体系的催化剂。

## 功能特点

- 通过 CAS 号查询化合物信息
- 显示化合物的 pKa 值和反应倾向
- 推荐最适合的催化剂
- 提供不同 pH 值下的催化效率数据

## 技术栈

- HTML5
- CSS3
- JavaScript
- Flask
- SQLite

## 本地运行

1. 克隆仓库：
```bash
git clone [repository-url]
cd chemical_app
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 运行应用：
```bash
python app.py
```

4. 在浏览器中访问：
```
http://localhost:5000
```

## 示例 CAS 号

- 108-95-2（苯酚）
- 121-12-0（甲基酚）
- 108-39-4（间甲酚）

## 许可证

MIT License 