import pytest
from copier import run_copy
import os
import tempfile
import shutil


@pytest.fixture
def temp_project_dir():
    """Create a temporary directory for testing project generation"""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


def test_fastapi_template(temp_project_dir):
    """Test that FastAPI template is generated correctly"""
    # Run copier to create project from template
    run_copy(
        ".",
        temp_project_dir,
        trust=True,
        data={
            "project_name": "test_project",
            "project_description": "A test project",
            "author_name": "Test Author",
            "author_email": "test@example.com",
            "framework": "fastapi",
            "domain": "test.example.com",
            "use_loki": True,
        },
    )

    # Check that key files exist
    assert os.path.exists(os.path.join(temp_project_dir, "src/main.py"))
    assert os.path.exists(os.path.join(temp_project_dir, "tests/test_main.py"))
    assert os.path.exists(os.path.join(temp_project_dir, "pyproject.toml"))

    # Check that Flask files don't exist
    assert not os.path.exists(os.path.join(temp_project_dir, "src/app.py"))
    assert not os.path.exists(os.path.join(temp_project_dir, "tests/test_app.py"))

    # TODO: Add more specific checks for file contents
