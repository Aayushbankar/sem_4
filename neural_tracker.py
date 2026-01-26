#!/usr/bin/env python3
"""
THE NEURAL-OMNIVERSE (V32) - THE ARTISAN BUILD
High-Resolution Braille Graphics Engine & Meticulous Mathematical Simulations.
Author: Antigravity Engineer
"""

import curses
import json
import os
import time
import math
import random
from datetime import date, datetime
from pathlib import Path

# --- DATABASE ---

SUBJECTS = {
    'MCN': {'name': 'Mobile Computing', 'color': 6},
    'CDF': {'name': 'Cyber Security', 'color': 2},
    'FML': {'name': 'Machine Learning', 'color': 3},
    'MAD': {'name': 'Android Dev', 'color': 4},
    'DMW': {'name': 'Data Mining', 'color': 5},
    'ES':  {'name': 'Entrepreneur', 'color': 4}
}

DATA = {
    'MCN': [
        {'n':'Networking Essentials','t':['Network Models','Client-Server','Layered Mech','OSI Model','TCP/IP','Data Traffic','Congestion','Congestion Ctrl']},
        {'n':'Protocol & Addr', 't':['ARP/RARP','Routing Types','Email Protocols','WWW & HTTP','Link Protocols','IPv4 Subnet','IPv6']},
        {'n':'Mobile Comp', 't':['Evolution','Mobile Arch','Wireless Ad-hoc','Middleware','Apps & Services','Security']},
        {'n':'Network Layer', 't':['Mobile IP','Packet Delivery','Registration','DHCP','TCP Variants','TCP over 3G']},
        {'n':'Trends', 't':['WLAN Arch','WPAN/Bluetooth','4G/5G/6G']}
    ],
    'CDF': [
        {'n':'Fundamentals','t':['CIA Triad','AAA','Vulns & Threats','Proxy Types','7 Layers']},
        {'n':'Network Sec','t':['Malware','Sys Vulns','OSI Attacks','OT Attacks','IoT Attacks']},
        {'n':'Cyber Crime','t':['Classification','Org Crimes','Indiv Crimes','Prop Crimes','Dark Web']},
        {'n':'Ethical Hacking','t':['Hacking Phases','Kali Linux','OSINT','EXIF Analysis','Nmap Scanning']},
        {'n':'Forensics','t':['Principles','Evidence Handling','Autopsy/Sleuth','CVE/MITRE','Case Studies']}
    ],
    'FML': [
        {'n':'Intro','t':['Human vs ML','Types of ML','Applications','Tools']},
        {'n':'Data Prep','t':['Pipeline','Data Types','Quality','Feature Selection']},
        {'n':'Modeling','t':['Model Selection','Training types','Confusion Matrix','Improvement']},
        {'n':'Supervised','t':['Classif vs Reg','KNN','SVM','Linear Reg','Log Reg']},
        {'n':'Unsupervised','t':['Clustering','K-Means','Assoc Rules','Apriori']},
        {'n':'Python','t':['Pandas','NumPy','Matplotlib','Scikit-learn']}
    ],
    'MAD': [
        {'n':'Intro','t':['Mobile OS','Android vs iOS','Android Studio','Emulator']},
        {'n':'Arch','t':['Layers','Activity Lifecycle','Service Lifecycle','Broadcast Rx','Manifest']},
        {'n':'UI/Events','t':['Layouts','Constraint','Widgets','Event Handling','Intents','Toasts']},
        {'n':'Storage','t':['SharedPrefs','SQLite','CRUD','Firebase']},
        {'n':'Trends', 't':['Kotlin','Flutter/React','APIs','Publishing']}
    ],
    'DMW': [
        {'n':'Fundamentals','t':['KDD Process','Applications','Data/Info/Know']},
        {'n':'Warehousing','t':['DW Concepts','OLTP vs OLAP','Data Marts']},
        {'n':'Techniques','t':['Classification','Decision Tree','Naive Bayes','K-Means','Apriori']},
        {'n':'Design','t':['Star/Snowflake','Fact/Dim Tables','ETL','OLAP Ops']},
        {'n':'Tools','t':['Orange/RapidMiner','Case Studies','Future Scope']}
    ],
    'ES': [
        {'n':'Intro','t':['Traits','Types','Intrapreneur','Structures','Startup India']},
        {'n':'Ideas','t':['Discovery','Business Plan','Market Research','4Ps']},
        {'n':'Mgmt','t':['Leadership','Resources','Production','HR']},
        {'n':'Support','t':['Institutions','PAN/GST','Incubators','Models']},
        {'n':'Exit','t':['CSR','Ethics','Export-Import','Exit Strategies']}
    ]
}

