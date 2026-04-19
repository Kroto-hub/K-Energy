@echo off
echo ========================================
echo   K-Energy 启动脚本
echo ========================================
echo.

cd /d "%~dp0"

echo [1/2] 启动后端 (http://localhost:8000) ...
start "K-Energy Backend" cmd /k "cd backend && python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload"
timeout /t 3 /nobreak >nul

echo [2/2] 启动前端 (http://localhost:5173) ...
start "K-Energy Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo ========================================
echo   启动完成！
echo   前端: http://localhost:5173
echo   后端: http://localhost:8000
echo   API文档: http://localhost:8000/docs
echo ========================================
echo.
echo 按任意键关闭此窗口（不会停止服务）...
pause >nul
