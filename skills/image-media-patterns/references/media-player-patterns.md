# Media Player Patterns — Video, Audio, Upload & Avatar Components

Production-ready specifications for video/audio player UIs, file upload patterns, and avatar component implementations.

---

## 1. Custom Video Player — Complete Spec

### Layout Structure

```
+----------------------------------------------------------------------+
|                                                                      |
|                          VIDEO FRAME                                 |
|                                                                      |
|                       [  ▶  PLAY  ]   (centered overlay)             |
|                                                                      |
+----------------------------------------------------------------------+
| ▶ | ◄◄ | ►► | ===●============= | 2:34 / 5:12 | 🔊━━ | CC | ⚙ | ⛶ |
+----------------------------------------------------------------------+
```

### Controls Bar Specification

| Element | Width | Height | Position | Behavior |
|---------|-------|--------|----------|----------|
| Play/Pause button | 44px | 44px | Left | Toggle ▶/❚❚ icon |
| Skip back (10s) | 36px | 36px | After play | Jump -10s, icon: ↺ |
| Skip forward (10s) | 36px | 36px | After skip back | Jump +10s, icon: ↻ |
| Progress bar | Flex | 4px (8px hover) | Center, fills space | Seekable, shows buffer |
| Time display | Auto | 44px | After progress | "2:34 / 5:12" |
| Volume button | 36px | 36px | Right group | Click: toggle mute |
| Volume slider | 80px | 4px | After volume icon | Horizontal, 0-100% |
| Captions (CC) | 36px | 36px | Right group | Toggle subtitles |
| Settings (gear) | 36px | 36px | Right group | Speed, quality menu |
| Fullscreen | 36px | 36px | Far right | Toggle fullscreen |

### Progress Bar Detail

```css
.video-progress {
  position: relative;
  height: 4px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 2px;
  cursor: pointer;
  transition: height 0.15s ease;
}

.video-progress:hover {
  height: 8px;
}

/* Buffered range */
.video-progress-buffer {
  position: absolute;
  height: 100%;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 2px;
}

/* Played range */
.video-progress-played {
  position: absolute;
  height: 100%;
  background: #ef4444; /* YouTube red or brand color */
  border-radius: 2px;
}

/* Scrubber thumb */
.video-progress-thumb {
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%) scale(0);
  width: 14px;
  height: 14px;
  background: #ef4444;
  border-radius: 50%;
  transition: transform 0.15s ease;
}

.video-progress:hover .video-progress-thumb {
  transform: translate(-50%, -50%) scale(1);
}

/* Preview thumbnail on hover */
.video-progress-preview {
  position: absolute;
  bottom: 100%;
  transform: translateX(-50%);
  margin-bottom: 8px;
  width: 160px;
  aspect-ratio: 16/9;
  background: #000;
  border-radius: 4px;
  overflow: hidden;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.15s;
}

.video-progress:hover .video-progress-preview {
  opacity: 1;
}
```

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| Space / K | Play/Pause |
| J | Rewind 10 seconds |
| L | Forward 10 seconds |
| Left Arrow | Rewind 5 seconds |
| Right Arrow | Forward 5 seconds |
| Up Arrow | Volume up 5% |
| Down Arrow | Volume down 5% |
| M | Toggle mute |
| F | Toggle fullscreen |
| C | Toggle captions |
| < (Shift+,) | Decrease speed |
| > (Shift+.) | Increase speed |
| 0-9 | Jump to 0%-90% of video |
| Home | Jump to beginning |
| End | Jump to end |
| Escape | Exit fullscreen |

### Controls Auto-Hide