PRACTICALS = {
    'CDF': ['Dark Web Analysis', 'IDS Demo', 'Email Header Analysis', 'Password Strength', 'Steganography Analysis', 'Malicious Scripting', 'OSINT Framework', 'Cybercrime Report', 'EXIF Metadata', 'NMAP/Kali', 'Autopsy Sleuth', 'Vulnerability Analysis'],
    'DMW': ['KDD Process', 'DM Apps', 'DW Concepts', 'OLTP vs OLAP', 'Decision Tree', 'Naive Bayes', 'K-Means', 'Apriori', 'Combined Study', 'Star Schema', 'Snowflake Schema', 'OLAP Ops', 'DM Tools', 'Case Study', 'Mini Project'],
    'ES': ['Traits Collage', 'Interview', 'Business Model', 'Portfolio Web', 'Trade Fair', 'Startup Story', 'Shark Tank', 'Waste Product', 'Cost Analysis', 'Bank Scheme', 'Industry Visit', 'Social Cause'],
    'FML': ['NumPy/Matplot', 'Pandas IO', 'Scikit Intro', 'Fruit Predict', 'Data Prep', 'Confusion Matrix', 'KNN Logic', 'SVM Genre', 'Logistic Reg', 'Linear Reg', 'K-Means Calc'],
    'MAD': ['Installation', 'Lifecycle', 'Linear/Rel', 'Constraint', 'Calculator', 'Intent Pass', 'Implicit Dial', 'Theme Toggle', 'Content Prov', 'SharedPrefs', 'SQLite Insert', 'SQLite CRUD', 'Firebase Auth', 'Firebase/API'],
    'MCN': ['Client-Server', 'P2P Network', 'Wireshark Setup', 'TCP Analysis', 'IPv4 Check', 'Subnet Calc', 'Class C Study', 'IPv6 Check', 'Wireless Adhoc', 'Mobile IP Pack', 'Agent Registration', 'Bluetooth Stack']
}

DEADLINE = date(2026, 3, 30)

# --- PERSISTENCE ---
APP_DIR = Path.home() / ".local" / "share" / "neural-omniverse-v32"
STATE_FILE = APP_DIR / "omniverse_v32_state.json"

class OmniverseEngine:
    def __init__(self):
        APP_DIR.mkdir(parents=True, exist_ok=True)
        self.state = self.load()
        self.sub_codes = list(SUBJECTS.keys())

    def load(self):
        if STATE_FILE.exists():
            try: return json.load(open(STATE_FILE))
            except: pass
        return {'absorbed': {}, 'logs': []}

    def save(self):
        with open(STATE_FILE, 'w') as f: json.dump(self.state, f)

    def log(self, entry):
        self.state['logs'].append(f"{datetime.now().strftime('%H:%M:%S')} | {entry}")
        if len(self.state['logs']) > 50: self.state['logs'].pop(0)

    def get_integrity(self, filter_code=None):
        total, done = 0, 0
        codes = [filter_code] if filter_code else self.sub_codes
        for code in codes:
            for unit in DATA[code]:
                total += len(unit['t'])
                for t in unit['t']:
                    if self.state['absorbed'].get(f"{code}_{unit['n']}_{t}"): done += 1
            if code in PRACTICALS:
                total += len(PRACTICALS[code])
                for p in PRACTICALS[code]:
                    if self.state['absorbed'].get(f"{code}_LAB_{p}"): done += 1
        return (done / total) if total > 0 else 0

