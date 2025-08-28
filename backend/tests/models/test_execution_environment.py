"""Unit tests for the ExecutionEnvironment model."""
import pytest
from pydantic import ValidationError

from backend.models.execution_environment import (
    ExecutionEnvironment,
    ResourceLimits,
    VolumeMount,
)


def test_resource_limits_creation():
    """Test successful ResourceLimits model creation."""
    limits = ResourceLimits(memory_mb=1024, cpu_limit=1.5, timeout_seconds=1800)
    assert limits.memory_mb == 1024
    assert limits.cpu_limit == 1.5
    assert limits.timeout_seconds == 1800


def test_resource_limits_defaults():
    """Test that default values are set correctly for ResourceLimits."""
    limits = ResourceLimits()
    assert limits.memory_mb == 512
    assert limits.cpu_limit == 1.0
    assert limits.timeout_seconds == 3600


def test_volume_mount_creation():
    """Test successful VolumeMount model creation."""
    mount = VolumeMount(
        host_path="/path/on/host", container_path="/path/in/container", read_only=True
    )
    assert mount.host_path == "/path/on/host"
    assert mount.container_path == "/path/in/container"
    assert mount.read_only is True


def test_execution_environment_creation():
    """Test successful ExecutionEnvironment model creation."""
    env_data = {
        "name": "test-env",
        "base_image": "python:3.11-slim",
        "dockerfile_content": "RUN pip install requests",
        "environment_variables": {"API_KEY": "12345"},
        "volumes": [
            {
                "host_path": "/data",
                "container_path": "/app/data",
                "read_only": False,
            }
        ],
        "resource_limits": {"memory_mb": 2048},
    }
    env = ExecutionEnvironment(**env_data)

    assert env.name == env_data["name"]
    assert env.base_image == env_data["base_image"]
    assert env.dockerfile_content == env_data["dockerfile_content"]
    assert env.environment_variables == env_data["environment_variables"]
    assert len(env.volumes) == 1
    assert env.volumes[0].host_path == "/data"
    assert env.resource_limits.memory_mb == 2048
    assert env.resource_limits.cpu_limit == 1.0  # Default value


def test_execution_environment_missing_required_fields():
    """Test that validation fails for missing required fields."""
    with pytest.raises(ValidationError) as excinfo:
        ExecutionEnvironment(name="test-env")
    assert "base_image" in str(excinfo.value)


def test_execution_environment_invalid_data():
    """Test that validation fails for invalid data types."""
    with pytest.raises(ValidationError):
        ExecutionEnvironment(
            name="test-env",
            base_image="ubuntu",
            resource_limits={"memory_mb": "not-a-number"},
        )