```javascript
class VideoControls {
  constructor(player) {
    this.player = player;
    this.controls = player.querySelector('.video-controls');
    this.hideTimeout = null;
    this.isPlaying = false;

    // Show controls on mouse movement
    player.addEventListener('mousemove', () => this.showControls());
    player.addEventListener('mouseleave', () => this.scheduleHide());

    // Always show when paused
    player.querySelector('video').addEventListener('pause', () => {
      this.isPlaying = false;
      this.showControls();
    });

    player.querySelector('video').addEventListener('play', () => {
      this.isPlaying = true;
      this.scheduleHide();
    });

    // Show on focus within controls
    this.controls.addEventListener('focusin', () => this.showControls());
    this.controls.addEventListener('focusout', () => {
      if (this.isPlaying) this.scheduleHide();
    });
  }

  showControls() {
    clearTimeout(this.hideTimeout);
    this.controls.classList.remove('hidden');
    this.player.style.cursor = 'default';
    if (this.isPlaying) this.scheduleHide();
  }

  scheduleHide() {
    clearTimeout(this.hideTimeout);
    this.hideTimeout = setTimeout(() => {
      this.controls.classList.add('hidden');
      this.player.style.cursor = 'none';
    }, 3000);
  }
}
```

```css
.video-controls {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 8px 16px;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.7));
  display: flex;
  align-items: center;
  gap: 8px;
  transition: opacity 0.3s ease, visibility 0.3s ease;
}

.video-controls.hidden {
  opacity: 0;
  visibility: hidden;
}
```

---

## 2. Picture-in-Picture (Scroll-Triggered)

```javascript
class ScrollPiP {
  constructor(videoElement) {
    this.video = videoElement;
    this.pip = document.createElement('div');
    this.pip.className = 'pip-container';
    this.pip.hidden = true;
    document.body.appendChild(this.pip);

    this.setupObserver();
    this.setupClose();
  }

  setupObserver() {
    this.observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          // Only PiP if video is playing
          if (!this.video.paused) {
            if (!entry.isIntersecting) {
              this.enterPiP();
            } else {
              this.exitPiP();
            }
          }
        });
      },
      { threshold: 0.5 }
    );
    this.observer.observe(this.video);
  }

  enterPiP() {
    // Move video to PiP container
    this.pip.appendChild(this.video);
    this.pip.hidden = false;
  }

  exitPiP() {
    // Move video back to original container
    this.originalParent.appendChild(this.video);
    this.pip.hidden = true;
  }

  setupClose() {
    const closeBtn = document.createElement('button');
    closeBtn.className = 'pip-close';
    closeBtn.setAttribute('aria-label', 'Close mini player');
    closeBtn.innerHTML = '&times;';
    closeBtn.addEventListener('click', () => {
      this.video.pause();
      this.exitPiP();
    });
    this.pip.appendChild(closeBtn);
  }
}
```

```css
.pip-container {
  position: fixed;
  bottom: 24px;
  right: 24px;
  width: 360px;
  aspect-ratio: 16/9;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  z-index: 9000;
  transition: transform 0.3s ease;
}

.pip-container[hidden] { display: none; }

.pip-container video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.pip-close {
  position: absolute;
  top: 8px;
  right: 8px;
  width: 28px;
  height: 28px;
  background: rgba(0, 0, 0, 0.6);
  color: white;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  font-size: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Responsive: smaller on mobile */
@media (max-width: 640px) {
  .pip-container {
    width: 200px;
    bottom: 16px;
    right: 16px;
  }
}
```

---

## 3. Audio Player — Full Implementation

### Waveform Player

```html
<div class="audio-player" role="region" aria-label="Audio player">
  <button class="audio-play" aria-label="Play">
    <svg class="icon-play" width="20" height="20"><polygon points="5,3 17,10 5,17" fill="currentColor"/></svg>
    <svg class="icon-pause" width="20" height="20" hidden><rect x="4" y="3" width="4" height="14" fill="currentColor"/><rect x="12" y="3" width="4" height="14" fill="currentColor"/></svg>
  </button>

  <div class="audio-waveform" role="slider" aria-label="Audio position" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" tabindex="0">
    <canvas class="waveform-canvas" width="600" height="48"></canvas>
    <div class="waveform-progress"></div>
  </div>

  <span class="audio-time" aria-live="off">
    <span class="audio-current">0:00</span> / <span class="audio-duration">3:42</span>
  </span>

  <div class="audio-speed">
    <button class="speed-btn" aria-label="Playback speed: 1x">1x</button>
  </div>
</div>
```