# --- BRAILLE GRAPHICS ENGINE ---

class BrailleCanvas:
    def __init__(self, h, w):
        self.h = h * 4
        self.w = w * 2
        self.grid = [[0 for _ in range(self.w)] for _ in range(self.h)]

    def clear(self):
        self.grid = [[0 for _ in range(self.w)] for _ in range(self.h)]

    def set(self, x, y):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.grid[int(y)][int(x)] = 1

    def render(self):
        output = []
        for y in range(0, self.h, 4):
            line = ""
            for x in range(0, self.w, 2):
                # Dots: 1 4 / 2 5 / 3 6 / 7 8
                dots = [
                    self.grid[y][x],     # 1
                    self.grid[y+1][x],   # 2
                    self.grid[y+2][x],   # 3
                    self.grid[y][x+1],   # 4
                    self.grid[y+1][x+1], # 5
                    self.grid[y+2][x+1], # 6
                    self.grid[y+3][x],   # 7
                    self.grid[y+3][x+1]  # 8
                ]
                val = 0
                for i, d in enumerate(dots):
                    if d: val += (1 << i)
                line += chr(0x2800 + val)
            output.append(line)
        return output

# --- THE INTERFACE (Neural-Omniverse V32) ---

class NeuralOmniverse:
    def __init__(self, engine):
        self.engine = engine
        self.sub_idx = 0
        self.topic_idx = 0
        self.scroll_top = 0
        self.msg = "OMNIVERSE_OS_V32_ONLINE"
        self.searching = False
        self.search_query = ""
        self.timer_seconds = 1500
        self.timer_active = False
        self.last_tick = time.time()
        self.glitch_timer = 0
        self.vis_mode = 0 # 0-9 High-Res Masterpieces
        
        # Sim States
        self.sim_t = 0.0
        self.stars = []
        self.fluid_density = []
        self.meteors = []
        self.mesh_nodes = []
        self.shockwaves = []
        self.canvas = None

    def _init_colors(self):
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_WHITE, -1)
        curses.init_pair(2, curses.COLOR_RED, -1)
        curses.init_pair(3, curses.COLOR_GREEN, -1)
        curses.init_pair(4, curses.COLOR_CYAN, -1)
        curses.init_pair(5, curses.COLOR_YELLOW, -1)
        curses.init_pair(6, 13, -1)  # High Fidelity Pink
        curses.init_pair(7, 45, -1)  # High Fidelity Aqua

    def safe_addstr(self, win, y, x, s, attr=0):
        h, w = win.getmaxyx()
        if 0 <= y < h and 0 <= x < w:
            try: win.addstr(int(y), int(x), s[:w-x-1], attr)
            except: pass

    def draw_chassis(self, win, h, w):
        p1_w = int(w * 0.3)
        p2_w = int(w * 0.45)
        p3_w = w - p1_w - p2_w - 2
        div1_x = p1_w
        div2_x = div1_x + p2_w
        
        # High-Fidelity Chassis
        self.safe_addstr(win, 0, 0, "▟" + "━"*(w-2) + "▙", curses.color_pair(4)|curses.A_DIM)
        for i in range(1, h-1):
            self.safe_addstr(win, i, 0, "┃", curses.color_pair(4)|curses.A_DIM)
            self.safe_addstr(win, i, w-1, "┃", curses.color_pair(4)|curses.A_DIM)
            self.safe_addstr(win, i, div1_x, "│", curses.color_pair(4)|curses.A_DIM)
            self.safe_addstr(win, i, div2_x, "│", curses.color_pair(4)|curses.A_DIM)
        
        split_y = int(h * 0.5)
        for x in range(div2_x + 1, w - 1):
            self.safe_addstr(win, split_y, x, "─", curses.color_pair(4)|curses.A_DIM)
        self.safe_addstr(win, h-1, 0, "▜" + "━"*(w-2) + "▛", curses.color_pair(4)|curses.A_DIM)
        return p1_w, p2_w, p3_w, div1_x, div2_x, split_y

    def draw_turbine(self, win, h, w_p):
        """Panel 1: Subject Turbine."""
        center_y = 3
        self.safe_addstr(win, 1, 2, "◈ SECTOR_SYNC", curses.color_pair(4)|curses.A_BOLD)
        for i in range(-2, 3):
            idx = (self.sub_idx + i) % len(self.engine.sub_codes)
            code = self.engine.sub_codes[idx]
            integrity = self.engine.get_integrity(code)
            y = center_y + i
            attr = curses.color_pair(7)
            if i == 0: attr |= curses.A_BOLD | curses.A_REVERSE
            else: attr |= curses.A_DIM
            off = abs(i)
            self.safe_addstr(win, y, 4 + off, f"{code} » {int(integrity*100)}% ", attr)

        self.safe_addstr(win, 6, 1, "┈"*(w_p-1), curses.color_pair(4)|curses.A_DIM)

        code = self.engine.sub_codes[self.sub_idx]
        items = []
        for u in DATA[code]:
            items.append({'type':'u','n':u['n']})
            for t in u['t']: items.append({'type':'t','n':t,'id':f"{code}_{u['n']}_{t}"})
        if code in PRACTICALS:
            items.append({'type':'u','n':'LABS'})
            for p in PRACTICALS[code]: items.append({'type':'t','n':p,'id':f"{code}_LAB_{p}"})
        
        if self.searching: items = [t for t in items if self.search_query.lower() in t['n'].lower()]
        view_h = h - 10
        if self.topic_idx >= len(items): self.topic_idx = max(0, len(items)-1)
        if self.topic_idx < self.scroll_top: self.scroll_top = self.topic_idx
        if self.topic_idx >= self.scroll_top + view_h: self.scroll_top = self.topic_idx - view_h + 1

        for i in range(view_h):
            idx = i + self.scroll_top
            if idx >= len(items): break
            t = items[idx]; y = 7 + i; is_f = (idx == self.topic_idx)
            if t['type'] == 'u':
                self.safe_addstr(win, y, 2, f"╡ {t['n'].upper()}", curses.color_pair(4)|curses.A_BOLD)
            else:
                is_d = self.engine.state['absorbed'].get(t['id']); attr = curses.color_pair(3) if is_d else curses.color_pair(1)
                if is_f: attr |= curses.A_REVERSE | curses.A_BOLD
                self.safe_addstr(win, y, 4, f"{'✺' if is_d else '✧'} {t['n']}", attr)

    def draw_artisan_vis(self, win, h, w_p, start_x):
        """Panel 2: 10 High-Res Braille Masterpieces."""
        modes = ["EVENT_HORIZON", "HYPER_DRIVE", "STAR_SHOWER", "SYNAPTIC_NET", "PLASMA_TIDE", "CYBER_AURORA", "SOLAR_FLARE", "QUANTUM_SYNC", "HYPER_CUBE", "ZEN_FLOW"]
        title = f"◈ {modes[self.vis_mode]}"
        self.safe_addstr(win, 1, start_x + (w_p - len(title))//2, title, curses.color_pair(4)|curses.A_BOLD)
        
        # Init or refresh Canvas
        if not self.canvas or self.canvas.w != (w_p-2)*2:
            self.canvas = BrailleCanvas(h-4, w_p-2)
        
        self.canvas.clear()
        cx, cy = self.canvas.w // 2, self.canvas.h // 2
        integrity = self.engine.get_integrity()
        self.sim_t += 0.05
        
        # 0: EVENT-HORIZON (High-Res Black Hole)
        if self.vis_mode == 0:
            for i in range(400):
                angle = i * 0.1 + self.sim_t
                rad = 30 + math.sin(angle*2)*5
                px = cx + int(rad * 2 * math.cos(angle))
                py = cy + int(rad * 0.3 * math.sin(angle)) # Disk tilt
                self.canvas.set(px, py)
                # Event horizon lensing
                if i % 10 == 0:
                    self.canvas.set(cx + int(math.cos(angle*2)*15), cy + int(math.sin(angle*2)*15))

        # 1: HYPER-DRIVE (Warp - FAV)
        elif self.vis_mode == 1:
            if not self.stars:
                for _ in range(120): self.stars.append([random.uniform(-1,1), random.uniform(-1,1), random.uniform(0.1, 2.0)])
            speed = 0.08 + integrity*0.1
            for s in self.stars:
                s[2] -= speed
                if s[2]<=0: s[0]=random.uniform(-1,1); s[1]=random.uniform(-1,1); s[2]=2.0
                px = cx + int((s[0]/s[2]) * self.canvas.w * 0.5)
                py = cy + int((s[1]/s[2]) * self.canvas.h * 0.5)
                # Draw high-res trail
                for l in range(3):
                    self.canvas.set(px - int(s[0]*l*2), py - int(s[1]*l*2))

        # 2: STAR-SHOWER (Meteors - FAV)
        elif self.vis_mode == 2:
            if random.random() < 0.2:
                self.meteors.append([random.randint(0, self.canvas.w), 0, random.uniform(1.5, 3.0), random.uniform(1.0, 2.5)])
            for m in self.meteors[:]:
                for k in range(10):
                    tx, ty = int(m[0]-k*m[3]), int(m[1]-k*m[2])
                    self.canvas.set(tx, ty)
                m[0] += m[3]; m[1] += m[2]
                if m[1] > self.canvas.h: self.meteors.remove(m)

        # 3: SYNAPTIC-NET (3D Mesh)
        elif self.vis_mode == 3:
            if not self.mesh_nodes:
                for _ in range(15): self.mesh_nodes.append({'x':random.uniform(-20,20), 'y':random.uniform(-10,10), 'z':random.uniform(-10,10)})
            for n in self.mesh_nodes:
                t_rot = self.sim_t * 0.5
                rx = n['x']*math.cos(t_rot) - n['z']*math.sin(t_rot)
                rz = n['x']*math.sin(t_rot) + n['z']*math.cos(t_rot)
                px = cx + int(rx * 2); py = cy + int(n['y'] * 2)
                self.canvas.set(px, py)
                for n2 in self.mesh_nodes:
                    if abs(n['x']-n2['x']) < 10 and abs(n['y']-n2['y']) < 10:
                        # Draw high-res line
                        for k in range(10):
                            lx = px + int((n2['x']-n['x'])*k*0.2)
                            ly = py + int((n2['y']-n['y'])*k*0.2)
                            self.canvas.set(lx, ly)

        # 4: PLASMA-TIDE (High-Res Fluid)
        elif self.vis_mode == 4:
            for y in range(0, self.canvas.h, 4):
                for x in range(0, self.canvas.w, 4):
                    # Scalar field logic
                    v = math.sin(x*0.05 + self.sim_t) + math.cos(y*0.1 - self.sim_t*0.5)
                    v += math.sin((x+y)*0.02 + self.sim_t*0.8)
                    if v > 0.8:
                        self.canvas.set(x, y); self.canvas.set(x+1, y+1)

        # 5: CYBER-AURORA (Harmonics)
        elif self.vis_mode == 5:
            for x in range(self.canvas.w):
                y_val = cy + int(math.sin(x*0.04 + self.sim_t)*10 + math.sin(x*0.08 - self.sim_t*0.3)*5)
                for i in range(5):
                    self.canvas.set(x, y_val - i)

        # 6: SOLAR-FLARE (Supernova - FAV)
        elif self.vis_mode == 6:
            if not self.shockwaves:
                for _ in range(80): self.shockwaves.append({'a':random.uniform(0, 6.28), 'd':random.uniform(2, 5), 's':random.uniform(0.5, 1.5)})
            for p in self.shockwaves:
                p['d'] += p['s']
                if p['d'] > 60: p['d'] = 2; p['a'] = random.uniform(0, 6.28)
                px = cx + int(p['d'] * 2 * math.cos(p['a']))
                py = cy + int(p['d'] * math.sin(p['a']))
                self.canvas.set(px, py)

        # 7: QUANTUM-SYNC (Mandala)
        elif self.vis_mode == 7:
            for i in range(6):
                ang_off = i * (math.pi/3) + self.sim_t*0.2
                rad = 20 + math.sin(self.sim_t)*5
                for k in range(12):
                    sub_ang = k * (math.pi/6)
                    px = cx + int(rad * math.cos(ang_off + sub_ang))
                    py = cy + int(rad/2 * math.sin(ang_off + sub_ang))
                    # Connector lines
                    for l in range(10):
                        lx = cx + int(rad * math.cos(ang_off + sub_ang) * (l/10))
                        ly = cy + int(rad/2 * math.sin(ang_off + sub_ang) * (l/10))
                        self.canvas.set(lx, ly)

        # 8: HYPER-CUBE (4D Tesseract)
        elif self.vis_mode == 8:
            t = self.sim_t
            for i in range(16):
                # 4D hypercube vertices
                x = 1 if i & 1 else -1; y = 1 if i & 2 else -1; z = 1 if i & 4 else -1; w = 1 if i & 8 else -1
                # rotate xy, xz, xw... simple 2 plane rotation for effect
                x1 = x*math.cos(t) - y*math.sin(t); y1 = x*math.sin(t) + y*math.cos(t)
                z1 = z*math.cos(t*0.5) - w*math.sin(t*0.5); w1 = z*math.sin(t*0.5) + w*math.cos(t*0.5)
                # Projection
                proj_x = cx + int(x1 * 15); proj_y = cy + int(z1 * 8)
                self.canvas.set(proj_x, proj_y)

        # 9: ZEN-FLOW (Procedural Mountains)
        elif self.vis_mode == 9:
            for x in range(self.canvas.w):
                h_val = int(math.sin(x*0.03 + self.sim_t*0.2)*12 + math.cos(x*0.07)*5)
                top = cy + h_val
                for y in range(top, self.canvas.h):
                    if (x+y) % 2 == 0: self.canvas.set(x, y) # Dithered fill

        # Render Braille to panel
        lines = self.canvas.render()
        for i, line in enumerate(lines):
            col = curses.color_pair(4 if self.vis_mode % 2 == 0 else 6)
            self.safe_addstr(win, 2+i, start_x+1, line, col)

    def draw_dashboard_deck(self, win, h, w_p, start_x, split_y):
        """Panel 3: Hub."""
        # MISSION
        self.safe_addstr(win, 1, start_x + 2, "◈ OMNI_DIRECTIVE", curses.color_pair(4)|curses.A_BOLD)
        m, s = self.timer_seconds // 60, self.timer_seconds % 60
        t_attr = curses.color_pair(5) | (curses.A_BOLD if self.timer_active else curses.A_DIM)
        self.safe_addstr(win, 3, start_x + 2, f"CHRONO  » {m:02}:{s:02}", t_attr)

        # HEALTH
        self.safe_addstr(win, split_y + 1, start_x + 2, "◈ INTEGRITY_MAP", curses.color_pair(4)|curses.A_BOLD)
        for i, code in enumerate(self.engine.sub_codes):
            integrity = self.engine.get_integrity(code)
            y = split_y + 3 + i
            bar_w = w_p - 12
            filled = int(integrity * bar_w)
            self.safe_addstr(win, y, start_x + 2, f"{code}:[", curses.color_pair(1)|curses.A_DIM)
            self.safe_addstr(win, y, start_x + 8, "█"*filled, curses.color_pair(3))
            self.safe_addstr(win, y, start_x + 8 + filled, " "*(bar_w - filled), 0)
            self.safe_addstr(win, y, start_x + 8 + bar_w, f"] {int(integrity*100)}%", curses.color_pair(1)|curses.A_DIM)

    def main_loop(self, stdscr):
        self._init_colors()
        curses.curs_set(0); stdscr.nodelay(True); stdscr.timeout(25)
        while True:
            stdscr.erase()
            h, w = stdscr.getmaxyx()
            if h < 24 or w < 100:
                self.safe_addstr(stdscr, h//2, (w-25)//2, "OMNIVERSE_REQD_100x24", curses.color_pair(2))
                stdscr.refresh(); time.sleep(1); continue

            p1_w, p2_w, p3_w, div1, div2, split_y = self.draw_chassis(stdscr, h, w)
            if self.glitch_timer > 0:
                self.glitch_timer -= 1
                if random.random() > 0.4: stdscr.attron(curses.A_REVERSE)

            self.draw_turbine(stdscr, h, p1_w)
            self.draw_artisan_vis(stdscr, h, p2_w, div1 + 1)
            self.draw_dashboard_deck(stdscr, h, p3_w, div2 + 1, split_y)

            self.safe_addstr(stdscr, h-1, 2, f"LOG: {self.msg} | 0-9:SHIFT SPACE:SYNC F:SEARCH Q:EXIT", curses.A_DIM)
            if self.searching: self.safe_addstr(stdscr, h-2, 2, f"SEARCH: {self.search_query}_", curses.color_pair(5)|curses.A_BOLD)

            if self.timer_active and time.time() - self.last_tick >= 1.0:
                self.timer_seconds -= 1; self.last_tick = time.time()
                if self.timer_seconds <= 0: self.timer_active = False; self.msg = "MISSION_ABSORBED"

            stdscr.refresh(); stdscr.attroff(curses.A_REVERSE)
            try: ch = stdscr.getch()
            except: ch = -1
            if ch == -1: continue

            if self.searching:
                if ch == 27: self.searching = False; self.search_query = ""
                elif ch in (10, 13): self.searching = False
                elif ch == 127: self.search_query = self.search_query[:-1]
                else: self.search_query += chr(ch)
                continue

            if ch == ord('q'): break
            elif ch == ord('l'): self.sub_idx = (self.sub_idx + 1) % len(self.engine.sub_codes); self.topic_idx = 0
            elif ch == ord('h'): self.sub_idx = (self.sub_idx - 1) % len(self.engine.sub_codes); self.topic_idx = 0
            elif ch in [ord(str(i)) for i in range(10)]: 
                self.vis_mode = int(chr(ch)); self.msg = f"SHIFT: MODE_{self.vis_mode}"; self.glitch_timer = 2
                self.stars=[]; self.meteors=[]; self.mesh_nodes=[]; self.shockwaves=[]
            elif ch == ord('j'): self.topic_idx += 1
            elif ch == ord('k'): self.topic_idx = max(0, self.topic_idx - 1)
            elif ch == ord('f'): self.searching = True
            elif ch == ord('t'): self.timer_active = not self.timer_active
            elif ch == ord('r'): self.timer_seconds = 1500; self.msg = "TIMER_RESET"
            elif ch == ord(' '):
                code = self.engine.sub_codes[self.sub_idx]
                items = []
                for u in DATA[code]:
                    items.append({'type':'u','n':u['n']})
                    for t in u['t']: items.append({'type':'t','n':t,'id':f"{code}_{u['n']}_{t}"})
                if code in PRACTICALS:
                    items.append({'type':'u','n':'LABS'})
                    for p in PRACTICALS[code]: items.append({'type':'t','n':p,'id':f"{code}_LAB_{p}"})
                if 0 <= self.topic_idx < len(items):
                    t = items[self.topic_idx]
                    if t['type'] == 't':
                        v = not self.engine.state['absorbed'].get(t['id'])
                        self.engine.state['absorbed'][t['id']] = v; self.engine.save()
                        self.engine.log(f"ABSORB: {t['n'][:15]}"); self.msg = f"SYNCED: {t['n'][:20]}"
                        self.glitch_timer = 4

if __name__ == "__main__":
    try: curses.wrapper(lambda s: NeuralOmniverse(OmniverseEngine()).main_loop(s))
    except (KeyboardInterrupt, SystemExit): pass
