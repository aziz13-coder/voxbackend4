# Build Instructions

## Prerequisites
- Node.js 16+ 
- Python 3.8+
- npm 8+

## Development Build
```bash
cd frontend
npm install
npm run dev
```

## Production Build Process

### 1. Prepare Environment
```bash
cd frontend
npm install
```

### 2. Build Frontend
```bash
npm run clean:build
npm run build
```

### 3. Build Backend Executable
```bash
npm run build-backend-exe
```

### 4. Package Application
```bash
# Windows Installer
npm run electron:build:win

# Microsoft Store
npm run electron:build:win-store

# Quick test build
npm run electron:pack
```

## Output Files
- `dist-electron/Vox Stella Setup 1.1.0.exe` - Windows installer
- `dist-electron/Horary Master 1.1.0.appx` - Microsoft Store package
- `dist-electron/win-unpacked/` - Unpacked application

## Troubleshooting
1. Run `npm run clean` to clear cache
2. Ensure Python backend builds without errors
3. Check `validate-icons.js` for asset issues
4. Review build logs in console

## Distribution
Ready for:
- Direct download distribution
- Microsoft Store submission
- Enterprise deployment