```css
.audio-player {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  background: #f3f4f6;
  border-radius: 12px;
  max-width: 600px;
}

.audio-play {
  flex: 0 0 40px;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  background: #111827;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}

.audio-play:hover { background: #374151; }

.audio-waveform {
  flex: 1;
  position: relative;
  height: 48px;
  cursor: pointer;
  border-radius: 4px;
}

.waveform-canvas {
  width: 100%;
  height: 100%;
  display: block;
}

.waveform-progress {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 0%;
  background: rgba(37, 99, 235, 0.2);
  pointer-events: none;
  border-radius: 4px;
}

.audio-time {
  flex: 0 0 auto;
  font-size: 13px;
  color: #6b7280;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}

.speed-btn {
  padding: 4px 8px;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  background: white;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
}
```

### Waveform Rendering

```javascript
function renderWaveform(canvas, peaks, playedColor = '#2563eb', unplayedColor = '#d1d5db') {
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const width = canvas.offsetWidth * dpr;
  const height = canvas.offsetHeight * dpr;
  canvas.width = width;
  canvas.height = height;
  ctx.scale(dpr, dpr);

  const displayWidth = canvas.offsetWidth;
  const displayHeight = canvas.offsetHeight;
  const barWidth = 3;
  const barGap = 2;
  const totalBarWidth = barWidth + barGap;
  const barCount = Math.floor(displayWidth / totalBarWidth);

  // Resample peaks to match bar count
  const step = peaks.length / barCount;

  ctx.clearRect(0, 0, displayWidth, displayHeight);

  for (let i = 0; i < barCount; i++) {
    const peakIndex = Math.floor(i * step);
    const amplitude = peaks[peakIndex] || 0;
    const barHeight = Math.max(2, amplitude * displayHeight * 0.8);
    const x = i * totalBarWidth;
    const y = (displayHeight - barHeight) / 2;

    ctx.fillStyle = unplayedColor;
    ctx.beginPath();
    ctx.roundRect(x, y, barWidth, barHeight, 1);
    ctx.fill();
  }
}

// Redraw with progress overlay
function updateWaveformProgress(canvas, peaks, progress, playedColor, unplayedColor) {
  renderWaveform(canvas, peaks, playedColor, unplayedColor);

  const ctx = canvas.getContext('2d');
  const displayWidth = canvas.offsetWidth;
  const displayHeight = canvas.offsetHeight;
  const barWidth = 3;
  const barGap = 2;
  const totalBarWidth = barWidth + barGap;
  const barCount = Math.floor(displayWidth / totalBarWidth);
  const step = peaks.length / barCount;
  const playedBars = Math.floor(barCount * progress);

  for (let i = 0; i < playedBars; i++) {
    const peakIndex = Math.floor(i * step);
    const amplitude = peaks[peakIndex] || 0;
    const barHeight = Math.max(2, amplitude * displayHeight * 0.8);
    const x = i * totalBarWidth;
    const y = (displayHeight - barHeight) / 2;

    ctx.fillStyle = playedColor;
    ctx.beginPath();
    ctx.roundRect(x, y, barWidth, barHeight, 1);
    ctx.fill();
  }
}
```

---

## 4. Podcast Player

