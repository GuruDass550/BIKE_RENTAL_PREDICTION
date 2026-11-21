# Bike Rental Demand API

A random forest regression model estimates how many bikes will be rented during one hour. It uses the temperature, hour, weekend status, and rain status. The CSV contains 600 synthetic examples. The reported mean absolute error measures performance on held-out synthetic examples. Real rental records would be needed to measure real-world accuracy.

## Run in VS Code on Windows

Extract the ZIP and open the folder containing app.py in VS Code. In PowerShell run:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe train.py
.\.venv\Scripts\python.exe -m uvicorn app:app --host 0.0.0.0 --port 10000
```

Open http://127.0.0.1:10000/docs. Select **POST /predict**, click **Try it out**, and execute:

```json
{"temperature_c": 24, "hour": 17, "weekend": false, "raining": false}
```

Look for HTTP 200 and an integer in predicted_rentals. From a second VS Code terminal, the same test can be run with PowerShell:

```powershell
Invoke-RestMethod http://127.0.0.1:10000/predict -Method Post -ContentType 'application/json' -Body '{"temperature_c":24,"hour":17,"weekend":false,"raining":false}'
```

Run ipconfig in the second terminal, find the PC's Wi-Fi IPv4 address, and open http://YOUR-PC-IP:10000/docs from a phone on the same Wi-Fi. Keep the server running. If Windows asks, allow access on your trusted Private network.

## GitHub and Render

Create a new empty GitHub repository, then run these commands from the folder containing Dockerfile. Replace the repository URL with your own.

```powershell
git init -b main
git add .
git status --short
git commit -m "Add bike rental demand API"
git remote add origin https://github.com/YOUR-USERNAME/bike-demand-api.git
git push -u origin main
```

Connect that repo to a new Render **Web Service**. Select branch **main** and language **Docker**. Leave **Root Directory** blank when Dockerfile is at the top level of the GitHub repo. Use **./Dockerfile** as the Dockerfile path and select **Free** for the instance type. The Docker build trains the model using the included CSV. After deployment, open the public HTTPS URL with /docs appended and run the same prediction.
