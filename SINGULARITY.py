import webview

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S.I.N.G.U.L.A.R.I.T.Y. · Bleeding EQ · Player</title>
    <script src="https://cdn.jsdelivr.net/npm/jsmediatags@3.9.7/dist/jsmediatags.min.js"></script>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }

        /* Light theme only */
        :root {
            --bg-start: #e0e5ec;
            --bg-end: #c8d0dc;
            --accent: #4a9eff;
            --accent-dark: #2d7acc;
            --text-primary: #1e2a3a;
            --text-secondary: #2c3e66;
            --card-bg: rgba(245,248,250,0.96);
            --button-bg: rgba(0,0,0,0.05);
            --button-hover: rgba(74,158,255,0.15);
            --border-light: rgba(0,0,0,0.08);
            --canvas-bg: radial-gradient(circle at center, rgba(255,255,255,0.2), rgba(200,210,220,0.4));
            --control-bar-bg: rgba(245,248,250,0.8);
            --sidebar-width-collapsed: 50px;
            --sidebar-width-expanded: 280px;
        }

        body {
            background: linear-gradient(135deg, var(--bg-start), var(--bg-end));
            font-family: 'Inter', system-ui, sans-serif;
            height: 100vh; width: 100vw; overflow: hidden;
            margin: 0; padding: 0;
        }

        /* Logo */
        .app-logo {
            position: fixed;
            top: 20px;
            left: calc(var(--sidebar-width-collapsed) + 20px);
            z-index: 200;
            font-size: 18px;
            font-weight: 700;
            letter-spacing: 2px;
            background: linear-gradient(135deg, var(--accent), var(--accent-dark));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0 0 8px rgba(0,0,0,0.1);
            pointer-events: none;
            transition: left 0.25s ease;
            white-space: nowrap;
        }
        body:has(.sidebar.expanded) .app-logo {
            left: calc(var(--sidebar-width-expanded) + 20px);
        }

        /* Sidebar */
        .sidebar {
            position: fixed;
            left: 0;
            top: 0;
            bottom: 0;
            width: var(--sidebar-width-collapsed);
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            z-index: 100;
            transition: width 0.25s ease;
            overflow-x: hidden;
            display: flex;
            flex-direction: column;
            box-shadow: 2px 0 8px rgba(0,0,0,0.1);
            border-right: 1px solid var(--border-light);
            cursor: pointer;
        }
        .sidebar.expanded {
            width: var(--sidebar-width-expanded);
            cursor: default;
        }
        .sidebar:not(.expanded)::before {
            content: "S";
            font-size: 32px;
            font-weight: 700;
            position: absolute;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: linear-gradient(135deg, var(--accent), var(--accent-dark));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            pointer-events: none;
            font-family: 'Inter', system-ui, sans-serif;
        }
        .sidebar-handle {
            display: none;
            width: 100%;
            height: 70px;
            background: var(--button-hover);
            align-items: center;
            justify-content: flex-start;
            padding-left: 20px;
            gap: 12px;
            cursor: pointer;
            font-size: 24px;
            color: var(--accent);
        }
        .sidebar.expanded .sidebar-handle {
            display: flex;
        }
        .sidebar-handle .logo-s {
            font-size: 28px;
            font-weight: 700;
            background: linear-gradient(135deg, var(--accent), var(--accent-dark));
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
        }
        .sidebar-handle .handle-text {
            font-size: 14px;
            font-weight: 500;
            color: var(--text-primary);
        }
        .playlist-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            opacity: 0;
            transition: opacity 0.2s;
            overflow-y: auto;
        }
        .sidebar.expanded .playlist-content {
            opacity: 1;
        }
        .playlist-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-light);
        }
        .playlist-header .header-icon {
            width: 18px;
            height: 18px;
            margin-right: 8px;
            stroke: var(--accent);
            stroke-width: 1.8;
            fill: none;
            vertical-align: middle;
        }
        .playlist-header span {
            color: var(--accent);
            font-weight: 600;
            font-size: 14px;
            display: inline-flex;
            align-items: center;
        }
        .playlist-actions button {
            background: var(--button-bg);
            border: none;
            width: 28px;
            height: 28px;
            border-radius: 28px;
            color: var(--text-secondary);
            cursor: pointer;
            font-size: 16px;
        }
        .playlist-actions button:hover {
            background: var(--accent);
            color: white;
        }
        .playlist-list {
            max-height: 180px;
            overflow-y: auto;
            padding: 8px;
        }
        .playlist-item {
            background: var(--button-bg);
            margin: 6px 0;
            padding: 8px 12px;
            border-radius: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
            transition: 0.1s;
        }
        .playlist-item.active {
            background: var(--accent);
            color: white;
        }
        .playlist-name {
            font-size: 13px;
            font-weight: 500;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            color: var(--text-primary);
        }
        .playlist-item.active .playlist-name {
            color: white;
        }
        .playlist-item-actions {
            display: none;
            gap: 6px;
        }
        .playlist-item:hover .playlist-item-actions {
            display: flex;
        }
        .playlist-item-actions button {
            background: rgba(0,0,0,0.2);
            border: none;
            width: 26px;
            height: 26px;
            border-radius: 26px;
            cursor: pointer;
            color: white;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: 0.1s;
        }
        .playlist-item-actions button:hover {
            background: var(--accent);
            transform: scale(1.02);
        }
        .playlist-item-actions .action-icon {
            width: 14px;
            height: 14px;
            stroke: currentColor;
            stroke-width: 2;
            fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
        }
        .tracks-header {
            padding: 12px 16px 6px;
            font-size: 12px;
            color: var(--accent);
            font-weight: 600;
            border-top: 1px solid var(--border-light);
            display: flex;
            align-items: center;
        }
        .tracks-header .header-icon {
            width: 16px;
            height: 16px;
            margin-right: 8px;
            stroke: var(--accent);
            stroke-width: 1.8;
            fill: none;
        }
        .playlist-tracks {
            flex: 1;
            overflow-y: auto;
            padding: 8px;
        }
        .track-item {
            background: var(--button-bg);
            padding: 8px 12px;
            margin: 6px 0;
            border-radius: 12px;
            font-size: 13px;
            cursor: pointer;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            color: var(--text-secondary);
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: 0.1s;
        }
        .track-item.active {
            background: var(--accent);
            color: white;
        }
        .track-item:hover {
            background: var(--button-hover);
        }
        .track-name {
            flex: 1;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .track-actions {
            display: none;
            gap: 6px;
        }
        .track-item:hover .track-actions {
            display: flex;
        }
        .track-actions button {
            background: rgba(0,0,0,0.2);
            border: none;
            width: 26px;
            height: 26px;
            border-radius: 26px;
            cursor: pointer;
            color: white;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: 0.1s;
        }
        .track-actions button:hover {
            background: var(--accent);
            transform: scale(1.02);
        }
        .track-actions .action-icon {
            width: 14px;
            height: 14px;
            stroke: currentColor;
            stroke-width: 2;
            fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
        }

        /* Main content */
        .main-content {
            margin-left: var(--sidebar-width-collapsed);
            transition: margin-left 0.25s ease;
            height: 100vh;
            display: flex;
            flex-direction: column;
            position: relative;
        }
        body:has(.sidebar.expanded) .main-content {
            margin-left: var(--sidebar-width-expanded);
        }
        .canvas-container {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            min-height: 0;
        }
        canvas {
            width: 100%;
            height: 100%;
            background: var(--canvas-bg);
            border-radius: 16px;
            display: block;
            object-fit: contain;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }

        /* Bottom controls */
        .overlay-controls {
            position: absolute;
            bottom: 20px;
            left: 20px;
            right: 20px;
            background: var(--control-bar-bg);
            backdrop-filter: blur(12px);
            border-radius: 60px;
            padding: 10px 20px;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            z-index: 20;
            pointer-events: auto;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            border: 1px solid var(--border-light);
        }
        .plus-menu { position: relative; display: inline-block; }
        .plus-btn { background: var(--accent); width: 40px; height: 40px; border-radius: 40px; font-size: 24px; font-weight: bold; cursor: pointer; transition: 0.2s; display: flex; align-items: center; justify-content: center; color: white; border: none; }
        .plus-btn:hover { transform: scale(1.05); background: var(--accent-dark); }
        .mini-menu { position: absolute; bottom: 55px; left: 0; background: var(--card-bg); backdrop-filter: blur(8px); border-radius: 16px; overflow: hidden; box-shadow: 0 8px 20px rgba(0,0,0,0.15); display: none; flex-direction: column; z-index: 30; min-width: 180px; border: 1px solid var(--border-light); }
        .mini-menu.show { display: flex; }
        .mini-menu button { background: transparent; padding: 12px 18px; text-align: left; color: var(--text-primary); font-size: 13px; cursor: pointer; transition: 0.1s; display: flex; align-items: center; gap: 10px; border: none; width: 100%; }
        .mini-menu button:hover { background: var(--button-hover); }
        .mini-menu .menu-icon {
            width: 18px;
            height: 18px;
            stroke: currentColor;
            stroke-width: 1.8;
            fill: none;
        }

        .transport-group { display: flex; gap: 6px; align-items: center; background: var(--button-bg); padding: 4px 12px; border-radius: 50px; }
        .transport-controls { display: flex; gap: 8px; align-items: center; }
        .transport-controls button { background: var(--button-bg); border: none; width: 38px; height: 38px; border-radius: 38px; font-size: 18px; cursor: pointer; transition: 0.1s; display: inline-flex; align-items: center; justify-content: center; color: var(--text-secondary); }
        .transport-controls button:not(:disabled):hover { background: var(--accent); transform: scale(1.02); color: white; }
        .transport-controls button:disabled { opacity: 0.4; cursor: not-allowed; }
        .transport-controls .play-pause { background: var(--accent); color: white; font-weight: bold; width: 44px; height: 44px; font-size: 22px; }
        .mode-buttons { display: flex; gap: 6px; margin-left: 4px; }
        .mode-btn { background: var(--button-bg); width: 34px; height: 34px; border-radius: 34px; cursor: pointer; transition: 0.1s; display: inline-flex; align-items: center; justify-content: center; color: var(--text-secondary); border: none; }
        .mode-btn svg {
            width: 18px;
            height: 18px;
            fill: none;
            stroke: currentColor;
            stroke-width: 2;
            stroke-linecap: round;
            stroke-linejoin: round;
        }
        .mode-btn.active { background: var(--accent); color: white; box-shadow: 0 0 6px var(--accent); }
        .mode-btn:hover { background: var(--accent); color: white; transform: scale(1.02); }

        /* Seek bar */
        .seek-wrapper {
            display: flex;
            align-items: center;
            gap: 10px;
            flex: 2;
            min-width: 200px;
        }
        .seek-bar-container {
            flex: 1;
            position: relative;
            height: 6px;
            background: rgba(0,0,0,0.15);
            border-radius: 10px;
            cursor: pointer;
        }
        .seek-bar-fill {
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            width: 0%;
            background: var(--accent);
            border-radius: 10px;
            pointer-events: none;
        }
        .seek-bar-thumb {
            position: absolute;
            top: 50%;
            transform: translate(-50%, -50%);
            width: 14px;
            height: 14px;
            background: var(--accent);
            border-radius: 50%;
            cursor: pointer;
            pointer-events: none;
            box-shadow: 0 0 4px var(--accent);
        }
        .progress-timer {
            font-size: 12px;
            color: var(--text-secondary);
            font-family: monospace;
            min-width: 75px;
            text-align: right;
            font-weight: 500;
        }

        /* Volume slider */
        .volume-wrapper {
            display: flex;
            align-items: center;
            gap: 8px;
            background: var(--button-bg);
            padding: 4px 12px;
            border-radius: 40px;
        }
        .volume-icon {
            width: 18px;
            height: 18px;
            stroke: var(--accent);
            stroke-width: 1.8;
            fill: none;
            display: block;
        }
        .volume-slider-container {
            position: relative;
            width: 80px;
            height: 4px;
            background: rgba(0,0,0,0.15);
            border-radius: 4px;
            cursor: pointer;
        }
        .volume-fill {
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            width: 0%;
            background: var(--accent);
            border-radius: 4px;
            pointer-events: none;
        }
        .volume-slider-input {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0;
            cursor: pointer;
            margin: 0;
            z-index: 2;
        }
        .volume-slider-input::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: var(--accent);
            cursor: pointer;
            border: none;
            position: relative;
            z-index: 3;
        }
        .track-info {
            background: var(--button-hover);
            padding: 6px 14px;
            border-radius: 40px;
            color: var(--accent);
            font-size: 13px;
            font-weight: 500;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            max-width: 240px;
            cursor: help;
        }

        /* Settings button */
        .settings-btn {
            background: var(--button-bg);
            width: 40px;
            height: 40px;
            border-radius: 40px;
            cursor: pointer;
            transition: 0.2s;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            color: var(--text-secondary);
            border: none;
        }
        .settings-btn svg {
            width: 20px;
            height: 20px;
            stroke: currentColor;
            stroke-width: 1.8;
            fill: none;
            transition: 0.2s;
        }
        .settings-btn:hover {
            background: var(--accent);
            color: white;
            transform: scale(1.05);
        }

        /* Settings modal */
        .settings-modal { position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 320px; background: var(--card-bg); backdrop-filter: blur(16px); border-radius: 24px; z-index: 300; display: none; flex-direction: column; box-shadow: 0 20px 40px rgba(0,0,0,0.3); border: 1px solid var(--border-light); overflow: hidden; }
        .settings-modal.show { display: flex; }
        .settings-header { padding: 16px 20px; background: rgba(0,0,0,0.2); border-bottom: 1px solid var(--border-light); display: flex; justify-content: space-between; align-items: center; }
        .settings-header h3 { color: var(--accent); font-size: 18px; display: flex; align-items: center; gap: 8px; margin: 0; }
        .settings-header .settings-header-icon {
            width: 20px;
            height: 20px;
            stroke: currentColor;
            stroke-width: 1.8;
            fill: none;
        }
        .close-settings { background: var(--button-bg); border: none; width: 32px; height: 32px; border-radius: 32px; font-size: 20px; cursor: pointer; color: var(--text-secondary); }
        .close-settings:hover { background: var(--accent); color: white; }
        .settings-body { padding: 20px; display: flex; flex-direction: column; gap: 20px; }
        .about-text { font-size: 12px; color: var(--text-secondary); text-align: center; }
        .social-section {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .vk-button {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: #4680c2;
            color: white;
            text-decoration: none;
            padding: 8px 16px;
            border-radius: 40px;
            font-size: 14px;
            font-weight: 500;
            transition: 0.2s;
            border: none;
            cursor: pointer;
        }
        .vk-button:hover {
            background: #3a6dab;
            transform: scale(1.02);
        }
        .vk-icon {
            width: 18px;
            height: 18px;
            fill: white;
        }

        @media (max-width: 1000px) {
            .overlay-controls { padding: 8px 16px; gap: 10px; border-radius: 50px; }
            .transport-controls button { width: 34px; height: 34px; font-size: 16px; }
            .transport-controls .play-pause { width: 40px; height: 40px; font-size: 20px; }
            .mode-btn { width: 30px; height: 30px; }
            .mode-btn svg { width: 16px; height: 16px; }
            .seek-wrapper { min-width: 160px; }
            .volume-slider-container { width: 70px; }
            .track-info { max-width: 180px; font-size: 12px; }
            .app-logo { font-size: 14px; top: 15px; left: calc(var(--sidebar-width-collapsed) + 15px); }
        }
        @media (max-width: 800px) {
            .overlay-controls { flex-wrap: wrap; justify-content: center; bottom: 12px; left: 12px; right: 12px; border-radius: 40px; }
            .seek-wrapper { width: 100%; order: 1; }
            .track-info { order: 2; }
        }
    </style>
</head>
<body>
    <div class="app-logo">S.I.N.G.U.L.A.R.I.T.Y.</div>

    <!-- Sidebar -->
    <div class="sidebar" id="sidebar">
        <div class="sidebar-handle" id="sidebarHandle">
            <span class="logo-s">S</span>
            <span class="handle-text">Playlist Manager</span>
        </div>
        <div class="playlist-content">
            <div class="playlist-header">
                <span>
                    <svg class="header-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M4 4h16v16H4zM8 8h8M8 12h8M8 16h4" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M20 7l-6-3v13" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                    PLAYLISTS
                </span>
                <div class="playlist-actions">
                    <button id="newPlaylistBtn" title="New playlist">+</button>
                </div>
            </div>
            <div class="playlist-list" id="playlistList"></div>
            <div class="tracks-header">
                <svg class="header-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M9 18V5l12-2v13" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                    <circle cx="6" cy="18" r="3" stroke="currentColor" stroke-width="1.8" fill="none"/>
                    <circle cx="18" cy="16" r="3" stroke="currentColor" stroke-width="1.8" fill="none"/>
                </svg>
                CURRENT PLAYLIST
            </div>
            <div class="playlist-tracks" id="playlistTracks"></div>
        </div>
    </div>

    <div class="main-content">
        <div class="canvas-container">
            <canvas id="visualizer"></canvas>
            <div class="overlay-controls">
                <div class="plus-menu">
                    <button class="plus-btn" id="plusBtn">+</button>
                    <div class="mini-menu" id="miniMenu">
                        <button id="addFilesBtn">
                            <svg class="menu-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M13 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/>
                                <polyline points="13 2 13 9 20 9"/>
                                <path d="M12 13v6M9 16h6"/>
                            </svg>
                            Add files
                        </button>
                        <button id="loadFolderBtn">
                            <svg class="menu-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
                            </svg>
                            Add folder
                        </button>
                    </div>
                </div>
                <div class="transport-group">
                    <div class="transport-controls">
                        <button id="prevBtn" disabled>⏮</button>
                        <button id="playPauseBtn" class="play-pause" disabled>▶</button>
                        <button id="nextBtn" disabled>⏭</button>
                    </div>
                    <div class="mode-buttons">
                        <button id="shuffleBtn" class="mode-btn" title="Shuffle">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M16 3h5v5M4 20L21 3M21 16v5h-5M12 12l-8 8M12 12l8-8" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M21 16v5h-5M4 4l8 8" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </button>
                        <button id="repeatBtn" class="mode-btn" title="Repeat">
                            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path d="M17 2l4 4-4 4" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M3 12v-3c0-2.2 1.8-4 4-4h13" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M7 22l-4-4 4-4" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                                <path d="M21 12v3c0 2.2-1.8 4-4 4H4" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </button>
                    </div>
                </div>
                <div class="seek-wrapper">
                    <div class="seek-bar-container" id="seekBarContainer">
                        <div class="seek-bar-fill" id="seekBarFill"></div>
                        <div class="seek-bar-thumb" id="seekBarThumb"></div>
                    </div>
                    <div class="progress-timer" id="progressTimer">0:00 / 0:00</div>
                </div>
                <div class="volume-wrapper">
                    <svg class="volume-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M3 9h4l5-5v16l-5-5H3z" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M16 8a5 5 0 0 1 0 8" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round"/>
                        <path d="M19 5a8 8 0 0 1 0 14" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round"/>
                    </svg>
                    <div class="volume-slider-container" id="volumeSliderContainer">
                        <div class="volume-fill" id="volumeFill"></div>
                        <input type="range" id="volumeSlider" class="volume-slider-input" min="0" max="1" step="0.01" value="1.0">
                    </div>
                </div>
                <div class="track-info" id="trackName" title="No track loaded">No track loaded</div>
                <button class="settings-btn" id="settingsBtn">
                    <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9c.78.25 1.3.95 1.51 1.65h.09a2 2 0 0 1 0 4h-.09c-.21.7-.73 1.4-1.51 1.65z" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </button>
            </div>
        </div>
    </div>

    <!-- Settings Modal -->
    <div class="settings-modal" id="settingsModal">
        <div class="settings-header">
            <h3>
                <svg class="settings-header-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9c.78.25 1.3.95 1.51 1.65h.09a2 2 0 0 1 0 4h-.09c-.21.7-.73 1.4-1.51 1.65z" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                Settings
            </h3>
            <button class="close-settings" id="closeSettingsBtn">✕</button>
        </div>
        <div class="settings-body">
            <div class="about-text">Project S.I.N.G.U.L.A.R.I.T.Y.<br>Author: A.A. Korotchenko<br>Version: 0.8</div>
            <div class="social-section">
                <a href="https://vk.com/id695013563" target="_blank" class="vk-button">
                    VK
                </a>
            </div>
        </div>
    </div>

    <script>
        (function(){
            // DOM elements
            const sidebar = document.getElementById('sidebar');
            const sidebarHandle = document.getElementById('sidebarHandle');
            const newPlaylistBtn = document.getElementById('newPlaylistBtn');
            const playlistListDiv = document.getElementById('playlistList');
            const playlistTracksDiv = document.getElementById('playlistTracks');
            const plusBtn = document.getElementById('plusBtn');
            const miniMenu = document.getElementById('miniMenu');
            const addFilesBtn = document.getElementById('addFilesBtn');
            const loadFolderBtn = document.getElementById('loadFolderBtn');
            const prevBtn = document.getElementById('prevBtn');
            const playPauseBtn = document.getElementById('playPauseBtn');
            const nextBtn = document.getElementById('nextBtn');
            const shuffleBtn = document.getElementById('shuffleBtn');
            const repeatBtn = document.getElementById('repeatBtn');
            const volumeSlider = document.getElementById('volumeSlider');
            const volumeFill = document.getElementById('volumeFill');
            const seekBarContainer = document.getElementById('seekBarContainer');
            const seekBarFill = document.getElementById('seekBarFill');
            const seekBarThumb = document.getElementById('seekBarThumb');
            const trackNameSpan = document.getElementById('trackName');
            const progressTimer = document.getElementById('progressTimer');
            const canvas = document.getElementById('visualizer');
            const ctx = canvas.getContext('2d');
            const settingsBtn = document.getElementById('settingsBtn');
            const settingsModal = document.getElementById('settingsModal');
            const closeSettingsBtn = document.getElementById('closeSettingsBtn');

            // Helper to set track name and its tooltip
            function setTrackName(name) {
                trackNameSpan.textContent = name;
                trackNameSpan.title = name;
            }

            // Sidebar toggle
            sidebar.addEventListener('click', (e) => {
                if (!sidebar.classList.contains('expanded')) sidebar.classList.add('expanded');
            });
            sidebarHandle.addEventListener('click', (e) => {
                e.stopPropagation();
                sidebar.classList.remove('expanded');
            });

            // Settings modal - toggle on gear button, close on ✕ or outside click
            settingsBtn.onclick = () => settingsModal.classList.toggle('show');
            closeSettingsBtn.onclick = () => settingsModal.classList.remove('show');
            window.onclick = (e) => { if (e.target === settingsModal) settingsModal.classList.remove('show'); };

            // Seek bar functions
            function updateSeekBar(percent) {
                percent = Math.min(100, Math.max(0, percent));
                seekBarFill.style.width = percent + '%';
                seekBarThumb.style.left = percent + '%';
            }
            function getPercentFromClick(e) {
                const rect = seekBarContainer.getBoundingClientRect();
                let x = e.clientX - rect.left;
                x = Math.min(rect.width, Math.max(0, x));
                return (x / rect.width) * 100;
            }

            // Volume fill
            function updateVolumeFill(value) {
                const percent = value * 100;
                volumeFill.style.width = percent + '%';
            }
            volumeSlider.addEventListener('input', (e) => {
                updateVolumeFill(e.target.value);
                if (audioElement) audioElement.volume = e.target.value;
            });
            updateVolumeFill(volumeSlider.value);

            // ---------- Audio & playlist logic ----------
            let playlists = [], currentPlaylistId = null;
            let audioCtx = null, analyser = null, source = null, audioElement = null;
            let rafId = null, dataArray = null, previousMagnitudes = [];
            let currentTrackIndex = -1, shuffleActive = false, repeatActive = false;
            let isSeeking = false;
            const smoothingFactor = 0.85, barCount = 60;
            let startTime = Date.now(), paletteHue = 210;

            function generateId() { return Date.now() + '-' + Math.random().toString(36).substr(2, 6); }
            function initPlaylists() {
                playlists = [{ id: generateId(), name: 'Default', tracks: [] }];
                currentPlaylistId = playlists[0].id;
                renderPlaylistList();
                renderCurrentPlaylistTracks();
            }
            function renderPlaylistList() {
                playlistListDiv.innerHTML = '';
                playlists.forEach(pl => {
                    const div = document.createElement('div'); div.className = 'playlist-item';
                    if (pl.id === currentPlaylistId) div.classList.add('active');
                    const nameSpan = document.createElement('span'); nameSpan.className = 'playlist-name';
                    nameSpan.textContent = pl.name; nameSpan.title = pl.name;
                    nameSpan.onclick = (e) => { e.stopPropagation(); switchPlaylist(pl.id); };
                    const actionsDiv = document.createElement('div'); actionsDiv.className = 'playlist-item-actions';
                    const renameBtn = document.createElement('button');
                    renameBtn.innerHTML = '<svg class="action-icon" viewBox="0 0 24 24"><path d="M17 3l4 4-11 11H6v-4L17 3z"/><path d="M11 4l4 4"/></svg>';
                    renameBtn.title = 'Rename';
                    renameBtn.onclick = (e) => { e.stopPropagation(); renamePlaylist(pl.id); };
                    const deleteBtn = document.createElement('button');
                    deleteBtn.innerHTML = '<svg class="action-icon" viewBox="0 0 24 24"><path d="M4 7h16M10 11v6M14 11v6"/><path d="M5 7l1 13a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2l1-13"/><path d="M9 7V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v3"/></svg>';
                    deleteBtn.title = 'Delete';
                    deleteBtn.onclick = (e) => { e.stopPropagation(); deletePlaylist(pl.id); };
                    actionsDiv.appendChild(renameBtn);
                    actionsDiv.appendChild(deleteBtn);
                    div.appendChild(nameSpan);
                    div.appendChild(actionsDiv);
                    playlistListDiv.appendChild(div);
                });
            }
            function switchPlaylist(playlistId) {
                currentPlaylistId = playlistId;
                if (audioElement) { audioElement.pause(); audioElement.src = ''; if (source) source.disconnect(); }
                currentTrackIndex = -1;
                closeAudioContext();
                renderPlaylistList();
                renderCurrentPlaylistTracks();
                setTrackName('No track loaded');
                updatePlayPauseButton();
                updateNavigationButtons();
                updateSeekBar(0);
            }
            function renamePlaylist(playlistId) {
                const playlist = playlists.find(p => p.id === playlistId);
                if (!playlist) return;
                const newName = prompt('Enter new playlist name:', playlist.name);
                if (newName && newName.trim()) { playlist.name = newName.trim(); renderPlaylistList(); }
            }
            function deletePlaylist(playlistId) {
                if (playlists.length === 1) { alert('Cannot delete the last playlist.'); return; }
                if (confirm('Delete playlist "' + playlists.find(p => p.id === playlistId).name + '"?')) {
                    const index = playlists.findIndex(p => p.id === playlistId);
                    if (index !== -1) {
                        playlists.splice(index, 1);
                        if (currentPlaylistId === playlistId) {
                            currentPlaylistId = playlists[0].id;
                            switchPlaylist(currentPlaylistId);
                        } else renderPlaylistList();
                    }
                }
            }
            function createNewPlaylist() {
                let name = prompt('New playlist name:', 'Playlist ' + (playlists.length+1));
                if (!name) name = 'Playlist ' + (playlists.length+1);
                const newId = generateId();
                playlists.push({ id: newId, name: name, tracks: [] });
                renderPlaylistList();
                switchPlaylist(newId);
            }
            function deleteTrackFromCurrentPlaylist(trackIndex) {
                const playlist = playlists.find(p => p.id === currentPlaylistId);
                if (!playlist || trackIndex >= playlist.tracks.length) return;
                if (trackIndex === currentTrackIndex) {
                    if (audioElement) {
                        audioElement.pause();
                        audioElement.src = '';
                        if (source) source.disconnect();
                    }
                    currentTrackIndex = -1;
                    setTrackName('No track loaded');
                    updatePlayPauseButton();
                    updateSeekBar(0);
                    progressTimer.textContent = '0:00 / 0:00';
                } else if (trackIndex < currentTrackIndex) {
                    currentTrackIndex--;
                }
                playlist.tracks.splice(trackIndex, 1);
                renderCurrentPlaylistTracks();
                updateNavigationButtons();
                if (playlist.tracks.length === 0) {
                    if (audioElement) {
                        audioElement.pause();
                        audioElement.src = '';
                        if (source) source.disconnect();
                    }
                    currentTrackIndex = -1;
                    setTrackName('No track loaded');
                    updatePlayPauseButton();
                    updateSeekBar(0);
                    progressTimer.textContent = '0:00 / 0:00';
                }
            }
            function renderCurrentPlaylistTracks() {
                const playlist = playlists.find(p => p.id === currentPlaylistId);
                if (!playlist) return;
                playlistTracksDiv.innerHTML = '';
                playlist.tracks.forEach((track, idx) => {
                    const div = document.createElement('div'); div.className = 'track-item';
                    if (idx === currentTrackIndex) div.classList.add('active');
                    const trackNameSpanElem = document.createElement('span');
                    trackNameSpanElem.className = 'track-name';
                    trackNameSpanElem.textContent = track.name;
                    trackNameSpanElem.title = track.name;
                    const actionsDiv = document.createElement('div'); actionsDiv.className = 'track-actions';
                    const deleteBtn = document.createElement('button');
                    deleteBtn.innerHTML = '<svg class="action-icon" viewBox="0 0 24 24"><path d="M4 7h16M10 11v6M14 11v6"/><path d="M5 7l1 13a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2l1-13"/><path d="M9 7V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v3"/></svg>';
                    deleteBtn.title = 'Remove from playlist';
                    deleteBtn.onclick = (e) => { e.stopPropagation(); deleteTrackFromCurrentPlaylist(idx); };
                    actionsDiv.appendChild(deleteBtn);
                    div.appendChild(trackNameSpanElem);
                    div.appendChild(actionsDiv);
                    div.onclick = (e) => {
                        if (e.target.closest('.track-actions')) return;
                        loadTrackFromCurrentPlaylist(idx);
                    };
                    playlistTracksDiv.appendChild(div);
                });
            }
            function getNextPlaylist() {
                const currentIndex = playlists.findIndex(p => p.id === currentPlaylistId);
                if (currentIndex === -1 || playlists.length === 0) return null;
                return playlists[(currentIndex + 1) % playlists.length];
            }
            function loadFirstTrackOfPlaylist(playlistId) {
                const targetPlaylist = playlists.find(p => p.id === playlistId);
                if (targetPlaylist && targetPlaylist.tracks.length > 0) {
                    switchPlaylist(playlistId);
                    loadTrackFromCurrentPlaylist(0);
                }
            }
            async function loadTrackFromCurrentPlaylist(index) {
                const playlist = playlists.find(p => p.id === currentPlaylistId);
                if (!playlist || index >= playlist.tracks.length) return;
                if (audioElement) { audioElement.pause(); audioElement.src = ''; if (source) source.disconnect(); }
                await closeAudioContext();
                const track = playlist.tracks[index];
                audioElement = new Audio();
                audioElement.volume = volumeSlider.value;
                audioElement.src = track.url;
                setTrackName(track.name);
                audioCtx = new (AudioContext || webkitAudioContext)();
                analyser = audioCtx.createAnalyser();
                analyser.fftSize = 2048; analyser.smoothingTimeConstant = 0.75;
                dataArray = new Uint8Array(analyser.frequencyBinCount);
                previousMagnitudes = new Array(barCount).fill(0);
                source = audioCtx.createMediaElementSource(audioElement);
                source.connect(analyser);
                analyser.connect(audioCtx.destination);
                source.connect(audioCtx.destination);
                await audioCtx.resume();
                currentTrackIndex = index;
                updatePlayPauseButton();
                updateNavigationButtons();
                renderCurrentPlaylistTracks();
                render();
                audioElement.addEventListener('timeupdate', updateProgress);
                audioElement.addEventListener('loadedmetadata', updateProgress);
                audioElement.addEventListener('ended', () => {
                    const cp = playlists.find(p => p.id === currentPlaylistId);
                    if (!cp) return;
                    if (repeatActive) { audioElement.currentTime = 0; audioElement.play().catch(e=>console.log); return; }
                    if (shuffleActive && cp.tracks.length > 1) {
                        let newIdx = currentTrackIndex;
                        while (newIdx === currentTrackIndex && cp.tracks.length > 1) newIdx = Math.floor(Math.random() * cp.tracks.length);
                        loadTrackFromCurrentPlaylist(newIdx); return;
                    }
                    const nextIdx = currentTrackIndex + 1;
                    if (nextIdx < cp.tracks.length) loadTrackFromCurrentPlaylist(nextIdx);
                    else {
                        const nextPl = getNextPlaylist();
                        if (nextPl && nextPl.id !== currentPlaylistId && nextPl.tracks.length > 0) loadFirstTrackOfPlaylist(nextPl.id);
                        else updatePlayPauseButton();
                    }
                });
                updateProgress();
                audioElement.play().catch(e=>console.log);
                updatePlayPauseButton();
            }
            function updateProgress() {
                if (!audioElement || !isFinite(audioElement.duration)) {
                    updateSeekBar(0);
                    progressTimer.textContent = '0:00 / 0:00';
                    return;
                }
                const cur = audioElement.currentTime, dur = audioElement.duration;
                if (!isSeeking) {
                    const percent = (cur / dur) * 100;
                    updateSeekBar(percent);
                }
                const fmt = t => { let m = Math.floor(t/60), s = Math.floor(t%60); return m+':'+(s<10?'0':'')+s; };
                progressTimer.textContent = `${fmt(cur)} / ${fmt(dur)}`;
            }
            function seekTo(percent) {
                if (!audioElement || !isFinite(audioElement.duration)) return;
                const newTime = (percent / 100) * audioElement.duration;
                audioElement.currentTime = newTime;
                updateProgress();
            }

            let dragging = false;
            function handleSeekStart(e) {
                e.preventDefault();
                dragging = true;
                isSeeking = true;
                const percent = getPercentFromClick(e);
                updateSeekBar(percent);
                seekTo(percent);
                document.addEventListener('mousemove', handleSeekMove);
                document.addEventListener('mouseup', handleSeekEnd);
            }
            function handleSeekMove(e) {
                if (!dragging) return;
                const percent = getPercentFromClick(e);
                updateSeekBar(percent);
                seekTo(percent);
            }
            function handleSeekEnd() {
                dragging = false;
                isSeeking = false;
                document.removeEventListener('mousemove', handleSeekMove);
                document.removeEventListener('mouseup', handleSeekEnd);
            }
            seekBarContainer.addEventListener('mousedown', handleSeekStart);

            function getNextTrackIndex(playlist) {
                if (repeatActive) return currentTrackIndex;
                if (shuffleActive && playlist.tracks.length > 1) {
                    let newIdx = currentTrackIndex;
                    while (newIdx === currentTrackIndex && playlist.tracks.length > 1) newIdx = Math.floor(Math.random() * playlist.tracks.length);
                    return newIdx;
                }
                return (currentTrackIndex + 1) % playlist.tracks.length;
            }
            function updatePlayPauseButton() {
                if (!audioElement || !audioElement.src) { playPauseBtn.textContent = '▶'; playPauseBtn.disabled = true; return; }
                playPauseBtn.disabled = false; playPauseBtn.textContent = audioElement.paused ? '▶' : '⏸';
            }
            function updateNavigationButtons() {
                const playlist = playlists.find(p => p.id === currentPlaylistId);
                const hasMultiple = playlist && playlist.tracks.length > 1;
                prevBtn.disabled = !hasMultiple; nextBtn.disabled = !hasMultiple;
            }
            function playAudio() { if (audioElement && audioElement.src) { audioElement.play(); updatePlayPauseButton(); } }
            function pauseAudio() { if (audioElement) { audioElement.pause(); updatePlayPauseButton(); } }
            function togglePlayPause() { if (!audioElement || !audioElement.src) return; audioElement.paused ? playAudio() : pauseAudio(); }
            function nextTrack() {
                const playlist = playlists.find(p => p.id === currentPlaylistId);
                if (!playlist || !playlist.tracks.length) return;
                loadTrackFromCurrentPlaylist(getNextTrackIndex(playlist));
            }
            function prevTrack() {
                const playlist = playlists.find(p => p.id === currentPlaylistId);
                if (!playlist || !playlist.tracks.length) return;
                if (repeatActive && currentTrackIndex >= 0) { if (audioElement) { audioElement.currentTime = 0; if (audioElement.paused) playAudio(); } return; }
                let newIdx = currentTrackIndex - 1;
                if (newIdx < 0) newIdx = playlist.tracks.length - 1;
                loadTrackFromCurrentPlaylist(newIdx);
            }
            function setVolume(val) { if (audioElement) audioElement.volume = val; }
            function addTracksToCurrentPlaylist(files) {
                if (!files.length) return;
                const playlist = playlists.find(p => p.id === currentPlaylistId);
                if (!playlist) return;
                for (let file of files) {
                    if (!file.type.startsWith('audio/')) continue;
                    const url = URL.createObjectURL(file);
                    const track = { name: file.name, url, file, coverUrl: null };
                    playlist.tracks.push(track);
                    extractCoverFromFile(file, (cover) => { track.coverUrl = cover; if (currentPlaylistId === playlist.id && playlist.tracks[currentTrackIndex] === track) render(); });
                }
                renderCurrentPlaylistTracks();
                updateNavigationButtons();
                if (currentTrackIndex === -1 && playlist.tracks.length > 0) loadTrackFromCurrentPlaylist(0);
            }
            function addFolder() {
                const input = document.createElement('input');
                input.type = 'file';
                input.webkitdirectory = true;
                input.directory = true;
                input.onchange = e => {
                    if (e.target.files.length) {
                        const audioFiles = Array.from(e.target.files).filter(f => f.type.startsWith('audio/'));
                        if (audioFiles.length) addTracksToCurrentPlaylist(audioFiles);
                        else alert('No audio files found.');
                    }
                };
                input.click();
            }
            function addMultipleFiles() {
                const input = document.createElement('input');
                input.type = 'file';
                input.accept = 'audio/*';
                input.multiple = true;
                input.onchange = e => {
                    if (e.target.files.length) addTracksToCurrentPlaylist(Array.from(e.target.files));
                };
                input.click();
            }
            function extractCoverFromFile(file, callback) { if (!window.jsmediatags) { callback(null); return; } window.jsmediatags.read(file, { onSuccess: (tag) => { const pic = tag.tags.picture; if (pic && pic.data) { const base64 = btoa(new Uint8Array(pic.data).reduce((d,b)=>d+String.fromCharCode(b),'')); callback(`data:${pic.format||'image/jpeg'};base64,${base64}`); } else callback(null); }, onError: () => callback(null) }); }
            function toggleShuffle() { shuffleActive = !shuffleActive; if (shuffleActive) { shuffleBtn.classList.add('active'); if (repeatActive) { repeatActive = false; repeatBtn.classList.remove('active'); } } else shuffleBtn.classList.remove('active'); }
            function toggleRepeat() { repeatActive = !repeatActive; if (repeatActive) { repeatBtn.classList.add('active'); if (shuffleActive) { shuffleActive = false; shuffleBtn.classList.remove('active'); } } else repeatBtn.classList.remove('active'); }

            function updateUIPalette() { paletteHue = (paletteHue + 0.3) % 360; const accent = `hsl(${paletteHue}, 70%, 55%)`; document.documentElement.style.setProperty('--accent', accent); trackNameSpan.style.color = `hsl(${paletteHue}, 70%, 45%)`; seekBarFill.style.backgroundColor = accent; seekBarThumb.style.backgroundColor = accent; progressTimer.style.color = `hsl(${paletteHue}, 60%, 40%)`; volumeFill.style.backgroundColor = accent; if (shuffleActive) shuffleBtn.classList.add('active'); if (repeatActive) repeatBtn.classList.add('active'); }
            setInterval(updateUIPalette, 100);
            function resizeCanvas() { const rect = canvas.parentElement.getBoundingClientRect(); const ratio = devicePixelRatio || 1; canvas.width = rect.width * ratio; canvas.height = rect.height * ratio; canvas.style.width = `${rect.width}px`; canvas.style.height = `${rect.height}px`; }
            window.addEventListener('resize', resizeCanvas); resizeCanvas();
            function lerp(a,b,t) { return a + (b-a)*t; }
            function map(v,imin,imax,omin,omax) { return (v-imin)*(omax-omin)/(imax-imin)+omin; }
            async function closeAudioContext() { if (rafId) cancelAnimationFrame(rafId); if (audioCtx && audioCtx.state !== 'closed') await audioCtx.close(); audioCtx = null; analyser = null; source = null; dataArray = null; previousMagnitudes = []; }
            function getSmoothHue(angleNorm, energy, timeOff) { let hue = (angleNorm * 360 + timeOff + energy * 40) % 360; hue = (hue + Math.sin(angleNorm * Math.PI * 2) * 30) % 360; return Math.max(0, Math.min(360, hue)); }
            function drawBleedingBar(ctx, cx, cy, aStart, aEnd, rInner, rOuter, norm, hue) {
                const x1 = cx + Math.cos(aStart) * rInner, y1 = cy + Math.sin(aStart) * rInner;
                const x2 = cx + Math.cos(aStart) * rOuter, y2 = cy + Math.sin(aStart) * rOuter;
                const x3 = cx + Math.cos(aEnd) * rOuter,   y3 = cy + Math.sin(aEnd) * rOuter;
                const x4 = cx + Math.cos(aEnd) * rInner,   y4 = cy + Math.sin(aEnd) * rInner;
                const sat = map(norm, 0, 1, 65, 100), light = map(norm, 0, 1, 55, 80);
                ctx.beginPath(); ctx.moveTo(x1,y1); ctx.lineTo(x2,y2); ctx.lineTo(x3,y3); ctx.lineTo(x4,y4); ctx.closePath();
                ctx.shadowColor = `hsl(${hue}, 80%, 60%)`; ctx.shadowBlur = Math.max(4, norm * 12);
                ctx.fillStyle = `hsl(${hue}, ${sat}%, ${light}%)`; ctx.fill(); ctx.shadowBlur = 0;
            }
            function drawCoverArt(ctx, cx, cy, radius, coverUrl, scale) {
                const r = radius * scale;
                if (coverUrl) {
                    const img = new Image(); img.src = coverUrl;
                    if (img.complete) {
                        ctx.save(); ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI*2); ctx.clip();
                        ctx.drawImage(img, cx - r, cy - r, r*2, r*2);
                        ctx.restore();
                    } else {
                        img.onload = () => {};
                        ctx.fillStyle = 'rgba(0,0,0,0.5)';
                        ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI*2); ctx.fill();
                        ctx.save(); ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI*2); ctx.clip();
                        const grad = ctx.createLinearGradient(cx - r/2, cy - r/2, cx + r/2, cy + r/2);
                        grad.addColorStop(0, `hsl(${paletteHue}, 70%, 55%)`);
                        grad.addColorStop(1, `hsl(${paletteHue - 15}, 60%, 45%)`);
                        ctx.fillStyle = grad;
                        ctx.font = `bold ${r * 0.7}px 'Inter', sans-serif`;
                        ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
                        ctx.fillText('S', cx, cy);
                        ctx.restore();
                    }
                } else {
                    ctx.fillStyle = 'rgba(0,0,0,0.5)';
                    ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI*2); ctx.fill();
                    ctx.save(); ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI*2); ctx.clip();
                    const grad = ctx.createLinearGradient(cx - r/2, cy - r/2, cx + r/2, cy + r/2);
                    grad.addColorStop(0, `hsl(${paletteHue}, 70%, 55%)`);
                    grad.addColorStop(1, `hsl(${paletteHue - 15}, 60%, 45%)`);
                    ctx.fillStyle = grad;
                    ctx.font = `bold ${r * 0.7}px 'Inter', sans-serif`;
                    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
                    ctx.fillText('S', cx, cy);
                    ctx.restore();
                }
            }
            function render() {
                if (!analyser || !dataArray) { rafId = requestAnimationFrame(render); return; }
                analyser.getByteFrequencyData(dataArray);
                const w = canvas.width, h = canvas.height; ctx.clearRect(0,0,w,h);
                const cx = w/2, cy = h/2, baseR = Math.min(w,h)*0.20, maxR = Math.min(w,h)*0.42;
                const step = Math.max(1, Math.floor(dataArray.length / barCount));
                let energy = 0, cnt = 0;
                for (let i=0; i<dataArray.length; i+=step) { energy += dataArray[i]; cnt++; }
                const energyNorm = energy / Math.max(1,cnt) / 255;
                const timeOff = (Date.now() - startTime) * 0.03;
                const angleStep = (Math.PI*2)/barCount;
                for (let i=0; i<barCount; i++) {
                    const idx = Math.min(dataArray.length-1, i*step);
                    const mag = dataArray[idx];
                    const smooth = lerp(previousMagnitudes[i]||0, mag, 1-smoothingFactor);
                    previousMagnitudes[i] = smooth;
                    const norm = smooth/255;
                    const inner = baseR + Math.pow(norm,1.4)*(maxR-baseR)*0.2;
                    const outer = inner + norm*(maxR-inner)*0.92;
                    const aStart = i*angleStep, aEnd = (i+1)*angleStep;
                    const hue = getSmoothHue(i/barCount, energyNorm, timeOff);
                    drawBleedingBar(ctx, cx, cy, aStart, aEnd, inner, outer, norm, hue);
                    drawBleedingBar(ctx, cx, cy, aStart+Math.PI, aEnd+Math.PI, inner, outer, norm, hue);
                }
                const playlist = playlists.find(p => p.id === currentPlaylistId);
                const cover = (playlist && currentTrackIndex >=0 && playlist.tracks[currentTrackIndex]) ? playlist.tracks[currentTrackIndex].coverUrl : null;
                const coverScale = 0.9 + energyNorm * 0.4;
                drawCoverArt(ctx, cx, cy, baseR*0.86, cover, coverScale);
                rafId = requestAnimationFrame(render);
            }

            // Event binding
            plusBtn.onclick = (e) => { e.stopPropagation(); miniMenu.classList.toggle('show'); };
            document.onclick = () => miniMenu.classList.remove('show');
            addFilesBtn.onclick = (e) => { e.stopPropagation(); addMultipleFiles(); miniMenu.classList.remove('show'); };
            loadFolderBtn.onclick = (e) => { e.stopPropagation(); addFolder(); miniMenu.classList.remove('show'); };
            playPauseBtn.onclick = togglePlayPause; prevBtn.onclick = prevTrack; nextBtn.onclick = nextTrack;
            shuffleBtn.onclick = toggleShuffle; repeatBtn.onclick = toggleRepeat;
            newPlaylistBtn.onclick = createNewPlaylist;
            window.onbeforeunload = () => { if (audioElement) audioElement.pause(); if (audioCtx) audioCtx.close(); if (rafId) cancelAnimationFrame(rafId); };
            resizeCanvas(); render(); setInterval(updateProgress, 200);
            initPlaylists();
        })();
    </script>
</body>
</html>
"""

class WebViewApp:
    def __init__(self):
        self.window = webview.create_window(
            title="Project S.I.N.G.U.L.A.R.I.T.Y.",
            html=HTML_CONTENT,
            width=1200,
            height=800,
            resizable=True,
            fullscreen=False,
            min_size=(800, 600)
        )

    def run(self):
        webview.start(debug=False, http_server=True)

if __name__ == "__main__":
    app = WebViewApp()
    app.run()