```html
<div class="podcast-player" role="region" aria-label="Podcast player: Episode Title">
  <!-- Album art -->
  <div class="podcast-art">
    <img src="episode-art.webp" alt="Episode artwork" width="300" height="300">
  </div>

  <!-- Info -->
  <div class="podcast-info">
    <h3 class="podcast-title">Episode 42: Design Systems at Scale</h3>
    <p class="podcast-show">The Design Podcast</p>
  </div>

  <!-- Progress -->
  <div class="podcast-progress">
    <input type="range" min="0" max="100" value="35" class="podcast-seek"
           aria-label="Seek position" aria-valuetext="12 minutes 34 seconds of 36 minutes">
    <div class="podcast-times">
      <span class="podcast-elapsed">12:34</span>
      <span class="podcast-remaining">-23:26</span>
    </div>
  </div>

  <!-- Controls -->
  <div class="podcast-controls">
    <button class="podcast-skip-back" aria-label="Skip back 15 seconds">
      <svg><!-- -15 icon --></svg>
    </button>
    <button class="podcast-play" aria-label="Play">
      <svg><!-- play/pause icon --></svg>
    </button>
    <button class="podcast-skip-forward" aria-label="Skip forward 30 seconds">
      <svg><!-- +30 icon --></svg>
    </button>
  </div>

  <!-- Secondary controls -->
  <div class="podcast-secondary">
    <button class="podcast-speed" aria-label="Playback speed: 1x">1x</button>
    <button class="podcast-sleep" aria-label="Sleep timer">🌙</button>
    <button class="podcast-chapters" aria-label="Chapters">📑</button>
    <button class="podcast-transcript" aria-label="Show transcript">📝</button>
  </div>
</div>
```

### Playback Speed Cycle

```javascript
const speeds = [0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.5, 3];

class SpeedControl {
  constructor(button, audioElement) {
    this.btn = button;
    this.audio = audioElement;
    this.index = 2; // default: 1x

    this.btn.addEventListener('click', () => this.cycle());
  }

  cycle() {
    this.index = (this.index + 1) % speeds.length;
    const speed = speeds[this.index];
    this.audio.playbackRate = speed;
    this.btn.textContent = speed === 1 ? '1x' : `${speed}x`;
    this.btn.setAttribute('aria-label', `Playback speed: ${speed}x`);
  }
}
```

---

## 5. Voice Message Player (Chat/Messaging)

```html
<div class="voice-message" role="region" aria-label="Voice message from Jane, 0:23">
  <div class="voice-avatar">
    <img src="jane-avatar.webp" alt="" width="36" height="36">
  </div>
  <button class="voice-play" aria-label="Play voice message">
    <svg class="icon-play" width="16" height="16"><polygon points="4,2 14,8 4,14" fill="currentColor"/></svg>
  </button>
  <div class="voice-waveform" role="slider" aria-label="Voice message position"
       aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" tabindex="0">
    <canvas width="200" height="28"></canvas>
  </div>
  <span class="voice-duration">0:23</span>
  <button class="voice-speed" aria-label="Speed: 1x">1x</button>
</div>
```

```css
.voice-message {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  background: #e5efff;
  border-radius: 18px;
  max-width: 320px;
}

.voice-avatar {
  flex: 0 0 36px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  overflow: hidden;
}

.voice-avatar img { width: 100%; height: 100%; object-fit: cover; }

.voice-play {
  flex: 0 0 28px;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: none;
  background: #2563eb;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.voice-waveform {
  flex: 1;
  height: 28px;
  cursor: pointer;
}

.voice-duration {
  font-size: 12px;
  color: #6b7280;
  font-variant-numeric: tabular-nums;
}

.voice-speed {
  font-size: 11px;
  padding: 2px 6px;
  border: 1px solid #bfdbfe;
  border-radius: 10px;
  background: white;
  cursor: pointer;
  font-weight: 600;
}
```

---

## 6. Upload Patterns — Complete Implementation

### Drag-and-Drop Upload Zone

```html
<div class="upload-zone" role="button" tabindex="0" aria-label="Upload images, drag and drop or click to browse">
  <input type="file" class="upload-input" accept="image/jpeg,image/png,image/webp,image/avif"
         multiple hidden aria-hidden="true">

  <div class="upload-idle">
    <svg class="upload-icon" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
      <path d="M12 16V4m0 0L8 8m4-4l4 4M4 17v2a2 2 0 002 2h12a2 2 0 002-2v-2"/>
    </svg>
    <p class="upload-text"><strong>Drag and drop</strong> images here</p>
    <p class="upload-subtext">or click to browse</p>
    <p class="upload-formats">JPG, PNG, WebP, AVIF up to 10 MB each</p>
  </div>

  <div class="upload-dragover" hidden>
    <p>Drop files to upload</p>
  </div>
</div>

<!-- Preview area -->
<div class="upload-previews" role="list" aria-label="Uploaded files"></div>
```

