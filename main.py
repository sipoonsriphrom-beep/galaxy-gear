from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Galaxy Gear Backend is Running!"}

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# สั่งให้ FastAPI ส่งหน้าเว็บ HTML ที่มีพื้นหลัง GIF และระบบร้านค้ากลับไป
@app.get("/", response_class=HTMLResponse)
def get_homepage():
    return """
    <!DOCTYPE html>
    <html lang="th">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>GALAXY GEAR - Premium Gaming Store</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(rgba(10, 10, 26, 0.85), rgba(10, 10, 26, 0.95)),
                            url('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM21lcm16em51dmk5dTIxanllbGo2OGMxODhjZjE1MHVxdm9wOHFkYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Fbox1ygIqnga5dLinz/giphy.gif');
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: #e2e8f0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            .glass-panel {
                background: rgba(15, 23, 42, 0.75);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.1);
            }
            .neon-border {
                box-shadow: 0 0 15px rgba(168, 85, 247, 0.3);
            }
        </style>
    </head>
    <body class="min-h-screen pb-12">
        <!-- Navbar -->
        <nav class="glass-panel sticky top-0 z-50 px-6 py-4 mb-8 flex justify-between items-center border-b border-purple-900/40">
            <div class="flex items-center space-x-3">
                <i class="fa-solid font-bold text-2xl text-purple-400 fa-rocket"></i>
                <span class="text-2xl font-black tracking-wider bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-500">GALAXY GEAR</span>
            </div>
            <div class="flex items-center space-x-6">
                <span class="bg-purple-900/50 text-purple-300 px-4 py-1.5 rounded-full border border-purple-500/30 text-sm font-semibold">
                    <i class="fa-brands fa-python text-yellow-400 mr-2"></i>Python Backend Active
                </span>
                <span class="text-emerald-400 font-bold bg-emerald-950/60 px-4 py-1.5 rounded-lg border border-emerald-500/30">
                    <i class="fa-solid fa-wallet mr-2"></i>฿ 5,000
                </span>
            </div>
        </nav>

        <!-- Main Content -->
        <div class="max-w-6xl mx-auto px-4">
            <div class="text-center my-10">
                <h1 class="text-4xl md:text-5xl font-black text-white mb-3">GALAXY GEAR STORE</h1>
                <p class="text-purple-300">ระบบร้านค้าไอเทมเกม ขับเคลื่อนด้วย Python FastAPI Server บน Render</p>
            </div>

            <!-- Product Grid -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Item 1 -->
                <div class="glass-panel rounded-2xl p-5 hover:border-purple-500/50 transition-all">
                    <div class="h-48 rounded-xl bg-purple-950/40 mb-4 flex items-center justify-center border border-purple-500/20">
                        <i class="fa-solid fa-headset text-6xl text-purple-400"></i>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-1">Cyber Headphones</h3>
                    <p class="text-slate-400 text-sm mb-4">หูฟังระบบเสียง Spatial Audio ไร้สาย</p>
                    <div class="flex justify-between items-center">
                        <span class="text-2xl font-black text-purple-400">฿ 1,290</span>
                        <button onclick="alert('สั่งซื้อสำเร็จ! บันทึกข้อมูลผ่าน Python Server')" class="bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 text-white font-bold py-2 px-4 rounded-xl transition">
                            ซื้อไอเทม
                        </button>
                    </div>
                </div>

                <!-- Item 2 -->
                <div class="glass-panel rounded-2xl p-5 hover:border-purple-500/50 transition-all">
                    <div class="h-48 rounded-xl bg-purple-950/40 mb-4 flex items-center justify-center border border-purple-500/20">
                        <i class="fa-solid fa-keyboard text-6xl text-pink-400"></i>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-1">Mechanical Keyboard</h3>
                    <p class="text-slate-400 text-sm mb-4">คีย์บอร์ดกลไกสวิตช์เงียบ RGB 16.8M สี</p>
                    <div class="flex justify-between items-center">
                        <span class="text-2xl font-black text-pink-400">฿ 2,450</span>
                        <button onclick="alert('สั่งซื้อสำเร็จ! บันทึกข้อมูลผ่าน Python Server')" class="bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 text-white font-bold py-2 px-4 rounded-xl transition">
                            ซื้อไอเทม
                        </button>
                    </div>
                </div>

                <!-- Item 3 -->
                <div class="glass-panel rounded-2xl p-5 hover:border-purple-500/50 transition-all">
                    <div class="h-48 rounded-xl bg-purple-950/40 mb-4 flex items-center justify-center border border-purple-500/20">
                        <i class="fa-solid fa-computer-mouse text-6xl text-cyan-400"></i>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-1">Ultra Wireless Mouse</h3>
                    <p class="text-slate-400 text-sm mb-4">เมาส์ไร้สายน้ำหนักเบาพิเศษ 26,000 DPI</p>
                    <div class="flex justify-between items-center">
                        <span class="text-2xl font-black text-cyan-400">฿ 990</span>
                        <button onclick="alert('สั่งซื้อสำเร็จ! บันทึกข้อมูลผ่าน Python Server')" class="bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-500 hover:to-pink-500 text-white font-bold py-2 px-4 rounded-xl transition">
                            ซื้อไอเทม
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
