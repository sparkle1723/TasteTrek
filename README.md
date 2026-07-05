# 🍜 TasteTrek — Event Management System

> **A Flask-based web application for discovering and booking culinary events.**  
> Built as part of IFQ557 Assessment 2 — Final Solution.

---

## 📖 Table of Contents / 目录

- [English](#english)
- [中文](#中文)

---

## English

### Overview

TasteTrek is a full-stack event management web application where users can browse food festivals, book tickets, post comments, create and manage events, and track booking history. Built with Python Flask, SQLAlchemy, WTForms, and Bootstrap 5.

### Features

| Feature | Description |
|---------|-------------|
| **User Authentication** | Register, login/logout with Flask-Login, password hashing via Werkzeug |
| **Landing Page** | Hero carousel, category filtering, text search, result count, 3×3 event grid |
| **Event Details** | Image, description, date/time, venue, status badges, ticket availability |
| **Booking System** | Login-required booking with quantity input, order confirmation page, booking history |
| **Comments** | Character counter, avatar initials, timestamps, visible to all users |
| **Event CRUD** | Create / update (except status) / cancel events; owner-only actions |
| **Auto Status Management** | Open → Sold Out (when tickets exhausted) → Inactive (when date passed) |
| **My Events Page** | Dashboard for event owners to manage their created events |
| **Error Handling** | Custom 404, 403, 500 pages; CSRF error handling |
| **Responsive Design** | Bootstrap 5, hover animations, rounded cards, intuitive UX |

### Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python 3, Flask 3.1.0 |
| ORM | Flask-SQLAlchemy, SQLAlchemy 2.0.36 |
| Forms | Flask-WTF, WTForms 3.2.1 |
| Auth | Flask-Login, Werkzeug 3.1.3 |
| Frontend | HTML, CSS, Bootstrap 5, Jinja2 |
| Database | SQLite |

### Project Structure

```
a3_groupX/
├── main.py                    # Entry point
├── requirements.txt           # Dependencies
├── instance/
│   └── tastetrek.db           # SQLite database (auto-seeded)
└── tastetrek/                 # Application package
    ├── __init__.py             # Flask app factory
    ├── models.py               # User, Event, Booking, Comment models
    ├── forms.py                # WTForms definitions
    ├── seed_data.py            # Seed data (3 users, 9 events)
    ├── routes/
    │   ├── main.py             # Landing page (search, filter)
    │   ├── auth.py             # Register, login, logout
    │   ├── events.py           # Event CRUD + comments
    │   └── bookings.py         # Booking + confirmation
    ├── static/style/
    │   └── style.css           # Custom styles
    └── templates/              # 13 Jinja2 templates
```

### Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the application
python main.py

# 3. Open browser
# http://127.0.0.1:5000
```

The database and seed data (3 users, 9 events, 3 bookings, 3 comments) are created automatically on first run.

### Demo Accounts

| Name | Email | Password |
|------|-------|----------|
| Alice Wang | `alice@example.com` | `password123` |
| Bob Smith | `bob@example.com` | `password123` |
| Carol Chen | `carol@example.com` | `password123` |

---

## 中文

### 概述

TasteTrek 是一个全栈事件管理 Web 应用，用户可以浏览美食节、预订门票、发表评论、创建和管理活动、查看预订历史。基于 Python Flask、SQLAlchemy、WTForms 和 Bootstrap 5 构建。

### 功能特性

| 功能 | 说明 |
|------|------|
| **用户认证** | 注册、登录/登出，密码哈希加密（Werkzeug） |
| **首页** | 轮播图、分类筛选、全文搜索、结果计数、3×3 事件网格 |
| **事件详情** | 图片、描述、日期时间、场地、状态徽章、余票显示 |
| **预订系统** | 需登录，数量输入，订单确认页，预订历史 |
| **评论系统** | 字符计数、首字母头像、时间戳、所有人可见 |
| **事件管理** | 创建 / 更新（不含状态）/ 取消，仅所有者可操作 |
| **状态自动管理** | Open → Sold Out（售罄）→ Inactive（日期已过） |
| **我的事件页** | 事件创建者管理面板 |
| **错误处理** | 自定义 404、403、500 页面；CSRF 过期友好提示 |
| **响应式设计** | Bootstrap 5，悬停动画，圆角卡片，直观交互 |

### 技术栈

| 组件 | 技术 |
|------|------|
| 后端 | Python 3, Flask 3.1.0 |
| ORM | Flask-SQLAlchemy, SQLAlchemy 2.0.36 |
| 表单 | Flask-WTF, WTForms 3.2.1 |
| 认证 | Flask-Login, Werkzeug 3.1.3 |
| 前端 | HTML, CSS, Bootstrap 5, Jinja2 |
| 数据库 | SQLite |

### 项目结构

```
a3_groupX/
├── main.py                    # 启动入口
├── requirements.txt           # 依赖清单
├── instance/
│   └── tastetrek.db           # SQLite 数据库（自动初始化）
└── tastetrek/                 # 应用包
    ├── __init__.py             # Flask 工厂函数
    ├── models.py               # User、Event、Booking、Comment 模型
    ├── forms.py                # WTForms 表单定义
    ├── seed_data.py            # 种子数据（3用户、9事件）
    ├── routes/
    │   ├── main.py             # 首页（搜索、筛选）
    │   ├── auth.py             # 注册、登录、登出
    │   ├── events.py           # 事件 CRUD + 评论
    │   └── bookings.py         # 预订 + 确认页
    ├── static/style/
    │   └── style.css           # 自定义样式
    └── templates/              # 13 个 Jinja2 模板
```

### 快速启动

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行应用
python main.py

# 3. 打开浏览器
# http://127.0.0.1:5000
```

首次运行会自动创建数据库并填充种子数据（3个用户、9个事件、3条预订、3条评论）。

### 演示账号

| 姓名 | 邮箱 | 密码 |
|------|------|------|
| Alice Wang | `alice@example.com` | `password123` |
| Bob Smith | `bob@example.com` | `password123` |
| Carol Chen | `carol@example.com` | `password123` |

---