```css
.upload-zone {
  border: 2px dashed #d1d5db;
  border-radius: 16px;
  padding: 48px 24px;
  text-align: center;
  cursor: pointer;
  transition: border-color 0.2s, background-color 0.2s;
  position: relative;
}

.upload-zone:hover {
  border-color: #9ca3af;
  background: #f9fafb;
}

.upload-zone.dragover {
  border-color: #2563eb;
  background: #eff6ff;
  border-style: solid;
}

.upload-zone:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: 2px;
}

.upload-icon {
  color: #9ca3af;
  margin-bottom: 12px;
}

.upload-text {
  font-size: 16px;
  color: #374151;
  margin-bottom: 4px;
}

.upload-subtext {
  font-size: 14px;
  color: #6b7280;
}

.upload-formats {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 8px;
}

/* Preview grid */
.upload-previews {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  gap: 12px;
  margin-top: 16px;
}

.upload-preview-item {
  position: relative;
  aspect-ratio: 1;
  border-radius: 8px;
  overflow: hidden;
  background: #f3f4f6;
}

.upload-preview-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.upload-preview-item .remove-btn {
  position: absolute;
  top: 4px;
  right: 4px;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: none;
  background: rgba(0, 0, 0, 0.6);
  color: white;
  cursor: pointer;
  font-size: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Upload progress overlay */
.upload-preview-item .progress-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
}

.upload-preview-item .progress-ring {
  width: 40px;
  height: 40px;
}
```

### JavaScript

```javascript
class FileUploader {
  constructor(container, options = {}) {
    this.zone = container.querySelector('.upload-zone');
    this.input = container.querySelector('.upload-input');
    this.previews = container.querySelector('.upload-previews');
    this.maxSize = options.maxSize || 10 * 1024 * 1024; // 10MB
    this.maxFiles = options.maxFiles || 20;
    this.acceptedTypes = options.acceptedTypes || ['image/jpeg', 'image/png', 'image/webp', 'image/avif'];
    this.files = [];
    this.onUpload = options.onUpload || (() => {});

    this.bindEvents();
  }

  bindEvents() {
    // Click to open file picker
    this.zone.addEventListener('click', () => this.input.click());
    this.zone.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        this.input.click();
      }
    });

    // File input change
    this.input.addEventListener('change', (e) => this.handleFiles(e.target.files));

    // Drag and drop
    this.zone.addEventListener('dragenter', (e) => this.onDragEnter(e));
    this.zone.addEventListener('dragover', (e) => this.onDragOver(e));
    this.zone.addEventListener('dragleave', (e) => this.onDragLeave(e));
    this.zone.addEventListener('drop', (e) => this.onDrop(e));

    // Paste
    document.addEventListener('paste', (e) => this.onPaste(e));
  }

  onDragEnter(e) {
    e.preventDefault();
    this.zone.classList.add('dragover');
  }

  onDragOver(e) {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'copy';
  }

  onDragLeave(e) {
    // Only remove if leaving the zone entirely
    if (!this.zone.contains(e.relatedTarget)) {
      this.zone.classList.remove('dragover');
    }
  }

  onDrop(e) {
    e.preventDefault();
    this.zone.classList.remove('dragover');
    this.handleFiles(e.dataTransfer.files);
  }

  onPaste(e) {
    const items = e.clipboardData?.items;
    if (!items) return;

    const imageFiles = [];
    for (const item of items) {
      if (item.type.startsWith('image/')) {
        const file = item.getAsFile();
        if (file) imageFiles.push(file);
      }
    }

    if (imageFiles.length > 0) {
      this.handleFiles(imageFiles);
    }
  }

  handleFiles(fileList) {
    const files = Array.from(fileList);

    files.forEach(file => {
      // Validate type
      if (!this.acceptedTypes.includes(file.type)) {
        this.showError(file, `Unsupported format: ${file.type}`);
        return;
      }

      // Validate size
      if (file.size > this.maxSize) {
        this.showError(file, `File too large: ${(file.size / 1024 / 1024).toFixed(1)}MB (max ${this.maxSize / 1024 / 1024}MB)`);
        return;
      }

      // Validate count
      if (this.files.length >= this.maxFiles) {
        this.showError(file, `Maximum ${this.maxFiles} files`);
        return;
      }

      this.files.push(file);
      this.addPreview(file);
      this.onUpload(file);
    });
  }

  addPreview(file) {
    const item = document.createElement('div');
    item.className = 'upload-preview-item';
    item.setAttribute('role', 'listitem');

    const img = document.createElement('img');
    img.alt = file.name;
    const url = URL.createObjectURL(file);
    img.src = url;
    img.onload = () => URL.revokeObjectURL(url);

    const removeBtn = document.createElement('button');
    removeBtn.className = 'remove-btn';
    removeBtn.setAttribute('aria-label', `Remove ${file.name}`);
    removeBtn.textContent = '\u00d7';
    removeBtn.addEventListener('click', () => {
      this.files = this.files.filter(f => f !== file);
      item.remove();
    });

    item.appendChild(img);
    item.appendChild(removeBtn);
    this.previews.appendChild(item);
  }

  showError(file, message) {
    console.error(`Upload error for ${file.name}: ${message}`);
    // Show toast notification or inline error
  }
}

// Initialize
new FileUploader(document.querySelector('.upload-container'), {
  maxSize: 10 * 1024 * 1024,
  maxFiles: 20,
  onUpload: (file) => {
    // Send to server via fetch/XMLHttpRequest with progress tracking
  }
});
```

