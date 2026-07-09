import os
import sys
import subprocess

def app():
    try:
        script_path = os.path.join("app", "app.py")

        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"Streamlit script not found at expected path: {script_path}")
        print(f"Starting Streamlit application: {script_path}")
        
        subprocess.run([sys.executable, "-m", "streamlit", "run", script_path], check=True)
        
    except FileNotFoundError as fnfe:
        print(f"Error: {fnfe}", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as cpe:
        print(f"Streamlit process exited with error code {cpe.returncode}", file=sys.stderr)
        sys.exit(cpe.returncode)
    except KeyboardInterrupt:
        print("\nStreamlit application stopped by user.", file=sys.stdout)
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    app()