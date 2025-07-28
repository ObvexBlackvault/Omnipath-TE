# AutoDeploy.bashrc  place in ~/Omnipath and then:
#   source ~/Omnipath/AutoDeploy.bashrc
# to spin up your env + server.

# 1) Activate Python venv
if [ -f "$HOME/Omnipath/venv/bin/activate" ]; then
  source "$HOME/Omnipath/venv/bin/activate"
fi

# 2) Start FastAPI backend if not already running
_backend_pid=$(pgrep -f "uvicorn backend.cli:app")
if [ -z "$_backend_pid" ]; then
  nohup uvicorn backend.cli:app --host 0.0.0.0 --port 8000 \
    > ~/Omnipath/logs/backend.out 2>&1 &
  echo " Backend started (logs in ~/Omnipath/logs/backend.out)"
fi

# 3) Start React frontend (Tier1_UI) if not running
_frontend_pid=$(pgrep -f "npm start --prefix Tier1_UI")
if [ -z "$_frontend_pid" ]; then
  nohup npm start --prefix ~/Omnipath/Tier1_UI \
    > ~/Omnipath/logs/frontend.out 2>&1 &
  echo " Frontend started (logs in ~/Omnipath/logs/frontend.out)"
fi
