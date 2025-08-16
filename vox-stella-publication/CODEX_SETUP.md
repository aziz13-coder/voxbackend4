# Codex Development Setup

## Quick Start (Lightweight)

For faster Codex setup, use the lightweight dependencies:

```bash
# Backend (lightweight)
cd backend
pip install -r ../requirements-codex.txt

# Frontend
cd ../frontend  
npm install --production
```

## Full Setup (Complete Features)

```bash
# Full dependencies (slower but complete)
cd backend
pip install -r requirements.txt

cd ../frontend
npm install
```

## Common Issues & Solutions

### 1. Long Setup Time
- **Expected**: Initial setup takes 2-3 minutes due to Swiss Ephemeris compilation
- **Solution**: Use `requirements-codex.txt` for development

### 2. npm Security Warnings
- **Status**: 2 moderate vulnerabilities (expected in development)
- **Solution**: Run `npm audit fix` after setup

### 3. Deprecation Warnings
- **Status**: Normal for astrology packages (using older stable versions)
- **Impact**: None on functionality

## Development Commands

```bash
# Frontend development
npm run dev

# Backend development  
python app.py

# Quick test
python -c "from horary_engine.engine import HoraryEngine; print('✅ Engine loads')"
```

## Codex-Friendly Features

- ✅ Lightweight dependency option
- ✅ Clear error handling
- ✅ Modular architecture
- ✅ Comprehensive documentation
- ✅ Type hints and comments