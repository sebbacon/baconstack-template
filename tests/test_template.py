import os
import subprocess
import time
import requests
import pytest
from copier import run_copy
import tempfile
import shutil
import signal


@pytest.fixture
def project_dir():
    # Create a temporary directory for the test project
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    # Cleanup after test
    shutil.rmtree(temp_dir)


def test_flask_template(project_dir):
    # Generate project from template
    run_copy(
        ".",
        project_dir,
        data={
            "project_name": "test_project",
            "framework": "flask",
            "project_description": "Test Flask App",
            "domain": "test.example.com",
            "author_name": "Test Author",
            "author_email": "test@example.com",
            "use_loki": False,
        },
        unsafe=True,
        vcs_ref="HEAD",
    )

    # Change to project directory
    original_dir = os.getcwd()
    os.chdir(project_dir)

    try:
        # Start the Flask app in the background
        process = subprocess.Popen(
            ["just", "dev"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            preexec_fn=os.setsid,  # Create new process group
        )

        # Wait for server to start
        time.sleep(2)

        try:
            # Test if server is responding
            response = requests.get("http://localhost:8001")
            assert response.status_code == 200
        finally:
            # Cleanup: kill the server process group
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
            process.wait()

    finally:
        # Return to original directory
        os.chdir(original_dir)
