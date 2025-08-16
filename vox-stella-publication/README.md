# Vox Stella - Traditional Horary Astrology

Professional desktop application for traditional horary astrology analysis using William Lilly's methods.

## Version
1.1.0

## System Requirements
- Windows 10/11 (x64)
- macOS 10.15+ (prepared)
- Linux (prepared)

## Quick Start

### Optimized for OpenAI Codex/Dev-Containers
This repo includes runtime optimization files:
- `.mise.toml` - Specifies only Python 3.12 + Node.js 20 (skips Ruby, Rust, Go, Swift, PHP)
- `.devcontainer/` - Pre-configured dev-container setup
- `.tool-versions` - Alternative runtime specification

### Development Setup
```bash
# Install dependencies
cd frontend && npm install
cd ../backend && pip install -r requirements.txt

# Run development
npm run dev              # Frontend
npm run dev:backend      # Backend

# Build for production
npm run build:production
```

### Faster Setup (Lightweight)
```bash
# Use lightweight dependencies for faster setup
cd backend && pip install -r ../requirements-codex.txt
cd ../frontend && npm install --production
```

### Production Build
```bash
# Full production build (Windows)
npm run build:production

# Output: dist-electron/Vox Stella Setup 1.1.0.exe
```

## Backend Quick Start
```bash
cd backend
pip install -r requirements.txt
gunicorn -c gunicorn.conf.py backend.app:app
# then visit http://localhost:5000/healthz
```

## Features
- Traditional horary chart analysis
- Enhanced chart wheel visualization
- Comprehensive dignity analysis
- Moon void-of-course detection
- Solar conditions (cazimi, combustion)
- Mutual reception analysis
- AI analysis integration
- Chart sharing capabilities

## License
Commercial - All rights reserved

## Support
For technical support and inquiries, please contact support@voxstella.com

---
© 2025 Vox Stella Team