---

## 7. Upload Progress with XHR

```javascript
function uploadFile(file, url, onProgress) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    const formData = new FormData();
    formData.append('file', file);

    xhr.upload.addEventListener('progress', (e) => {
      if (e.lengthComputable) {
        const percent = Math.round((e.loaded / e.total) * 100);
        onProgress(percent);
      }
    });

    xhr.addEventListener('load', () => {
      if (xhr.status >= 200 && xhr.status < 300) {
        resolve(JSON.parse(xhr.responseText));
      } else {
        reject(new Error(`Upload failed: ${xhr.status}`));
      }
    });

    xhr.addEventListener('error', () => reject(new Error('Network error')));
    xhr.addEventListener('abort', () => reject(new Error('Upload cancelled')));

    xhr.open('POST', url);
    xhr.send(formData);
  });
}

// Usage
uploadFile(file, '/api/upload', (percent) => {
  progressBar.style.width = `${percent}%`;
  progressText.textContent = `${percent}%`;
});
```

---

## 8. Avatar Component — React

```jsx
import React from 'react';

const SIZES = {
  xs: 24, sm: 32, md: 40, lg: 48, xl: 64, '2xl': 80, '3xl': 128,
};

const COLORS = [
  '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4',
  '#FFEAA7', '#DDA0DD', '#98D8C8', '#F7DC6F',
  '#FF8A80', '#80CBC4', '#81D4FA', '#C5E1A5',
];

function getInitials(name) {
  if (!name) return '?';
  const parts = name.trim().split(/\s+/);
  if (parts.length === 1) return parts[0][0].toUpperCase();
  return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
}

function getColor(identifier) {
  let hash = 0;
  for (let i = 0; i < identifier.length; i++) {
    hash = identifier.charCodeAt(i) + ((hash << 5) - hash);
  }
  return COLORS[Math.abs(hash) % COLORS.length];
}

/**
 * Avatar component with image, initials fallback, and status indicator.
 *
 * @param {Object} props
 * @param {string} [props.src] - Image URL
 * @param {string} [props.name] - User name (for initials fallback)
 * @param {string} [props.userId] - Unique ID (for color generation)
 * @param {'xs'|'sm'|'md'|'lg'|'xl'|'2xl'|'3xl'} [props.size='md']
 * @param {'circle'|'rounded'} [props.shape='circle']
 * @param {'online'|'away'|'busy'|'offline'} [props.status]
 * @param {string} [props.alt]
 */
function Avatar({
  src,
  name,
  userId,
  size = 'md',
  shape = 'circle',
  status,
  alt,
  ...rest
}) {
  const px = SIZES[size] || SIZES.md;
  const borderRadius = shape === 'circle' ? '50%' : '20%';
  const [imgError, setImgError] = React.useState(false);

  const statusColors = {
    online: '#22C55E',
    away: '#EAB308',
    busy: '#EF4444',
    offline: '#9CA3AF',
  };

  const statusSize = Math.max(8, Math.round(px * 0.28));
  const fontSize = Math.round(px * 0.4);

  const containerStyle = {
    position: 'relative',
    display: 'inline-flex',
    width: px,
    height: px,
    flexShrink: 0,
  };

  const avatarStyle = {
    width: px,
    height: px,
    borderRadius,
    overflow: 'hidden',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize,
    fontWeight: 600,
    color: 'white',
    backgroundColor: src && !imgError ? '#e5e7eb' : getColor(userId || name || 'default'),
    userSelect: 'none',
  };

  const statusStyle = {
    position: 'absolute',
    bottom: 0,
    right: 0,
    width: statusSize,
    height: statusSize,
    borderRadius: '50%',
    backgroundColor: statusColors[status],
    border: '2px solid white',
    boxSizing: 'content-box',
  };

  return (
    <div style={containerStyle} {...rest}>
      <div style={avatarStyle} role="img" aria-label={alt || name || 'User avatar'}>
        {src && !imgError ? (
          <img
            src={src}
            alt=""
            onError={() => setImgError(true)}
            style={{ width: '100%', height: '100%', objectFit: 'cover' }}
          />
        ) : name ? (
          getInitials(name)
        ) : (
          <svg width={px * 0.5} height={px * 0.5} viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 12c2.7 0 5-2.3 5-5s-2.3-5-5-5-5 2.3-5 5 2.3 5 5 5zm0 2c-3.3 0-10 1.7-10 5v2h20v-2c0-3.3-6.7-5-10-5z"/>
          </svg>
        )}
      </div>
      {status && <div style={statusStyle} aria-label={status} />}
    </div>
  );
}

/**
 * Avatar group with overlap and +N overflow.
 *
 * @param {Object} props
 * @param {Array} props.users - Array of { src, name, userId }
 * @param {number} [props.max=4] - Max visible avatars
 * @param {'xs'|'sm'|'md'|'lg'} [props.size='md']
 */
function AvatarGroup({ users, max = 4, size = 'md' }) {
  const px = SIZES[size] || SIZES.md;
  const overlap = Math.round(px * 0.25);
  const visible = users.slice(0, max);
  const overflow = users.length - max;

  return (
    <div
      style={{ display: 'flex', flexDirection: 'row-reverse', alignItems: 'center' }}
      role="group"
      aria-label={`${users.length} members`}
    >
      {overflow > 0 && (
        <div
          style={{
            width: px,
            height: px,
            borderRadius: '50%',
            backgroundColor: '#e5e7eb',
            border: '2px solid white',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            fontSize: Math.round(px * 0.32),
            fontWeight: 600,
            color: '#374151',
            marginLeft: -overlap,
            zIndex: 0,
          }}
          aria-label={`${overflow} more members`}
        >
          +{overflow}
        </div>
      )}
      {visible.reverse().map((user, i) => (
        <div
          key={user.userId || i}
          style={{ marginLeft: i === visible.length - 1 ? 0 : -overlap, zIndex: i + 1 }}
        >
          <Avatar
            src={user.src}
            name={user.name}
            userId={user.userId}
            size={size}
            style={{ border: '2px solid white', boxSizing: 'content-box' }}
          />
        </div>
      ))}
    </div>
  );
}

export { Avatar, AvatarGroup };
```

