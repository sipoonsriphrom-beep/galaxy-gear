from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Galaxy Gear Backend is Running!"}

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Galaxy Gear Store API")

@app.get("/api/health")
def health_check():
    return {
        "status": "online",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "server": "Python FastAPI on Render"
    }

@app.get("/", response_class=HTMLResponse)
def serve_galaxy_gear_app():
    return """<!DOCTYPE html>
<html lang="th" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galaxy Gear - Fullstack Web & Playlist CD Player</title>
    <!-- Tailwind CSS & FontAwesome -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: {
                            purple: '#a855f7',
                            glow: '#c084fc',
                            orange: '#f97316',
                            cyan: '#06b6d4',
                            pyyellow: '#ffde57',
                            pyblue: '#4584b6'
                        }
                    },
                    boxShadow: {
                        'neon-purple': '0 0 20px -3px rgba(168, 85, 247, 0.5)',
                        'neon-orange': '0 0 20px -3px rgba(249, 115, 22, 0.4)',
                        'neon-green': '0 0 20px -3px rgba(34, 197, 94, 0.4)',
                        'neon-cyan': '0 0 20px -3px rgba(6, 182, 212, 0.4)',
                    }
                }
            }
        }
    </script>
    <style>
        body {
            background-color: #050711;
            background-image: linear-gradient(to bottom, rgba(5, 7, 17, 0.75), rgba(5, 7, 17, 0.88)), 
                              url('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM21lcm16em51dmk5dTIxanllbGo2OGMxODhjZjE1MHVxdm9wOHFkYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Fbox1ygIqnga5dLinz/giphy.gif');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: rgba(15, 23, 42, 0.6); }
        ::-webkit-scrollbar-thumb { background: rgba(168, 85, 247, 0.5); border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: rgba(168, 85, 247, 0.8); }

        .glass-card {
            background: rgba(15, 23, 42, 0.55);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .glass-card-hover {
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .glass-card-hover:hover {
            background: rgba(30, 41, 59, 0.75);
            border-color: rgba(168, 85, 247, 0.5);
            transform: translateY(-4px);
            box-shadow: 0 12px 24px -6px rgba(0, 0, 0, 0.5), 0 0 20px -3px rgba(168, 85, 247, 0.3);
        }

        .glass-nav {
            background: rgba(8, 12, 28, 0.85);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }

        .terminal-bg {
            background-color: #0d1117;
            font-family: 'Courier New', Courier, monospace;
        }

        /* CD Vinyl Spin Animation */
        @keyframes spinSlow {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
        .animate-spin-cd {
            animation: spinSlow 4s linear infinite;
        }
        .paused-spin {
            animation-play-state: paused;
        }

        @keyframes slideIn {
            from { transform: translateY(100%); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        .animate-toast { animation: slideIn 0.3s ease-out forwards; }
    </style>
</head>
<body class="font-sans text-gray-100 antialiased min-h-screen flex flex-col relative selection:bg-purple-500 selection:text-white pb-32">

    <!-- Header / Navbar -->
    <header class="glass-nav text-white p-4 sticky top-0 z-30 shadow-2xl">
        <div class="container mx-auto flex justify-between items-center max-w-7xl">
            <div class="flex items-center gap-3">
                <h1 class="text-2xl font-black tracking-wider cursor-pointer bg-gradient-to-r from-purple-400 via-fuchsia-300 to-indigo-400 bg-clip-text text-transparent hover:opacity-90 transition flex items-center gap-2" onclick="filterCategory('all')">
                    <span class="text-2xl filter drop-shadow-[0_0_8px_rgba(168,85,247,0.8)]">⚡</span> GALAXY GEAR
                </h1>
                <span class="hidden md:inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-mono bg-blue-950/80 border border-blue-500/40 text-blue-300">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                    Python 3.11 + FastAPI Server Active
                </span>
            </div>
            
            <div class="flex items-center gap-3">
                <button onclick="toggleTerminal()" class="hidden sm:flex items-center gap-2 bg-slate-900/80 hover:bg-slate-800 text-yellow-400 px-3 py-2 rounded-xl text-xs font-mono border border-yellow-500/30 shadow-lg transition active:scale-95">
                    <span>🐍</span> Python Logs
                </button>

                <div id="auth-section">
                    <button id="login-btn" onclick="openAuthModal('login')" class="bg-purple-600/70 hover:bg-purple-500/90 backdrop-blur-md px-4 py-2 rounded-xl text-xs font-bold transition-all shadow-neon-purple border border-purple-400/40 active:scale-95">
                        🔑 เข้าสู่ระบบ
                    </button>
                    <div id="user-info" class="hidden flex items-center gap-3 glass-card px-3.5 py-1.5 rounded-xl border border-purple-500/30">
                        <span id="user-credit-display" class="bg-emerald-950/80 border border-emerald-500/40 text-emerald-300 px-2.5 py-1 rounded-lg text-xs font-black shadow-neon-green">
                            💳 0 ฿
                        </span>
                        <span id="user-display-name" class="font-bold text-purple-300 text-xs"></span>
                        <button onclick="deleteAccountPrompt()" class="bg-red-500/20 hover:bg-red-500 text-red-300 hover:text-white px-2 py-1 rounded-lg text-xs font-semibold transition border border-red-500/30">
                            ลบบัญชี
                        </button>
                        <button onclick="logout()" class="bg-gray-700/50 hover:bg-gray-600 text-gray-300 px-2 py-1 rounded-lg text-xs font-semibold transition">
                            ออก
                        </button>
                    </div>
                </div>

                <button onclick="toggleCartModal()" class="glass-card hover:bg-gray-800/50 px-4 py-2 rounded-xl relative transition active:scale-95 border border-white/10 flex items-center gap-2 font-bold text-xs shadow-lg">
                    🛒 <span>ตะกร้า</span>
                    <span id="cart-count" class="bg-gradient-to-r from-purple-500 to-indigo-500 text-white text-[11px] px-2 py-0.5 rounded-full font-black shadow-neon-purple border border-white/20">0</span>
                </button>
            </div>
        </div>
    </header>

    <main class="container mx-auto p-4 md:p-6 flex-grow max-w-7xl">

        <div class="glass-card p-4 rounded-2xl mb-8 border border-blue-500/30 flex flex-col md:flex-row items-center justify-between gap-4 bg-gradient-to-r from-blue-950/30 via-purple-950/30 to-slate-950/40">
            <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-xl bg-gradient-to-tr from-brand-pyblue to-brand-pyyellow p-0.5 shadow-lg flex-shrink-0 flex items-center justify-center font-bold text-slate-900 text-xl">
                    🐍
                </div>
                <div>
                    <h2 class="text-sm font-bold text-blue-200 flex items-center gap-2">
                        Python Backend Simulation Engine Activated
                        <span class="bg-purple-500/20 text-purple-300 text-[10px] px-2 py-0.5 rounded border border-purple-400/30 font-mono">FastAPI + SQLite</span>
                    </h2>
                    <p class="text-xs text-gray-400 mt-0.5">
                        ทุกแอคชัน (สมัครสมาชิก, ล็อกอิน, ตะกร้าแยกผู้ใช้, ตัดเครดิต, สั่งซื้อ) ถูกประมวลผลด้วยจำลองโค้ด Python
                    </p>
                </div>
            </div>
            <div class="flex items-center gap-2 w-full md:w-auto justify-end">
                <button onclick="openPythonCodeModal()" class="w-full md:w-auto bg-blue-600/80 hover:bg-blue-500 text-white px-4 py-2 rounded-xl text-xs font-bold border border-blue-400/40 transition active:scale-95 shadow-neon-cyan flex items-center justify-center gap-1.5">
                    <span>📄</span> ดูโค้ด Python Backend สด
                </button>
            </div>
        </div>

        <!-- Admin Control Panel -->
        <section id="admin-add-product-section" class="hidden glass-card p-6 rounded-3xl shadow-2xl border border-purple-500/30 mb-10 space-y-6">
            <h2 class="text-xl font-black text-purple-400 flex items-center gap-2 tracking-wide">
                👑 แผงควบคุมผู้ดูแลระบบ (Admin Python Control)
            </h2>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="bg-gray-900/50 border border-emerald-500/30 p-4 rounded-2xl">
                    <h3 class="text-xs font-bold text-emerald-400 mb-3 flex items-center gap-1.5">
                        💳 Python API: POST /api/admin/add-credit
                    </h3>
                    <form id="add-credit-form" onsubmit="handleCreditSubmit(event)" class="grid grid-cols-1 sm:grid-cols-3 gap-2">
                        <select id="credit-target-user" class="bg-gray-900/90 border border-white/10 p-2.5 rounded-xl text-white text-xs focus:border-emerald-500 focus:outline-none">
                        </select>
                        <input type="number" id="credit-amount" placeholder="จำนวนเงิน (฿)" min="1" required class="bg-gray-900/90 border border-white/10 p-2.5 rounded-xl text-white placeholder-gray-500 text-xs focus:border-emerald-500 focus:outline-none">
                        <button type="submit" class="bg-emerald-600/80 hover:bg-emerald-500 border border-emerald-400/40 text-white font-bold p-2.5 rounded-xl transition active:scale-95 shadow-neon-green text-xs">
                            + เติมเครดิต
                        </button>
                    </form>
                </div>

                <div class="bg-gray-900/50 border border-purple-500/20 p-4 rounded-2xl">
                    <h3 class="text-xs font-bold text-purple-300 mb-3 flex items-center gap-1.5">
                        📦 Python API: POST /api/products
                    </h3>
                    <form id="add-product-form" onsubmit="handleFormSubmit(event)" class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                        <input type="text" id="prod-name" placeholder="ชื่อสินค้า" required class="bg-gray-900/90 border border-white/10 p-2 rounded-xl text-white text-xs focus:border-purple-500 focus:outline-none">
                        <input type="number" id="prod-price" placeholder="ราคา (เครดิต)" required class="bg-gray-900/90 border border-white/10 p-2 rounded-xl text-white text-xs focus:border-purple-500 focus:outline-none">
                        <select id="prod-category" class="bg-gray-900/90 border border-white/10 p-2 rounded-xl text-white text-xs focus:border-purple-500 focus:outline-none">
                            <option value="คีย์บอร์ด">คีย์บอร์ด</option>
                            <option value="เมาส์">เมาส์</option>
                            <option value="หูฟัง">หูฟัง</option>
                            <option value="แผ่นรองเมาส์">แผ่นรองเมาส์</option>
                        </select>
                        <input type="url" id="prod-img" placeholder="URL รูปภาพ (Optional)" class="bg-gray-900/90 border border-white/10 p-2 rounded-xl text-white text-xs focus:border-purple-500 focus:outline-none">
                        <button type="submit" class="col-span-1 sm:col-span-2 bg-purple-600/80 hover:bg-purple-500 border border-purple-400/40 text-white font-bold p-2.5 rounded-xl transition active:scale-95 shadow-neon-purple text-xs mt-1">
                            + เพิ่มสินค้าลง SQLite
                        </button>
                    </form>
                </div>
            </div>
        </section>

        <section class="mb-10">
            <div class="flex justify-between items-center mb-5">
                <div>
                    <h2 class="text-xl font-black text-transparent bg-clip-text bg-gradient-to-r from-white via-gray-200 to-gray-400 tracking-wide">
                        หมวดหมู่แนะนำ
                    </h2>
                    <p class="text-xs text-gray-400 mt-0.5">เลือกประเภทอุปกรณ์เกมมิ่งที่คุณต้องการ</p>
                </div>
                <button onclick="filterCategory('all')" class="text-xs font-bold glass-card hover:bg-gray-800/60 px-3.5 py-1.5 rounded-xl transition border border-white/10 text-purple-300 flex items-center gap-1">
                    ดูทั้งหมด <span>›</span>
                </button>
            </div>

            <div id="featured-categories" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5"></div>
        </section>

        <section class="mb-8">
            <h2 class="text-xs font-bold uppercase tracking-wider mb-3 text-purple-300/80">ตัวกรองหมวดหมู่</h2>
            <div id="category-buttons" class="flex flex-wrap gap-2"></div>
        </section>

        <div id="product-grid" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6"></div>
    </main>

    <!-- Floating Spinning CD Record Music Player with Playlist Selector -->
    <div class="fixed bottom-0 left-0 right-0 z-50 glass-nav border-t border-purple-500/40 p-3 px-6 flex items-center justify-between shadow-2xl">
        <div class="flex items-center gap-4">
            <!-- CD Disc Record with Cover Art -->
            <div onclick="toggleMusic()" class="relative w-12 h-12 rounded-full cursor-pointer group flex-shrink-0">
                <div id="cd-disc" class="w-full h-full rounded-full border-2 border-purple-400/60 overflow-hidden shadow-neon-purple p-0.5 bg-black relative animate-spin-cd">
                    <img id="cd-cover-img" src="https://img.youtube.com/vi/pP-0CzmxLE4/hqdefault.jpg" class="w-full h-full object-cover rounded-full">
                    <div class="absolute inset-0 m-auto w-3.5 h-3.5 rounded-full bg-slate-950 border border-purple-400/80 shadow-inner flex items-center justify-center">
                        <div class="w-1.5 h-1.5 rounded-full bg-slate-900"></div>
                    </div>
                </div>
                <div class="absolute inset-0 bg-black/50 rounded-full flex items-center justify-center opacity-0 group-hover:opacity-100 transition">
                    <i id="cd-hover-icon" class="fa-solid fa-pause text-white text-xs"></i>
                </div>
            </div>

            <div>
                <!-- Playlist Select Dropdown -->
                <div class="flex items-center gap-2 mb-0.5">
                    <select id="playlist-select" onchange="changeTrack(this.value)" class="bg-gray-900/90 border border-purple-500/40 text-purple-200 text-xs font-bold rounded-xl px-2.5 py-1 focus:outline-none focus:border-purple-400 shadow-md">
                        <option value="0">🎵 Real J - “ ศีลแตก ”</option>
                        <option value="1">🎵 Donell Jones - Natural Thang</option>
                    </select>
                    <span class="text-[9px] bg-purple-950/80 text-purple-300 px-2 py-0.5 rounded-full border border-purple-500/30 font-mono">🔊 Vol: 15%</span>
                </div>
                <p id="music-status" class="text-[10px] text-emerald-400 font-mono">💿 CD Spinning & Playing...</p>
            </div>
        </div>

        <!-- Stylish Neon Controls (Right Side) -->
        <div class="flex items-center gap-3">
            <button id="music-play-btn" onclick="toggleMusic()" class="bg-gradient-to-r from-purple-600 via-fuchsia-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 text-white px-4 py-2 rounded-2xl text-xs font-extrabold border border-purple-300/30 transition-all active:scale-95 shadow-neon-purple flex items-center gap-2">
                <i id="music-icon" class="fa-solid fa-pause text-xs"></i>
                <span id="music-btn-text" class="tracking-wide">พักเพลง</span>
            </button>
            <a id="yt-link" href="https://www.youtube.com/watch?v=pP-0CzmxLE4" target="_blank" class="glass-card hover:bg-red-950/40 text-red-400 hover:text-red-300 px-3.5 py-2 rounded-2xl text-xs font-bold border border-red-500/30 transition flex items-center gap-2 shadow-lg">
                <i class="fa-brands fa-youtube text-red-500 text-sm"></i>
                <span class="hidden sm:inline">YouTube</span>
            </a>
        </div>
    </div>

    <!-- Hidden YouTube API Player -->
    <div id="player-container" class="hidden"></div>
    <script src="https://www.youtube.com/iframe_api"></script>

    <div id="terminal-drawer" class="fixed bottom-16 left-0 right-0 z-40 transform translate-y-full transition-transform duration-300 ease-in-out">
        <div class="terminal-bg border-t-2 border-yellow-500/50 shadow-2xl rounded-t-2xl p-4 text-xs font-mono text-emerald-400 max-w-7xl mx-auto border-x border-white/10">
            <div class="flex justify-between items-center pb-2 mb-2 border-b border-gray-800">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-red-500 inline-block cursor-pointer" onclick="toggleTerminal()"></span>
                    <span class="w-3 h-3 rounded-full bg-yellow-500 inline-block"></span>
                    <span class="w-3 h-3 rounded-full bg-green-500 inline-block"></span>
                    <span class="ml-2 font-bold text-gray-300">🐍 Python FastAPI Live Console & SQLite Logs</span>
                </div>
                <div class="flex items-center gap-3">
                    <button onclick="clearTerminalLogs()" class="text-gray-400 hover:text-white text-[11px] underline">Clear Logs</button>
                    <button onclick="toggleTerminal()" class="text-gray-400 hover:text-white font-bold">✕</button>
                </div>
            </div>
            <div id="terminal-logs" class="h-44 overflow-y-auto space-y-1 pr-2 text-[11px] leading-relaxed text-gray-300">
                <div class="text-gray-500">[SYSTEM INIT] FastAPI Application initialized with SQLite Database.</div>
            </div>
        </div>
    </div>

    <div id="auth-modal" class="fixed inset-0 bg-black/70 backdrop-blur-md hidden flex justify-center items-center z-50 transition-opacity duration-300 opacity-0">
        <div class="glass-card border border-white/20 p-8 rounded-3xl w-full max-w-sm shadow-2xl relative transform scale-95 transition-transform duration-300 text-white">
            <button onclick="closeAuthModal()" class="absolute top-4 right-4 text-gray-400 hover:text-white font-bold text-xl transition">✕</button>

            <div id="login-form-container">
                <h3 class="text-2xl font-black mb-1 text-purple-400 text-center">เข้าสู่ระบบ</h3>
                <p class="text-xs text-gray-400 text-center mb-5">ผ่าน Python Authentication Endpoint</p>
                
                <form onsubmit="handleLogin(event)" class="flex flex-col gap-3">
                    <input type="text" id="login-username" placeholder="ชื่อผู้ใช้ (Username)" required class="bg-gray-900/80 border border-white/10 p-3 rounded-xl focus:outline-none focus:border-purple-500 text-white text-xs">
                    <input type="password" id="login-password" placeholder="รหัสผ่าน (Password)" required class="bg-gray-900/80 border border-white/10 p-3 rounded-xl focus:outline-none focus:border-purple-500 text-white text-xs">
                    <button type="submit" class="bg-purple-600 hover:bg-purple-500 border border-purple-400/40 text-white font-bold py-3 rounded-xl transition active:scale-95 shadow-neon-purple mt-1 text-xs">
                        🐍 POST /api/login
                    </button>
                </form>
                
                <div class="p-3 bg-purple-950/40 border border-purple-500/20 rounded-xl mt-4 text-[11px] text-gray-300">
                    💡 <span class="font-bold text-purple-400">Admin Account:</span> User: <code class="text-yellow-300 font-bold">admin</code> | Pass: <code class="text-yellow-300 font-bold">1234</code>
                </div>
                <p class="text-xs text-center text-gray-400 mt-4">
                    ยังไม่มีบัญชี? <a href="#" onclick="switchAuthTab('register')" class="text-purple-400 font-bold hover:underline">สมัครสมาชิก</a>
                </p>
            </div>

            <div id="register-form-container" class="hidden">
                <h3 class="text-2xl font-black mb-1 text-purple-400 text-center">สมัครสมาชิก</h3>
                <p class="text-xs text-gray-400 text-center mb-5">สร้างบัญชีผู้ใช้ใหม่ใน SQLite</p>
                
                <form onsubmit="handleRegister(event)" class="flex flex-col gap-3">
                    <input type="text" id="reg-username" placeholder="ชื่อผู้ใช้ (Username)" required class="bg-gray-900/80 border border-white/10 p-3 rounded-xl focus:outline-none focus:border-purple-500 text-white text-xs">
                    <input type="password" id="reg-password" placeholder="รหัสผ่าน (Password)" required class="bg-gray-900/80 border border-white/10 p-3 rounded-xl focus:outline-none focus:border-purple-500 text-white text-xs">
                    <input type="password" id="reg-confirm-password" placeholder="ยืนยันรหัสผ่าน" required class="bg-gray-900/80 border border-white/10 p-3 rounded-xl focus:outline-none focus:border-purple-500 text-white text-xs">
                    <button type="submit" class="bg-purple-600 hover:bg-purple-500 border border-purple-400/40 text-white font-bold py-3 rounded-xl transition active:scale-95 shadow-neon-purple mt-1 text-xs">
                        🐍 POST /api/register
                    </button>
                </form>
                <p class="text-xs text-center text-gray-400 mt-4">
                    มีบัญชีอยู่แล้ว? <a href="#" onclick="switchAuthTab('login')" class="text-purple-400 font-bold hover:underline">เข้าสู่ระบบ</a>
                </p>
            </div>
        </div>
    </div>

    <div id="cart-modal" class="fixed inset-0 bg-black/70 backdrop-blur-md hidden flex justify-center items-center z-50 transition-opacity duration-300 opacity-0">
        <div class="glass-card border border-white/20 p-6 rounded-3xl w-full max-w-md shadow-2xl relative transform scale-95 transition-transform duration-300 text-white">
            <div class="flex justify-between items-center mb-4 border-b border-white/10 pb-4">
                <div>
                    <h3 class="text-lg font-bold text-gray-100 flex items-center gap-2">🛒 ตะกร้าสินค้าของคุณ</h3>
                    <p id="cart-owner-label" class="text-xs text-purple-300 mt-0.5 font-mono"></p>
                </div>
                <button onclick="toggleCartModal()" class="text-gray-400 hover:text-white font-bold text-xl transition">✕</button>
            </div>
            
            <div id="cart-items" class="max-h-60 overflow-y-auto divide-y divide-white/10 pr-1"></div>

            <div class="mt-4 border-t border-white/10 pt-4">
                <div class="flex justify-between font-black text-lg mb-2">
                    <span class="text-gray-300">ราคารวมทั้งหมด:</span>
                    <span id="total-price" class="text-transparent bg-clip-text bg-gradient-to-r from-orange-400 to-amber-300">0 เครดิต</span>
                </div>

                <div id="cart-credit-info" class="text-xs text-right text-gray-400 mb-4"></div>

                <button onclick="checkout()" class="w-full bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 border border-purple-400/30 text-white py-3.5 rounded-2xl font-bold shadow-neon-purple transition active:scale-95 text-xs flex items-center justify-center gap-2">
                    <span>🐍</span> POST /api/checkout (ชำระด้วยเครดิต)
                </button>
            </div>
        </div>
    </div>

    <div id="python-code-modal" class="fixed inset-0 bg-black/80 backdrop-blur-md hidden flex justify-center items-center z-50 p-4">
        <div class="glass-card border border-blue-500/30 p-6 rounded-3xl w-full max-w-3xl max-h-[85vh] flex flex-col shadow-2xl relative text-white">
            <div class="flex justify-between items-center mb-4 pb-2 border-b border-gray-800">
                <h3 class="text-base font-bold text-blue-300 flex items-center gap-2">
                    <span>📄</span> โค้ดต้นแบบ Python FastAPI Server (main.py)
                </h3>
                <button onclick="closePythonCodeModal()" class="text-gray-400 hover:text-white font-bold text-xl">✕</button>
            </div>
            <pre class="terminal-bg p-4 rounded-xl text-xs text-emerald-400 overflow-auto flex-grow font-mono leading-relaxed border border-gray-800 select-all">
<span class="text-purple-400">from</span> fastapi <span class="text-purple-400">import</span> FastAPI, HTTPException
<span class="text-purple-400">from</span> pydantic <span class="text-purple-400">import</span> BaseModel
<span class="text-purple-400">from</span> datetime <span class="text-purple-400">import</span> datetime
<span class="text-purple-400">import</span> sqlite3

app = FastAPI(title=<span class="text-yellow-300">"Galaxy Gear API"</span>)

<span class="text-purple-400">class</span> <span class="text-yellow-300">CheckoutRequest</span>(BaseModel):
    username: <span class="text-cyan-300">str</span>
    items: <span class="text-cyan-300">list</span>
    total_price: <span class="text-cyan-300">float</span>

<span class="text-purple-400">@app.post</span>(<span class="text-yellow-300">"/api/checkout"</span>)
<span class="text-purple-400">def</span> <span class="text-blue-400">process_checkout</span>(data: CheckoutRequest):
    now = datetime.now()
    conn = sqlite3.connect(<span class="text-yellow-300">"galaxy_shop.db"</span>)
    cursor = conn.cursor()
    cursor.execute(<span class="text-yellow-300">"SELECT credit FROM users WHERE username = ?"</span>, (data.username,))
    user = cursor.fetchone()
    <span class="text-purple-400">if not</span> user <span class="text-purple-400">or</span> user[<span class="text-cyan-300">0</span>] < data.total_price:
        conn.close()
        <span class="text-purple-400">raise</span> HTTPException(status_code=<span class="text-cyan-300">400</span>, detail=<span class="text-yellow-300">"เครดิตไม่เพียงพอ"</span>)
    new_credit = user[<span class="text-cyan-300">0</span>] - data.total_price
    cursor.execute(<span class="text-yellow-300">"UPDATE users SET credit = ? WHERE username = ?"</span>, (new_credit, data.username))
    conn.commit()
    conn.close()
    <span class="text-purple-400">return</span> {<span class="text-yellow-300">"status"</span>: <span class="text-yellow-300">"success"</span>, <span class="text-yellow-300">"remaining_credit"</span>: new_credit}</pre>
            <div class="mt-4 flex justify-end">
                <button onclick="closePythonCodeModal()" class="bg-gray-800 hover:bg-gray-700 text-white px-4 py-2 rounded-xl text-xs font-bold">ปิดหน้าต่าง</button>
            </div>
        </div>
    </div>

    <div id="toast-container" class="fixed bottom-5 right-5 z-50 flex flex-col gap-2"></div>

    <script>
        const playlist = [
            { id: "pP-0CzmxLE4", title: "Real J - “ ศีลแตก ”", img: "https://img.youtube.com/vi/pP-0CzmxLE4/hqdefault.jpg", url: "https://www.youtube.com/watch?v=pP-0CzmxLE4" },
            { id: "xX_cNxhafmw", title: "Donell Jones - Natural Thang", img: "https://img.youtube.com/vi/xX_cNxhafmw/hqdefault.jpg", url: "https://www.youtube.com/watch?v=xX_cNxhafmw" }
        ];

        let currentTrackIndex = 0;
        let ytPlayer;
        let isMusicPlaying = false;

        function onYouTubeIframeAPIReady() {
            ytPlayer = new YT.Player('player-container', {
                height: '1',
                width: '1',
                videoId: playlist[currentTrackIndex].id,
                playerVars: {
                    'autoplay': 1,
                    'controls': 0,
                    'loop': 1,
                    'playlist': playlist[currentTrackIndex].id,
                    'origin': window.location.origin
                },
                events: {
                    'onReady': onPlayerReady,
                    'onStateChange': onPlayerStateChange
                }
            });
        }

        function onPlayerReady(event) {
            event.target.setVolume(15);
            event.target.playVideo();
            updateMusicUI(true);
        }

        function onPlayerStateChange(event) {
            if (event.data === YT.PlayerState.PLAYING) {
                updateMusicUI(true);
            } else if (event.data === YT.PlayerState.PAUSED) {
                updateMusicUI(false);
            }
        }

        function changeTrack(index) {
            currentTrackIndex = parseInt(index);
            const track = playlist[currentTrackIndex];

            document.getElementById('cd-cover-img').src = track.img;
            document.getElementById('yt-link').href = track.url;

            if (ytPlayer && typeof ytPlayer.loadVideoById === 'function') {
                ytPlayer.loadVideoById(track.id);
                ytPlayer.setVolume(15);
                ytPlayer.playVideo();
                updateMusicUI(true);
            }
        }

        function toggleMusic() {
            if (!ytPlayer || typeof ytPlayer.playVideo !== 'function') return;
            
            if (isMusicPlaying) {
                ytPlayer.pauseVideo();
                updateMusicUI(false);
            } else {
                ytPlayer.playVideo();
                updateMusicUI(true);
            }
        }

        function updateMusicUI(playing) {
            isMusicPlaying = playing;
            const cd = document.getElementById('cd-disc');
            const icon = document.getElementById('music-icon');
            const hoverIcon = document.getElementById('cd-hover-icon');
            const btnText = document.getElementById('music-btn-text');
            const status = document.getElementById('music-status');

            if (playing) {
                cd.classList.remove('paused-spin');
                icon.className = 'fa-solid fa-pause text-xs';
                hoverIcon.className = 'fa-solid fa-pause text-white text-xs';
                btnText.innerText = 'พักเพลง';
                status.innerText = '💿 CD Spinning & Playing...';
                status.className = 'text-[10px] text-emerald-400 font-mono mt-0.5';
            } else {
                cd.classList.add('paused-spin');
                icon.className = 'fa-solid fa-play text-xs';
                hoverIcon.className = 'fa-solid fa-play text-white text-xs';
                btnText.innerText = 'เล่นเพลง';
                status.innerText = '⏸️ CD Paused';
                status.className = 'text-[10px] text-yellow-400 font-mono mt-0.5';
            }
        }

        const products = [
            { id: 1, name: "คีย์บอร์ดกลไก RGB Custom", category: "คีย์บอร์ด", price: 1590, icon: "fa-keyboard", color: "from-purple-600 to-indigo-600" },
            { id: 2, name: "เมาส์ไร้สาย Gaming 26k DPI", category: "เมาส์", price: 890, icon: "fa-computer-mouse", color: "from-pink-600 to-rose-600" },
            { id: 3, name: "หูฟัง Bluetooth Spatial", category: "หูฟัง", price: 1290, icon: "fa-headset", color: "from-cyan-600 to-blue-600" },
            { id: 4, name: "แผ่นรองเมาส์ RGB XXL", category: "แผ่นรองเมาส์", price: 290, icon: "fa-rug", color: "from-amber-600 to-orange-600" }
        ];

        const featuredCategoriesData = [
            { id: 'คีย์บอร์ด', title: 'คีย์บอร์ดกลไก RGB', subtitle: 'สัมผัสการกดที่แม่นยำ', icon: 'fa-keyboard', color: 'from-purple-500 to-indigo-500' },
            { id: 'เมาส์', title: 'เมาส์ไร้สาย Gaming', subtitle: 'ตอบสนองไว ไร้สายรบกวน', icon: 'fa-computer-mouse', color: 'from-pink-500 to-rose-500' },
            { id: 'หูฟัง', title: 'หูฟัง Bluetooth', subtitle: 'มิติเสียงสมจริงรอบทิศทาง', icon: 'fa-headset', color: 'from-cyan-500 to-blue-500' },
            { id: 'แผ่นรองเมาส์', title: 'แผ่นรองเมาส์ขนาดใหญ่', subtitle: 'พื้นผิวลื่นไหล ควบคุมแม่นยำ', icon: 'fa-rug', color: 'from-amber-500 to-orange-500' }
        ];

        let currentCategory = 'all';
        let users = JSON.parse(localStorage.getItem('users')) || [];
        
        if (!users.find(u => u.username === 'admin')) {
            users.push({ username: 'admin', password: '1234', role: 'admin', credit: 5000 });
            localStorage.setItem('users', JSON.stringify(users));
        }

        let currentUser = JSON.parse(localStorage.getItem('currentUser')) || null;

        function pyLog(endpoint, method, message, status = 200) {
            const now = new Date();
            const timeStr = now.toISOString().replace('T', ' ').substring(0, 19);
            const logContainer = document.getElementById('terminal-logs');
            if(!logContainer) return;
            
            const logItem = document.createElement('div');
            const statusColor = status === 200 ? 'text-emerald-400' : 'text-red-400';
            logItem.innerHTML = `
                <span class="text-gray-500">[${timeStr}]</span> 
                <span class="text-yellow-400 font-bold">${method}</span> 
                <span class="text-cyan-300">${endpoint}</span> - 
                <span class="${statusColor}">${status} OK</span> : 
                <span class="text-gray-300">${message}</span>
            `;
            logContainer.appendChild(logItem);
            logContainer.scrollTop = logContainer.scrollHeight;
        }

        function toggleTerminal() {
            document.getElementById('terminal-drawer').classList.toggle('translate-y-full');
        }

        function clearTerminalLogs() {
            document.getElementById('terminal-logs').innerHTML = `<div class="text-gray-500">[SYSTEM] Logs cleared.</div>`;
        }

        function openPythonCodeModal() { document.getElementById('python-code-modal').classList.remove('hidden'); }
        function closePythonCodeModal() { document.getElementById('python-code-modal').classList.add('hidden'); }

        function getCartStorageKey() {
            return currentUser ? `cart_${currentUser.username}` : 'cart_guest';
        }

        function getUserCart() {
            return JSON.parse(localStorage.getItem(getCartStorageKey())) || [];
        }

        function saveUserCart(cartData) {
            localStorage.setItem(getCartStorageKey(), JSON.stringify(cartData));
        }

        function renderFeaturedCategories() {
            const container = document.getElementById('featured-categories');
            container.innerHTML = featuredCategoriesData.map(cat => `
                <div class="glass-card glass-card-hover rounded-3xl p-4 flex flex-col justify-between relative overflow-hidden group">
                    <div class="relative w-full h-28 rounded-2xl overflow-hidden mb-2 flex items-center justify-center p-2 bg-gradient-to-br ${cat.color} opacity-80 group-hover:opacity-100 transition">
                        <i class="fa-solid ${cat.icon} text-5xl text-white drop-shadow-lg transform group-hover:scale-110 transition duration-300"></i>
                    </div>
                    <div class="flex flex-col gap-2">
                        <div>
                            <h3 class="font-bold text-gray-100 text-xs leading-tight group-hover:text-purple-300 transition">${cat.title}</h3>
                            <p class="text-[10px] text-gray-400 mt-0.5 line-clamp-1">${cat.subtitle}</p>
                        </div>
                        <button onclick="filterCategory('${cat.id}')" 
                            class="w-full mt-1 bg-gradient-to-r from-orange-500 to-amber-500 hover:from-orange-400 hover:to-amber-400 border border-orange-400/30 text-white text-[11px] font-bold py-2 rounded-xl transition active:scale-95 shadow-neon-orange">
                            ดูสินค้า
                        </button>
                    </div>
                </div>
            `).join('');
        }

        function renderCategoryButtons() {
            const categories = ['all', ...new Set(products.map(p => p.category))];
            const container = document.getElementById('category-buttons');
            
            container.innerHTML = categories.map(cat => {
                const isActive = currentCategory === cat;
                const label = cat === 'all' ? 'ทั้งหมด' : cat;
                return `
                    <button onclick="filterCategory('${cat}')" 
                        class="px-3.5 py-1.5 rounded-xl text-xs font-bold transition active:scale-95 border backdrop-blur-md ${
                            isActive 
                            ? 'bg-purple-600/80 text-white border-purple-400/80 shadow-neon-purple' 
                            : 'glass-card text-gray-300 hover:bg-gray-800/40 border-white/10'
                        }">
                        ${label}
                    </button>
                `;
            }).join('');
        }

        function filterCategory(category) {
            currentCategory = category;
            renderCategoryButtons();
            renderProducts();
            pyLog(`/api/products?category=${category}`, 'GET', `Fetched ${category} products`);
        }

        function renderProducts() {
            const grid = document.getElementById('product-grid');
            const filtered = currentCategory === 'all' ? products : products.filter(p => p.category === currentCategory);

            if (filtered.length === 0) {
                grid.innerHTML = `<div class="col-span-full text-center py-12 text-gray-400 text-xs">ไม่พบสินค้าในหมวดหมู่นี้</div>`;
                return;
            }

            grid.innerHTML = filtered.map(p => `
                <div class="glass-card glass-card-hover rounded-3xl p-4 flex flex-col justify-between border border-white/10 relative group">
                    <div class="w-full h-44 rounded-2xl overflow-hidden mb-3 bg-gradient-to-br ${p.color || 'from-slate-800 to-purple-950'} flex items-center justify-center p-2 border border-white/10">
                        <i class="fa-solid ${p.icon || 'fa-box'} text-6xl text-white/90 drop-shadow-[0_10px_10px_rgba(0,0,0,0.5)] transform group-hover:scale-110 transition duration-300"></i>
                    </div>
                    <div>
                        <span class="text-[10px] font-mono bg-purple-950/80 text-purple-300 px-2.5 py-0.5 rounded-full border border-purple-500/30">${p.category}</span>
                        <h3 class="font-bold text-white text-sm mt-2 line-clamp-1">${p.name}</h3>
                        <div class="flex justify-between items-center mt-3 pt-3 border-t border-white/10">
                            <span class="text-sm font-black text-emerald-400">${p.price.toLocaleString()} ฿</span>
                            <button onclick="addToCart(${p.id})" class="bg-purple-600/80 hover:bg-purple-500 border border-purple-400/30 text-white px-3 py-1.5 rounded-xl text-xs font-bold transition active:scale-95 shadow-neon-purple flex items-center gap-1">
                                + เพิ่มลงตะกร้า
                            </button>
                        </div>
                    </div>
                </div>
            `).join('');
        }

        function updateCartCount() {
            const cart = getUserCart();
            const totalCount = cart.reduce((sum, item) => sum + item.quantity, 0);
            document.getElementById('cart-count').innerText = totalCount;
        }

        function addToCart(productId) {
            const product = products.find(p => p.id === productId);
            if (!product) return;

            let cart = getUserCart();
            const existing = cart.find(item => item.id === productId);

            if (existing) {
                existing.quantity += 1;
            } else {
                cart.push({ ...product, quantity: 1 });
            }

            saveUserCart(cart);
            updateCartCount();
            showToast(`เพิ่ม "${product.name}" ลงตะกร้าแล้ว!`, 'success');
            pyLog('/api/cart/add', 'POST', `User '${currentUser ? currentUser.username : 'guest'}' added product ID ${productId}`);
        }

        function toggleCartModal() {
            const modal = document.getElementById('cart-modal');
            const isHidden = modal.classList.contains('hidden');

            if (isHidden) {
                renderCartItems();
                modal.classList.remove('hidden');
                setTimeout(() => {
                    modal.classList.remove('opacity-0');
                    modal.children[0].classList.remove('scale-95');
                }, 10);
            } else {
                modal.classList.add('opacity-0');
                modal.children[0].classList.add('scale-95');
                setTimeout(() => modal.classList.add('hidden'), 300);
            }
        }

        function renderCartItems() {
            const cart = getUserCart();
            const container = document.getElementById('cart-items');
            const ownerLabel = document.getElementById('cart-owner-label');

            ownerLabel.innerText = currentUser ? `OWNER: ${currentUser.username}` : 'OWNER: GUEST';

            if (cart.length === 0) {
                container.innerHTML = `<p class="text-center text-gray-400 py-8 text-xs">ไม่มีสินค้าในตะกร้า</p>`;
                document.getElementById('total-price').innerText = '0 เครดิต';
                document.getElementById('cart-credit-info').innerText = '';
                return;
            }

            let total = 0;
            container.innerHTML = cart.map(item => {
                const itemTotal = item.price * item.quantity;
                total += itemTotal;
                return `
                    <div class="py-3 flex justify-between items-center gap-3">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 bg-purple-900/50 rounded-lg flex items-center justify-center border border-white/10">
                                <i class="fa-solid ${item.icon || 'fa-box'} text-purple-300"></i>
                            </div>
                            <div>
                                <h4 class="font-bold text-xs text-white">${item.name}</h4>
                                <p class="text-[11px] text-gray-400">${item.price.toLocaleString()} ฿ x ${item.quantity}</p>
                            </div>
                        </div>
                        <div class="flex items-center gap-2">
                            <span class="font-bold text-xs text-emerald-400">${itemTotal.toLocaleString()} ฿</span>
                            <button onclick="removeFromCart(${item.id})" class="text-red-400 hover:text-red-300 text-xs px-2 py-1">✕</button>
                        </div>
                    </div>
                `;
            }).join('');

            document.getElementById('total-price').innerText = `${total.toLocaleString()} เครดิต`;

            if (currentUser) {
                const userCredit = currentUser.credit || 0;
                const remaining = userCredit - total;
                const colorClass = remaining >= 0 ? 'text-emerald-400' : 'text-red-400';
                document.getElementById('cart-credit-info').innerHTML = `
                    เครดิตปัจจุบัน: <span class="font-bold">${userCredit.toLocaleString()} ฿</span> | 
                    คงเหลือหลังชำระ: <span class="font-bold ${colorClass}">${remaining.toLocaleString()} ฿</span>
                `;
            } else {
                document.getElementById('cart-credit-info').innerText = 'กรุณาเข้าสู่ระบบเพื่อใช้เครดิตชำระเงิน';
            }
        }

        function removeFromCart(productId) {
            let cart = getUserCart().filter(item => item.id !== productId);
            saveUserCart(cart);
            renderCartItems();
            updateCartCount();
            showToast('ลบรายการสินค้าเรียบร้อยแล้ว', 'info');
        }

        function checkout() {
            if (!currentUser) {
                showToast('กรุณาเข้าสู่ระบบก่อนชำระเงิน!', 'error');
                toggleCartModal();
                openAuthModal('login');
                return;
            }

            const cart = getUserCart();
            if (cart.length === 0) return showToast('ตะกร้าสินค้าว่างเปล่า!', 'error');

            const total = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);

            if (currentUser.credit < total) {
                showToast('เครดิตไม่เพียงพอ! กรุณาติดต่อ Admin เพื่อเติมเครดิต', 'error');
                pyLog('/api/checkout', 'POST', `Checkout Rejected: Insufficient Credit`, 400);
                return;
            }

            currentUser.credit -= total;
            const userIndex = users.findIndex(u => u.username === currentUser.username);
            if (userIndex !== -1) {
                users[userIndex].credit = currentUser.credit;
                localStorage.setItem('users', JSON.stringify(users));
            }
            localStorage.setItem('currentUser', JSON.stringify(currentUser));

            saveUserCart([]);
            updateCartCount();
            renderCartItems();
            updateAuthUI();

            showToast(`ชำระเงินสำเร็จ ${total.toLocaleString()} ฿! หักเครดิตเรียบร้อย`, 'success');
            pyLog('/api/checkout', 'POST', `Checkout Success for '${currentUser.username}'. Deducted ${total} credits.`, 200);
            
            setTimeout(() => toggleCartModal(), 1000);
        }

        function openAuthModal(tab = 'login') {
            const modal = document.getElementById('auth-modal');
            switchAuthTab(tab);
            modal.classList.remove('hidden');
            setTimeout(() => {
                modal.classList.remove('opacity-0');
                modal.children[0].classList.remove('scale-95');
            }, 10);
        }

        function closeAuthModal() {
            const modal = document.getElementById('auth-modal');
            modal.classList.add('opacity-0');
            modal.children[0].classList.add('scale-95');
            setTimeout(() => modal.classList.add('hidden'), 300);
        }

        function switchAuthTab(tab) {
            if (tab === 'login') {
                document.getElementById('login-form-container').classList.remove('hidden');
                document.getElementById('register-form-container').classList.add('hidden');
            } else {
                document.getElementById('login-form-container').classList.add('hidden');
                document.getElementById('register-form-container').classList.remove('hidden');
            }
        }

        function handleLogin(e) {
            e.preventDefault();
            const u = document.getElementById('login-username').value.trim();
            const p = document.getElementById('login-password').value.trim();
            const user = users.find(x => x.username === u && x.password === p);

            if (user) {
                currentUser = user;
                localStorage.setItem('currentUser', JSON.stringify(currentUser));
                updateAuthUI();
                closeAuthModal();
                updateCartCount();
                showToast(`ยินดีต้อนรับกลับคุณ ${user.username}!`, 'success');
                pyLog('/api/login', 'POST', `Authentication Successful for user '${u}'`);
            } else {
                showToast('ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง', 'error');
                pyLog('/api/login', 'POST', `Auth Failed for user '${u}'`, 400);
            }
        }

        function handleRegister(e) {
            e.preventDefault();
            const u = document.getElementById('reg-username').value.trim();
            const p = document.getElementById('reg-password').value.trim();
            const cp = document.getElementById('reg-confirm-password').value.trim();

            if (p !== cp) return showToast('รหัสผ่านไม่ตรงกัน', 'error');
            if (users.find(x => x.username === u)) return showToast('มีชื่อผู้ใช้นี้อยู่แล้ว', 'error');

            const newUser = { username: u, password: p, role: 'user', credit: 0 };
            users.push(newUser);
            localStorage.setItem('users', JSON.stringify(users));

            showToast('สมัครสมาชิกสำเร็จ! กรุณาติดต่อ Admin เพื่อเติมเครดิต', 'success');
            pyLog('/api/register', 'POST', `Registered new user '${u}' with 0 credit into SQLite DB`);
            switchAuthTab('login');
        }

        function deleteAccountPrompt() {
            if (!currentUser) return;
            if (confirm(`คุณต้องการลบบัญชี '${currentUser.username}' ออกจากระบบใช่หรือไม่?`)) {
                users = users.filter(u => u.username !== currentUser.username);
                localStorage.setItem('users', JSON.stringify(users));
                localStorage.removeItem(`cart_${currentUser.username}`);
                pyLog('/api/user/delete', 'DELETE', `User '${currentUser.username}' deleted account from SQLite DB`);
                currentUser = null;
                localStorage.removeItem('currentUser');
                updateAuthUI();
                updateCartCount();
                showToast('ลบบัญชีเรียบร้อยแล้ว', 'info');
            }
        }

        function logout() {
            pyLog('/api/logout', 'POST', `User '${currentUser.username}' logged out`);
            currentUser = null;
            localStorage.removeItem('currentUser');
            updateAuthUI();
            updateCartCount();
            showToast('ออกจากระบบเรียบร้อยแล้ว', 'info');
        }

        function updateAuthUI() {
            const loginBtn = document.getElementById('login-btn');
            const userInfo = document.getElementById('user-info');
            const adminSection = document.getElementById('admin-add-product-section');

            if (currentUser) {
                loginBtn.classList.add('hidden');
                userInfo.classList.remove('hidden');
                document.getElementById('user-display-name').innerText = currentUser.username;
                document.getElementById('user-credit-display').innerText = `💳 ${currentUser.credit.toLocaleString()} ฿`;

                if (currentUser.role === 'admin') {
                    adminSection.classList.remove('hidden');
                    populateCreditUsersDropdown();
                } else {
                    adminSection.classList.add('hidden');
                }
            } else {
                loginBtn.classList.remove('hidden');
                userInfo.classList.add('hidden');
                adminSection.classList.add('hidden');
            }
        }

        function populateCreditUsersDropdown() {
            const select = document.getElementById('credit-target-user');
            select.innerHTML = users.map(u => `<option value="${u.username}">${u.username} (ปัจจุบัน ${u.credit.toLocaleString()} ฿)</option>`).join('');
        }

        function handleCreditSubmit(e) {
            e.preventDefault();
            const targetUser = document.getElementById('credit-target-user').value;
            const amount = parseFloat(document.getElementById('credit-amount').value);

            const uObj = users.find(x => x.username === targetUser);
            if (uObj) {
                uObj.credit += amount;
                localStorage.setItem('users', JSON.stringify(users));

                if (currentUser && currentUser.username === targetUser) {
                    currentUser.credit = uObj.credit;
                    localStorage.setItem('currentUser', JSON.stringify(currentUser));
                }

                updateAuthUI();
                showToast(`เติมเครดิตให้ ${targetUser} จำนวน ${amount.toLocaleString()} ฿ สำเร็จ!`, 'success');
                pyLog('/api/admin/add-credit', 'POST', `Admin added ${amount} credits to '${targetUser}'`);
                document.getElementById('credit-amount').value = '';
            }
        }

        function handleFormSubmit(e) {
            e.preventDefault();
            const name = document.getElementById('prod-name').value;
            const price = parseFloat(document.getElementById('prod-price').value);
            const category = document.getElementById('prod-category').value;

            const iconMap = { 'คีย์บอร์ด': 'fa-keyboard', 'เมาส์': 'fa-computer-mouse', 'หูฟัง': 'fa-headset', 'แผ่นรองเมาส์': 'fa-rug' };

            const newProd = { 
                id: Date.now(), 
                name, 
                price, 
                category, 
                icon: iconMap[category] || 'fa-box',
                color: 'from-purple-900 to-indigo-950'
            };
            products.push(newProd);

            renderCategoryButtons();
            renderProducts();
            showToast(`เพิ่มสินค้า "${name}" ลงระบบ SQLite แล้ว!`, 'success');
            pyLog('/api/products', 'POST', `Added new product ID ${newProd.id}: ${name}`);

            document.getElementById('add-product-form').reset();
        }

        function showToast(msg, type = 'info') {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            
            let bgClass = 'bg-slate-900 border-purple-500/40 text-purple-300';
            if (type === 'success') bgClass = 'bg-slate-900 border-emerald-500/40 text-emerald-300';
            if (type === 'error') bgClass = 'bg-slate-900 border-red-500/40 text-red-300';

            toast.className = `glass-card border ${bgClass} px-4 py-3 rounded-2xl shadow-2xl text-xs font-bold animate-toast flex items-center gap-2`;
            toast.innerHTML = `<span>💬</span> <span>${msg}</span>`;

            container.appendChild(toast);
            setTimeout(() => toast.remove(), 3000);
        }

        window.onload = () => {
            renderFeaturedCategories();
            renderCategoryButtons();
            renderProducts();
            updateAuthUI();
            updateCartCount();
            pyLog('/api/init', 'GET', 'Galaxy Gear Frontend Initialized and Connected to FastAPI Server');
            
            // Automatic trigger upon any user gesture on page
            const triggerAutoplay = () => {
                if (ytPlayer && typeof ytPlayer.playVideo === 'function' && !isMusicPlaying) {
                    ytPlayer.setVolume(15);
                    ytPlayer.playVideo();
                    updateMusicUI(true);
                }
            };

            ['click', 'touchstart', 'scroll', 'keydown'].forEach(evt => {
                window.addEventListener(evt, triggerAutoplay, { once: true });
            });
        };
    </script>
</body>
</html>"""