---

## 9. Avatar Component — SwiftUI

```swift
import SwiftUI

struct AvatarView: View {
    let imageURL: URL?
    let name: String
    let size: CGFloat
    var status: OnlineStatus?
    var shape: AvatarShape = .circle

    enum AvatarShape {
        case circle, roundedSquare
    }

    enum OnlineStatus {
        case online, away, busy, offline

        var color: Color {
            switch self {
            case .online: return .green
            case .away: return .yellow
            case .busy: return .red
            case .offline: return .gray
            }
        }
    }

    private var initials: String {
        let parts = name.split(separator: " ")
        if parts.count >= 2 {
            return "\(parts.first!.prefix(1))\(parts.last!.prefix(1))".uppercased()
        }
        return String(name.prefix(1)).uppercased()
    }

    private var backgroundColor: Color {
        let colors: [Color] = [.red, .blue, .green, .orange, .purple, .teal, .pink, .indigo]
        let hash = name.unicodeScalars.reduce(0) { $0 + Int($1.value) }
        return colors[abs(hash) % colors.count].opacity(0.7)
    }

    var body: some View {
        ZStack(alignment: .bottomTrailing) {
            Group {
                if let url = imageURL {
                    AsyncImage(url: url) { image in
                        image.resizable().aspectRatio(contentMode: .fill)
                    } placeholder: {
                        initialsView
                    }
                } else {
                    initialsView
                }
            }
            .frame(width: size, height: size)
            .clipShape(avatarShape)

            if let status = status {
                Circle()
                    .fill(status.color)
                    .frame(width: size * 0.28, height: size * 0.28)
                    .overlay(
                        Circle().stroke(.white, lineWidth: 2)
                    )
                    .offset(x: 2, y: 2)
            }
        }
        .accessibilityLabel(name)
    }

    private var initialsView: some View {
        ZStack {
            backgroundColor
            Text(initials)
                .font(.system(size: size * 0.38, weight: .semibold))
                .foregroundStyle(.white)
        }
    }

    @ViewBuilder
    private var avatarShape: some Shape {
        switch shape {
        case .circle:
            Circle()
        case .roundedSquare:
            RoundedRectangle(cornerRadius: size * 0.2, style: .continuous)
        }
    }
}

// Avatar Group
struct AvatarGroupView: View {
    let users: [(name: String, imageURL: URL?)]
    var maxVisible: Int = 4
    var size: CGFloat = 40

    var body: some View {
        HStack(spacing: -(size * 0.25)) {
            ForEach(Array(users.prefix(maxVisible).enumerated()), id: \.offset) { index, user in
                AvatarView(imageURL: user.imageURL, name: user.name, size: size)
                    .overlay(Circle().stroke(.white, lineWidth: 2))
                    .zIndex(Double(maxVisible - index))
            }

            if users.count > maxVisible {
                ZStack {
                    Circle().fill(.gray.opacity(0.2))
                    Text("+\(users.count - maxVisible)")
                        .font(.system(size: size * 0.3, weight: .semibold))
                        .foregroundStyle(.secondary)
                }
                .frame(width: size, height: size)
                .overlay(Circle().stroke(.white, lineWidth: 2))
            }
        }
        .accessibilityElement(children: .combine)
        .accessibilityLabel("\(users.count) members")
    }
}
```

---

## 10. Media Accessibility Checklist

| Media Type | Required | WCAG Level |
|-----------|----------|------------|
| All images | Alt text (or `alt=""` for decorative) | A (1.1.1) |
| Pre-recorded video | Captions | A (1.2.2) |
| Pre-recorded audio | Transcript | A (1.2.1) |
| Pre-recorded video | Audio description | AA (1.2.5) |
| Live video | Captions | AA (1.2.4) |
| Autoplay media | Pause/stop mechanism | A (1.4.2) |
| Animation | Respect `prefers-reduced-motion` | AAA (2.3.3) |
| Custom player | Keyboard-accessible controls | A (2.1.1) |
| Carousel | Pause, stop, hide mechanism | A (2.2.2) |
| Media controls | Minimum 44x44px touch target | AA (2.5.8) |
| Color-only info | Not conveyed by color alone | A (1.4.1) |
| Focus | Visible focus indicator on controls | AA (2.4.7) |
